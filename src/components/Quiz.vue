<template>
    <div class="flex flex-col items-center justify-center w-full lg:w-[990px]">
        <div class="mt-4 mb-8 w-full">
            <EloRange :elo="elo" :score="score"></EloRange>
        </div>

        <!-- Current Mode -->
        <div
            class="w-24 h-7 translate-y-1/2 text-xl text-center justify-self-center"
        >
            <div v-if="page !== 'start'">
                <Transition name="spin">
                    <div
                        v-if="mode === 'foreign'"
                        class="bg-slate-100 border-2 border-slate-300 rounded-full px-2 w-24 h-8 absolute"
                    >
                        🇬🇧 ➜ 🇫🇷
                    </div>
                    <div
                        v-else
                        class="bg-slate-100 border-2 border-slate-300 rounded-full px-2 w-24 h-8 absolute"
                    >
                        🇫🇷 ➜ 🇬🇧
                    </div>
                </Transition>
            </div>
        </div>

        <div
            class="min-h-[384px] bg-white border-2 border-slate-200 rounded-[18px] flex flex-col items-center justify-center w-full lg:w-[990px]"
        >
            <div
                v-if="page === 'start'"
                class="text-l md:text-xl my-8 text-center flex flex-col gap-2"
            >
                <div class="text-6xl">🎓</div>
                <div class="mb-4 text-6xl">Practice</div>
                <div>Translate each word accurately to level up.</div>
                <div>
                    Words you struggle with will be tested
                    <span class="underline decoration-2 decoration-rose-500"
                        >more often</span
                    >, to help you remember!
                </div>
                <div>
                    As you get
                    <span class="underline decoration-2 decoration-rose-500"
                        >better</span
                    >, the words will get
                    <span class="underline decoration-2 decoration-rose-500"
                        >harder</span
                    >, and you'll have to translate more words to level up.
                </div>
                <button
                    class="flex self-center items-center justify-center h-8 md:h-12 w-48 rounded-full border-2 border-slate-300 p-4 m-8 text-xl md:text-2xl bg-white hover:bg-slate-200 outline-none"
                    @click="nextWord()"
                >
                    Ready?
                </button>
            </div>

            <div v-else>
                <div class="w-full h-full grid grid-rows-6 text-center">
                    <!-- Word -->
                    <div
                        ref="word"
                        class="text-slate-900 my-auto whitespace-nowrap py-4 row-span-3"
                        :style="wordSizeStyle"
                        :class="{
                            'text-emerald-500': lastTestResult === true,
                            'text-rose-500': lastTestResult === false,
                        }"
                    >
                        {{
                            lastTestResult !== null
                                ? mode === "foreign"
                                    ? currentWord.word
                                    : currentWord.translation
                                : mode === "native"
                                ? currentWord.word
                                : currentWord.translation
                        }}
                    </div>

                    <!-- Example -->
                    <div>
                        <div class="text-xl">
                            {{
                                mode === "foreign"
                                    ? currentWord.example_en
                                    : currentWord.example
                            }}
                        </div>
                        <div
                            v-if="lastTestResult !== null"
                            class="text-xl"
                            :class="{
                                'text-emerald-500': lastTestResult === true,
                                'text-rose-500': lastTestResult === false,
                            }"
                        >
                            {{
                                mode === "foreign"
                                    ? currentWord.example
                                    : currentWord.example_en
                            }}
                        </div>
                    </div>

                    <div class="row-span-2">
                        <!-- Input for user to enter the answer -->
                        <input
                            v-show="lastTestResult === null"
                            class="h-8 md:h-12 w-full md:w-96 rounded-full border-2 border-slate-200 p-4 m-8 text-xl md:text-2xl bg-white hover:bg-slate-100 focus:border-rose-500 outline-none"
                            v-model="answer"
                            @keydown.enter="submitAnswer"
                            ref="answerInput"
                            :placeholder="
                                mode === 'foreign'
                                    ? 'What is this in French?'
                                    : 'What does this mean?'
                            "
                        />

                        <!-- Button to continue after result screen -->
                        <button
                            v-show="lastTestResult !== null"
                            class="flex items-center justify-center h-8 md:h-12 w-full md:w-96 rounded-full border-2 border-slate-200 p-4 m-8 text-xl md:text-2xl bg-white hover:bg-slate-100 outline-none"
                            @click="nextWord"
                            ref="continueButton"
                        >
                            Continue
                        </button>
                    </div>
                </div>
            </div>
        </div>
        <div v-if="debugMode" class="text-xs">
            <code>
                <br />
                <span
                    @click="
                        answer =
                            mode == native
                                ? currentWord.word
                                : currentWord.translation;
                        submitAnswer();
                    "
                >
                    CORRECT
                </span>
                <span
                    @click="
                        answer = '';
                        submitAnswer();
                    "
                >
                    INCORRECT
                </span>
                <br />
                <br />

                currentWord: {{ currentWord }} <br />

                <br />

                lowScoreMode: {{ lowScoreMode }} <br />
                mode: {{ mode }} <br />
                modeTestCount: {{ modeTestCount }} <br />
            </code>
        </div>
    </div>
