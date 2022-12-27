<template>
    <div
        id="app"
        class="flex flex-col items-center bg-white h-screen bg-slate-100 text-slate-900 px-4 py-8 selection:bg-rose-500 selection:text-white"
    >
        <!-- Heading desktop -->
        <div class="hidden md:block text-center">
            <h1 class="text-4xl pt-8 pb-4">
                <span class="text-slate-500">
                    When learning a new language,
                </span>
                <span class="text-slate-900 underline decoration-rose-500">
                    the first 1000
                </span>
                <span class="text-slate-500">
                    words are the most important.
                </span>
            </h1>

            <!-- Subtitle -->
            <h2 class="text-2xl pb-12">
                <span class="text-slate-400">
                    Here you can learn your first 1000 words in French 🇫🇷.
                </span>
            </h2>
        </div>

        <!-- Heading mobile -->
        <div class="block md:hidden">
            <h1 class="text-4xl pb-4">
                <span class="text-slate-900 underline decoration-rose-500">
                    the first 1000
                </span>
            </h1>
        </div>

        <!-- Flash cards -->
        <div class="flex gap-4">
            <!-- Search box -->
            <input
                v-if="!quizMode"
                v-model="search"
                class="h-8 md:h-12 w-full md:w-96 rounded-full border-2 border-slate-200 p-4 text-xl md:text-2xl focus:border-rose-500 outline-none"
                type="text"
                placeholder="Search for a word"
            />

            <!-- Quiz button -->
            <button
                class="h-8 md:h-12 w-8 md:w-12 flex justify-center items-center rounded-full border-2 border-slate-200 p-4 text-xl md:text-2xl bg-white hover:bg-slate-100 outline-none"
                @click="quizMode = !quizMode"
                title="Quiz"
            >
                <span class="translate-y-px">🎓</span>
            </button>

            <!-- Hide translations -->
            <button
                v-if="!quizMode"
                class="h-8 md:h-12 w-8 md:w-12 flex justify-center items-center rounded-full border-2 border-slate-200 p-4 text-xl md:text-2xl bg-white hover:bg-slate-100 outline-none"
                @click="hideTranslations = !hideTranslations"
                title="Hide translations"
            >
                <span class="-translate-y-px">📖</span>
            </button>
        </div>

        <carousel
            v-if="!quizMode"
            :words="wordsFiltered"
            :hide-translations="hideTranslations"
        ></carousel>

        <!-- Quiz -->
        <div v-if="quizMode">
            <quiz
                :words="wordsFiltered"
                :wordScores="wordScores"
                :elo="elo"
                @test-result="onTestResult"
            ></quiz>
        </div>

        <!-- Footer -->
        <div class="flex flex-col flex-1 items-center place-content-end mt-8">
            <div class="text-sm text-slate-400">
                <span class="text-slate-500">Made with ❤️ by </span>
                <a
                    class="text-slate-900 underline decoration-rose-500"
                    href="https://github.com/xdgfx"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    xdgfx
                </a>
            </div>
            <div class="text-sm text-slate-400">
                <span class="text-slate-500">Notice a mistake? </span>
                <a
                    class="text-slate-900 underline decoration-rose-500"
                    href="https://github.com/XDGFX/the-first-1000/issues/new"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    Let me know!
                </a>
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

            // Parameters for the quiz
            elo: JSON.parse(localStorage.getItem("elo")) || 500, // Init to 500 elo
            wordScores: JSON.parse(localStorage.getItem("wordScores")) || {}, // Words default to 0.5
        };
    },
    computed: {
        wordsFiltered() {
            // When not in quiz mode, words are filtered by the search box
            if (!this.quizMode) {
                // If the search box is empty, return all words
                if (this.search === "") {
                    return words;
                }

                // Otherwise, return the words that match the search query
                const fuse = new Fuse(words, {
                    keys: [
                        { name: "word", weight: 4 },
                        { name: "translation", weight: 4 },
                        "example",
                        "example_en",
                        { name: "tags", weight: 2 },
                        { name: "synonyms", weight: 3 },
                    ],
                    shouldSort: true,
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
            this.wordScores[word.word] = this.wordScores[word.word] || 0.5;

            // Adjust the score based on whether the user got the answer right or wrong
            const adjustment = correct ? 0.1 : -0.1;
            this.wordScores[word.word] = Math.min(
                Math.max(this.wordScores[word.word] + adjustment, 0),
                1
            );

            // Update the elo
            this.elo = Math.min(
                Math.max(this.elo + (correct ? 2 : -2), 0),
                2000
            );
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
    },
};
</script>

<style></style>
