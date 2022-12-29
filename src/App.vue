<template>
    <div
        id="app"
        class="flex flex-col items-center bg-white h-screen bg-slate-100 text-slate-900 px-4 py-8 selection:bg-rose-500 selection:text-white"
    >
        <!-- Menu -->
        <div class="w-full lg:w-[990px] flex flex-wrap items-center">
            <h1 class="text-2xl md:text-4xl flex-1">
                <span
                    class="text-slate-900 underline decoration-rose-500 whitespace-nowrap"
                >
                    the first 1000
                </span>
            </h1>

            <div class="flex flex-2 gap-4 items-center">
                <!-- Search box -->
                <input
                    v-if="!quizMode"
                    v-model="search"
                    class="h-8 md:h-12 shrink rounded-full border-2 border-slate-200 p-4 text-xl md:text-2xl focus:border-rose-500 outline-none"
                    type="text"
                    placeholder="Search"
                />

                <!-- Hide translations -->
                <button
                    v-if="!quizMode"
                    class="h-8 md:h-12 w-8 md:w-12 flex justify-center items-center rounded-full border-2 border-slate-200 p-4 text-xl md:text-2xl bg-white hover:bg-slate-100 outline-none"
                    @click="hideTranslations = !hideTranslations"
                    title="Hide translations"
                >
                    <span>🔖</span>
                </button>

                <span
                    v-if="!quizMode"
                    class="text-slate-300 text-4xl select-none -translate-y-1"
                    >·</span
                >

                <!-- Quiz button -->
                <button
                    class="h-8 md:h-12 w-8 md:w-12 flex justify-center items-center rounded-full border-2 border-slate-200 text-slate-500 p-4 text-xl md:text-2xl bg-white hover:bg-slate-100 outline-none"
                    @click="
                        quizMode = !quizMode;
                        firstLoad = false;
                    "
                    title="Practice"
                >
                    <span v-if="quizMode" class="-translate-y-px"> 📖 </span>
                    <span v-else class="translate-y-px"> 🎓 </span>

                    <!-- Notification circle -->
                    <div
                        v-if="!quizMode && firstLoad"
                        class="absolute h-4 w-4 translate-x-full -translate-y-full"
                    >
                        <div
                            class="h-4 w-4 rounded-full bg-cyan-400 animate-ping"
                        ></div>
                        <div
                            class="h-4 w-4 rounded-full bg-cyan-400 -translate-y-full"
                        ></div>
                    </div>
                </button>
            </div>
        </div>

        <carousel
            v-if="!quizMode"
            :words="wordsFiltered"
            :wordScores="wordScores"
            :hide-translations="hideTranslations"
        ></carousel>

        <!-- Quiz -->
        <quiz
            v-if="quizMode"
            :words="wordsFiltered"
            :wordScores="wordScores"
            :elo="elo"
            :score="score"
            @test-result="onTestResult"
        ></quiz>

        <!-- Footer -->
        <div
            class="flex flex-col flex-1 items-center place-content-end mt-2 md:mt-8"
        >
            <div
                class="text-xs md:text-sm text-slate-500 flex gap-2 text-center items-center"
            >
                <div>
                    Made with ❤️ by

                    <a
                        class="text-slate-900 underline decoration-rose-500"
                        href="https://github.com/xdgfx"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        xdgfx</a
                    >
                </div>
                ·
                <div>
                    <a
                        class="text-slate-900"
                        href="https://ko-fi.com/callumm"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        Buy me a coffee ☕</a
                    >
                </div>
                ·
                <div>
                    Notice a mistake?
                    <a
                        class="text-slate-900 underline decoration-rose-500"
                        href="https://github.com/XDGFX/the-first-1000/issues/new"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        Let me know!</a
                    >
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Fuse from "fuse.js";

import words from "@/french.json";
import Carousel from "@/components/Carousel.vue";
import Quiz from "@/components/Quiz.vue";

export default {
    name: "App",
    components: {
        Carousel,
        Quiz,
    },
    data() {
        return {
            search: "",
            hideTranslations: false,
            quizMode: false,

            firstLoad: localStorage.getItem("elo") === null, // If this is the first time the user has loaded the page

            // Parameters for the quiz
            elo: JSON.parse(localStorage.getItem("elo")) || 500, // Init to 500 elo
            score: JSON.parse(localStorage.getItem("score")) || 0, // Init to 0 score
            wordScores: JSON.parse(localStorage.getItem("wordScores")) || {}, // Words default to 0.5
        };
    },
    computed: {
        wordsFiltered() {
            // When not in quiz mode, words are filtered by the search box
            if (!this.quizMode) {
                words.sort((a, b) => {
                    // Sort the words based on their score in the wordScores
                    // object, and then based on difficulty (easy first)
                    const aScore = this.wordScores[a.word] || 10;
                    const bScore = this.wordScores[b.word] || 10;

                    if (aScore === bScore) {
                        return a.difficulty - b.difficulty;
                    }

                    return aScore - bScore;
                });

                // If the search box is empty, return all words
                if (this.search === "") {
                    return words;
                }

                // Otherwise, return the words that match the search query
                const fuse = new Fuse(words, {
                    keys: [
                        { name: "word", weight: 6 },
                        { name: "translation", weight: 6 },
                        "example",
                        "example_en",
                        { name: "tags", weight: 2 },
                        { name: "synonyms", weight: 3 },
                    ],
                    shouldSort: true,
                    ignoreLocation: true,
                });
                const results = fuse.search(
                    this.search.replace(/\s+/g, " ").toLowerCase()
                );

                return results.map((result) => result.item);
            } else {
                // When in quiz mode, words are filtered by your elo, and the
                // difficulty of the word.
                //
                // Difficulty Level | Elo
                // -------------------------
                // 1                | 0 - 800
                // 1, 2             | 800 - 1200
                // 1, 2, 3          | 1200 - 1600
                // all              | 1600 - 2000
                return words.filter((word) => {
                    if (this.elo < 800) {
                        return word.difficulty === 1;
                    } else if (this.elo < 1200) {
                        return word.difficulty <= 2;
                    } else if (this.elo < 1600) {
                        return word.difficulty <= 3;
                    } else {
                        return true;
                    }
                });
            }
        },
    },

    methods: {
        // When the quiz is finished, update the elo and wordScores
        onTestResult(word, correct) {
            // Update the wordScores
            this.wordScores[word.word] = this.wordScores[word.word] || 5;

            // Adjust the score based on whether the user got the answer right or wrong
            const adjustment = correct ? 1 : -1;
            this.wordScores[word.word] = Math.min(
                Math.max(this.wordScores[word.word] + adjustment, 0),
                10
            );

            // Update the elo
            this.elo = Math.min(
                Math.max(this.elo + (correct ? 2 : -2), 0),
                2000
            );

            // Update the score
            this.score += correct ? 10 : 0;
            this.score = Math.min(this.score, 20000);
        },
    },

    watch: {
        // When the elo changes, save it to localStorage
        elo() {
            // If elo is not a number, raise an error
            if (isNaN(this.elo)) {
                throw new Error("Elo is not a number");
            }

            localStorage.setItem("elo", JSON.stringify(this.elo));
        },

        // When the wordScores change, save them to localStorage
        wordScores: {
            handler(newValue, oldValue) {
                localStorage.setItem(
                    "wordScores",
                    JSON.stringify(this.wordScores)
                );
            },
            deep: true,
        },

        // When the score changes, save it to localStorage
        score() {
            if (isNaN(this.score)) {
                throw new Error("Score is not a number");
            }

            localStorage.setItem("score", JSON.stringify(this.score));
        },
    },
};
</script>

<style></style>