</template>

<script>
import Fuse from "fuse.js";
import diacritics from "diacritics";

import EloRange from "@/components/EloRange.vue";

export default {
    name: "QuizButton",
    emits: ["test-result"],
    components: { EloRange },
    inject: ["debugMode"],
    data() {
        return {
            // The word that is currently being displayed
            currentWord: null,

            // The result of the last test
            lastTestResult: null,

            // Indicates more than 20 words with a score of less than 5
            lowScoreMode: false,

            // The answer that the user has entered
            answer: "",

            // The current page from "start", "test", "result"
            page: "start",

            // Random selection between foreign and native mode
            mode: Math.random() > 0.5 ? "foreign" : "native",
            modeTestCount: 0, // Number of tests performed in the current mode
        };
    },
    props: {
        words: {
            type: Array,
            required: true,
        },
        wordScores: {
            type: Object,
            required: true,
        },
        elo: {
            type: Number,
            required: true,
        },
        score: {
            type: Number,
            required: true,
        },
    },
    methods: {
        getWord() {
            // If there's more than 20 words with a score of less than 5, then
            // only pick from those words
            const wordsWithLowScore = this.words.filter(
                (word) => (this.wordScores[word.word] || 5) < 5
            );

            this.lowScoreMode = wordsWithLowScore.length > 20;

            if (this.lowScoreMode) {
                console.log("Picking from words with low score");
                // Select a word at random from the list of words
                return wordsWithLowScore[
                    Math.floor(Math.random() * wordsWithLowScore.length)
                ];
            }

            // Select a word at random from the list of words
            const word =
                this.words[Math.floor(Math.random() * this.words.length)];

            // Get the score of the word
            const score = this.wordScores[word.word] || 5;

            // Calculate the probability of selecting the word
            const selectionProbability = Math.pow(Math.random(), 2) * 10;

            // If the selection probability is greater than the score, select
            // the word
            if (selectionProbability > score) {
                return word;
            } else {
                // Otherwise, select the next word
                return this.getWord();
            }
        },

        submitAnswer() {
            this.page = "result";

            // Get the user input, and split it into words
            const answerWords = this.answer.split(" ");

            // Get the correct answer, and split it into words
            let correctAnswerWord;
            if (this.mode === "foreign") {
                correctAnswerWord = this.currentWord.word;
            } else {
                correctAnswerWord = this.currentWord.translation;
            }

            // Remove diactrics and split the words
            const correctAnswerWords = diacritics
                .remove(correctAnswerWord)
                .split(" ");

            // Check if the answer is correct by comparing the words. Only one
            // word must match for the answer to be correct. Use Fuse to allow
            // fuzzy matches.
            const fuse = new Fuse(correctAnswerWords, {
                keys: ["word"],
                shouldSort: true,
                includeScore: true,
            });

            // Check if any of the words in the answer match the correct answer
            const isCorrect = answerWords.some((word) => {
                const results = fuse.search(diacritics.remove(word));
                return results.length > 0 && results[0].score < 0.2;
            });

            // Emit the test result
            this.$emit("test-result", this.currentWord, isCorrect);

            // Set the last test result
            this.lastTestResult = isCorrect;

            // Clear the answer
            this.answer = "";

            // Focus the continue button
            setTimeout(() => {
                this.$refs.continueButton.focus();
            }, 10);
        },

        nextWord() {
            this.page = "test";

            // Increment the mode test count
            this.modeTestCount++;

            // If the mode test count is greater than 10, switch the mode
            if (this.modeTestCount > 10) {
                this.mode = this.mode === "foreign" ? "native" : "foreign";
                this.modeTestCount = 0;
            }

            // Select the next word
            this.currentWord = this.getWord();

            // Clear the last test result
            this.lastTestResult = null;

            // Focus the answer input
            setTimeout(() => {
                this.$refs.answerInput.focus();
            }, 10);
        },
    },

    // beforeMount() {
    //     // Select the first word
    //     this.currentWord = this.getWord();
    // },

    computed: {
        wordSizeStyle() {
            // Based on the number of characters in the word, we can estimate the font size
            // <8 characters: 96px
            // 8-12 characters: 72px
            // 12-16 characters: 48px
            // 16-20 characters: 36px
            // 20+ characters: 24px

            const wordLength = this.currentWord.word.length;
            let fontSize = 96;

            if (wordLength >= 8 && wordLength < 12) {
                fontSize = 72;
            } else if (wordLength >= 12 && wordLength < 16) {
                fontSize = 48;
            } else if (wordLength >= 16 && wordLength < 20) {
                fontSize = 36;
            } else if (wordLength >= 20) {
                fontSize = 24;
            }

            return {
                fontSize: `${fontSize}px`,
            };
        },
    },
};
</script>

<style scoped>
.spin-enter-active,
.spin-leave-active {
    transition: all 0.5s ease-in-out;
}

.spin-enter-from {
    transform: rotate(-180deg);
    opacity: 0;
}

.spin-leave-to {
    transform: rotate(180deg);
    opacity: 0;
}
</style>
