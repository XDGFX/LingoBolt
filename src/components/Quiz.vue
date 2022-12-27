<template>
    <div class="mt-4">
        <EloRange :elo="elo" :score="score"></EloRange>
    </div>

    <div class="flex justify-center">
        <div
            class="min-h-[384px] bg-slate-200 rounded-[18px] flex flex-col items-center m-2 w-full lg:w-[990px]"
        >
            <!-- Test page -->
            <div
                class="w-full h-full grid grid-rows-6 text-center justify-items-center"
            >
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
                        mode === "foreign" || lastTestResult !== null
                            ? currentWord.translation
                            : currentWord.word
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
                        class="h-8 md:h-12 w-full md:w-96 rounded-full border-2 border-slate-200 p-4 m-8 text-xl md:text-2xl focus:border-rose-500 outline-none"
                        v-model="answer"
                        @keydown.enter="submitAnswer"
                        ref="answerInput"
                        placeholder="What does this mean?"
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
</template>

<script>
import Fuse from "fuse.js";

import EloRange from "@/components/EloRange.vue";

export default {
    name: "QuizButton",
    emits: ["test-result"],
    components: { EloRange },
    data() {
        return {
            // The word that is currently being displayed
            currentWord: null,

            // The answer that the user has entered
            answer: "",

            // The result of the last test
            lastTestResult: null,

            mode: "native", // foreign or native
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
        selectNextWord() {
            // Select a word at random from the list of words
            const word =
                this.words[Math.floor(Math.random() * this.words.length)];

            // Get the score of the word
            const score = this.wordScores[word.word] || 0.5;

            // Calculate the probability of selecting the word
            const selectionProbability = Math.pow(Math.random(), 2);

            // If the selection probability is greater than the score, select
            // the word
            if (selectionProbability > score) {
                return word;
            } else {
                // Otherwise, select the next word
                return this.selectNextWord();
            }
        },

        submitAnswer() {
            // Get the user input, and split it into words
            const answerWords = this.answer.split(" ");

            // Get the correct answer, and split it into words
            let correctAnswerWords;
            if (this.mode === "foreign") {
                correctAnswerWords = this.currentWord.word.split(" ");
            } else {
                correctAnswerWords = this.currentWord.translation.split(" ");
            }

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
                const results = fuse.search(word);
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
            // Select the next word
            this.currentWord = this.selectNextWord();

            // Clear the last test result
            this.lastTestResult = null;

            // Focus the answer input
            setTimeout(() => {
                this.$refs.answerInput.focus();
            }, 10);
        },
    },

    beforeMount() {
        // Select the first word
        this.currentWord = this.selectNextWord();
    },

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

<style></style>
