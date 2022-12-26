<template>
    <div class="h-96 bg-slate-200 rounded-[18px] grid md:grid-cols-2 m-2">
        <!-- word -->
        <div
            class="flex flex-col items-center justify-center bg-slate-100 rounded-[18px] m-2"
        >
            <div
                ref="word"
                class="flex text-slate-900 whitespace-nowrap -mb-4"
                :style="wordSizeStyle"
            >
                {{ word.word }}
            </div>
            <div
                class="flex md:text-4xl text-slate-400 text-center px-4 py-2"
                v-show="!hideTranslations"
            >
                {{ word.translation }}
            </div>
            <AudioPlayer v-if="showTTS" :word="word.word"></AudioPlayer>
        </div>

        <div class="flex flex-col">
            <!-- Example -->
            <div class="flex flex-grow flex-col p-4 text-l md:text-2xl">
                <div class="flex justify-left items-center">
                    <div class="text-4xl pr-4">
                        {{ word.emoji }}
                    </div>
                    <div class="flex flex-col justify-center gap-2">
                        <AudioPlayer
                            v-if="showTTS"
                            :word="word.example"
                        ></AudioPlayer>
                        <p>"{{ word.example }}"</p>
                        <p class="text-slate-500" v-show="!hideTranslations">
                            "{{ word.example_en }}"
                        </p>
                    </div>
                </div>
            </div>

            <!-- Tags, difficulty -->
            <div class="p-4">
                <div class="pb-2 overflow-x-auto whitespace-nowrap">
                    <div class="px-2 text-sm text-slate-900">Tags</div>
                    <div class="flex text-slate-500 text-l">
                        <div
                            v-for="tag in word.tags"
                            :key="tag"
                            class="bg-slate-300 rounded-full m-2 px-2"
                        >
                            {{ tag }}
                        </div>
                    </div>
                </div>

                <div class="pb-2">
                    <div class="grid grid-cols-2 px-2">
                        <div class="text-sm text-slate-900">Synonyms</div>
                        <div class="text-right text-sm text-slate-900">
                            Antonyms
                        </div>
                    </div>
                    <div class="flex overflow-x-auto whitespace-nowrap">
                        <div class="flex flex-1 text-slate-900 text-l pr-4">
                            <div
                                v-for="synonym in word.synonyms"
                                :key="synonym"
                                class="bg-emerald-300 rounded-full m-2 px-2"
                            >
                                {{ synonym }}
                            </div>
                        </div>

                        <div
                            class="flex text-slate-900 text-l justify-self-end"
                        >
                            <div
                                v-for="antonym in word.antonyms"
                                :key="antonym"
                                class="bg-rose-300 rounded-full m-2 px-2"
                            >
                                {{ antonym }}
                            </div>
                        </div>
                    </div>
                </div>

                <DifficultyRange :value="word.difficulty" />
            </div>
        </div>
    </div>
</template>

<script>
import DifficultyRange from "@/components/DifficultyRange.vue";
import AudioPlayer from "@/components/AudioPlayer.vue";

export default {
    name: "Card",
    components: {
        DifficultyRange,
        AudioPlayer,
    },
    props: {
        word: {
            type: Object,
            required: true,
        },
        showTTS: {
            type: Boolean,
            default: false,
        },
        hideTranslations: {
            type: Boolean,
            default: false,
        },
    },
    computed: {
        wordSizeStyle() {
            // Based on the number of characters in the word, we can estimate the font size
            // <8 characters: 96px
            // 8-12 characters: 72px
            // 12-16 characters: 48px
            // 16-20 characters: 36px
            // 20+ characters: 24px

            const wordLength = this.word.word.length;
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
