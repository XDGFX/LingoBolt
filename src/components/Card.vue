<template>
    <div class="h-[384px] bg-slate-200 rounded-[18px] grid md:grid-cols-2 m-2">
        <!-- Word -->
        <div
            class="flex flex-col items-center justify-center bg-slate-100 rounded-[18px] m-2 md:p-4 md:p-12"
        >
            <!-- Learning tag -->
            <div
                v-if="wordScore !== null && wordScore >= 7"
                class="rounded-full m-2 px-2"
                :class="{
                    'bg-yellow-300': wordScore == 10,
                    'bg-cyan-300': wordScore != 10,
                }"
            >
                {{ wordScore == 10 ? "Mastered" : "Almost mastered" }}
            </div>

            <div class="hidden md:inline">
                <ReactiveText>
                    <div
                        ref="word"
                        class="text-slate-900 text-center whitespace-nowrap"
                    >
                        {{ word.word }}
                    </div>
                </ReactiveText>
            </div>

            <div class="md:hidden">
                <ReactiveText initialSize="4rem">
                    <div
                        ref="word"
                        class="text-slate-900 text-center whitespace-nowrap"
                    >
                        {{ word.word }}
                    </div>
                </ReactiveText>
            </div>

            <div
                class="flex text-2xl md:text-4xl text-slate-400 text-center px-4 pb-2 md:py-2"
                v-show="!hideTranslations"
            >
                {{ word.translation }}
            </div>

            <div v-if="debugMode">
                <code>
                    wordScore: {{ wordScore }} <br />
                    tags: {{ word.tags }} <br />
                </code>
            </div>
        </div>

        <div
            class="flex md:flex-col p-4 overflow-x-scroll snap-x snap-mandatory gap-4 mb-1 mx-1"
        >
            <!-- Example -->
            <div
                class="flex flex-1 basis-full snap-center md:basis-auto shrink-0 grow-0 md:grow flex-grow flex-col justify-around md:justify-start md:text-2xl"
            >
                <div class="flex justify-left items-center md:h-auto">
                    <div class="text-4xl pr-4">
                        {{ word.emoji }}
                    </div>
                    <div class="flex flex-col justify-center gap-2">
                        <div class="flex gap-2 align-middle">
                            <p>"{{ word.example }}"</p>
                        </div>
                        <p class="text-slate-500" v-show="!hideTranslations">
                            "{{ word.example_en }}"
                        </p>
                    </div>
                </div>

                <!-- Difficulty Range -->
                <DifficultyRange class="md:hidden" :value="word.difficulty" />
            </div>

            <!-- Second page on mobile -->
            <div
                class="flex basis-full snap-center md:basis-auto shrink-0 grow-0 flex-col justify-around"
            >
                <div
                    class="flex justify-between overflow-x-auto whitespace-nowrap"
                >
                    <!-- Part of speech -->
                    <div
                        v-if="word.part_of_speech"
                        class="pb-2 overflow-x-auto whitespace-nowrap"
                    >
                        <div class="px-2 text-sm text-slate-900">
                            Part of Speech
                        </div>
                        <div class="flex text-slate-500 text-l">
                            <div class="bg-slate-300 rounded-full m-2 px-2">
                                {{ word.part_of_speech }}
                            </div>
                        </div>
                    </div>

                    <!-- Gender -->
                    <div
                        v-if="word.gender"
                        class="pb-2 overflow-x-auto whitespace-nowrap"
                    >
                        <div class="px-2 text-sm text-slate-900">Gender</div>
                        <div class="flex text-slate-500 text-l">
                            <div class="bg-slate-300 rounded-full m-2 px-2">
                                {{ word.gender }}
                            </div>
                        </div>
                    </div>

                    <!-- Plural -->
                    <div
                        v-if="word.plural"
                        class="pb-2 overflow-x-auto whitespace-nowrap"
                    >
                        <div class="px-2 text-sm text-slate-900">Plural</div>
                        <div class="flex text-slate-500 text-l">
                            <div class="bg-slate-300 rounded-full m-2 px-2">
                                {{ word.plural }}
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Synonyms and Antonyms -->
                <div
                    v-if="word.synonyms.length > 0 || word.antonyms.length > 0"
                >
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

                <!-- Difficulty Range -->
                <DifficultyRange
                    class="hidden md:inline"
                    :value="word.difficulty"
                />
            </div>
        </div>
    </div>
</template>

<script>
import DifficultyRange from "@/components/DifficultyRange.vue";
import ReactiveText from "@/components/ReactiveText.vue";

export default {
    name: "Card",
    components: {
        DifficultyRange,
        ReactiveText,
    },
    inject: ["debugMode"],
    props: {
        word: {
            type: Object,
            required: true,
        },
        wordScore: {
            type: Number,
            default: null,
        },
        hideTranslations: {
            type: Boolean,
            default: false,
        },
    },
};
</script>
