<template>
    <div
        class="h-96 bg-slate-200 rounded-[18px] grid grid-cols-4 grid-rows-2 m-2"
    >
        <!-- Word -->
        <div
            class="row-span-2 col-span-2 flex flex-col items-center justify-center bg-slate-100 rounded-[18px] m-2"
        >
            <div class="text-slate-900 whitespace-nowrap text-8xl">
                {{ word.word }}
            </div>
            <div class="text-4xl text-slate-400">
                {{ word.translation }}
            </div>
            <AudioPlayer :word="word.word"></AudioPlayer>
        </div>

        <!-- Example -->
        <div class="col-span-2 flex flex-col justify-center text-2xl p-4">
            <div class="flex justify-left items-center">
                <div class="text-4xl pr-4">
                    {{ word.emoji }}
                </div>
                <div class="col-span-2 flex flex-col justify-center text-2xl">
                    <AudioPlayer :word="word.example"></AudioPlayer>
                    <p class="pb-2">"{{ word.example }}"</p>
                    <p class="text-slate-500">"{{ word.example_en }}"</p>
                </div>
            </div>
        </div>

        <!-- Tags, difficulty -->
        <div class="col-span-2 grid p-4 content-end">
            <div class="pb-2">
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
                <div class="flex">
                    <div class="flex flex-1 text-slate-900 text-l">
                        <div
                            v-for="synonym in word.synonyms"
                            :key="synonym"
                            class="bg-emerald-300 rounded-full m-2 px-2"
                        >
                            {{ synonym }}
                        </div>
                    </div>

                    <div class="flex text-slate-900 text-l justify-self-end">
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
    },
};
</script>

<style scoped></style>
