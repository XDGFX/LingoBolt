<template>
    <div
        class="h-[384px] bg-slate-200 rounded-[18px] flex flex-col md:flex-row m-2"
    >
        <!-- Word -->
        <div
            class="flex flex-col basis-1/2 shrink-0 grow-0 overflow-x-hidden items-center justify-center bg-slate-100 rounded-[18px] m-2 p-4 md:p-12"
        >
            <!-- Learning tag -->
            <div
                v-if="wordScore !== null && wordScore >= 7"
                class="rounded-full px-2"
                :class="{
                    'bg-yellow-300': wordScore == 10,
                    'bg-cyan-300': wordScore != 10,
                }"
            >
                {{ wordScore == 10 ? "Mastered" : "Almost mastered" }}
            </div>

            <ReactiveText>
                <div
                    ref="word"
                    class="text-slate-900 whitespace-nowrap leading-none"
                >
                    {{ word.word }}
                </div>
            </ReactiveText>

            <div
                class="flex text-2xl md:text-4xl text-slate-400 text-center"
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

        <!-- Info -->
        <div
            class="flex md:flex-col basis-1/2 p-4 overflow-x-scroll snap-x snap-mandatory gap-4 m-1"
        >
            <!-- Example -->
            <div
                class="flex flex-1 basis-full snap-center md:basis-auto shrink-0 grow-0 md:grow flex-col md:justify-start md:text-xl lg:text-2xl"
            >
                <div class="flex flex-1 justify-left items-center md:h-auto">
                    <div class="w-min text-4xl pr-4">
                        <!-- <Twemoji> -->
                        {{ word.emoji }}
                        <!-- </Twemoji> -->
                    </div>
                    <div class="flex flex-col justify-center gap-2">
                        <div class="overflow-auto">
                            {{ word.example }}
                        </div>
                        <p
                            class="text-slate-500 overflow-auto"
                            v-show="!hideTranslations"
                        >
                            {{ word.example_en }}
                        </p>
                    </div>
                </div>

                <!-- Difficulty Range -->
                <div class="flex-1 md:hidden">
                    <DifficultyRange :value="word.difficulty" />
                </div>
            </div>

            <!-- Second page on mobile -->
            <div
                class="flex basis-full w-full snap-center md:basis-auto shrink-0 grow-0 flex-col justify-around"
            >
                <div
                    class="flex justify-between overflow-x-auto whitespace-nowrap"
                >
                    <!-- Part of speech -->
                    <div
                        v-if="word.part_of_speech"
                        class="pb-2 whitespace-nowrap"
                    >
                        <div class="px-2 text-sm text-slate-900">
                            Part of Speech
                        </div>
                        <div class="flex text-slate-500">
                            <div class="bg-slate-300 rounded-full m-2 px-2">
                                {{ word.part_of_speech }}
                            </div>
                        </div>
                    </div>

                    <!-- Gender -->
                    <div v-if="word.gender" class="pb-2 whitespace-nowrap">
                        <div class="px-2 text-sm text-slate-900">Gender</div>
                        <div class="flex text-slate-500">
                            <div class="bg-slate-300 rounded-full m-2 px-2">
                                {{ word.gender }}
                            </div>
                        </div>
                    </div>

                    <!-- Plural -->
                    <div v-if="word.plural" class="pb-2 whitespace-nowrap">
                        <div class="px-2 text-sm text-slate-900">Plural</div>
                        <div class="flex text-slate-500">
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
                        <div class="flex flex-1 text-slate-900 pr-4">
                            <div
                                v-for="synonym in word.synonyms"
                                :key="synonym"
                                class="bg-emerald-300 rounded-full m-2 px-2"
                            >
                                {{ synonym }}
                            </div>
                        </div>

                        <div class="flex text-slate-900 justify-self-end">
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
import Twemoji from "@/components/Twemoji.vue";

export default {
    name: "Card",
    components: {
        DifficultyRange,
        ReactiveText,
        Twemoji,
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
