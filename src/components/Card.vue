<template>
    <div
        class="h-96 bg-slate-200 rounded-[18px] grid grid-cols-4 grid-rows-2 m-4"
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
        </div>

        <!-- Example -->
        <div class="col-span-2 flex flex-col justify-center text-2xl p-4">
            <div class="flex justify-left items-center">
                <div class="text-4xl pr-4">
                    {{ word.emoji }}
                </div>
                <div class="col-span-2 flex flex-col justify-center text-2xl">
                    <p class="pb-2">"{{ word.example }}"</p>
                    <p class="text-slate-500">"{{ word.example_en }}"</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "Card",
    props: {
        word: {
            type: Object,
            required: true,
        },
    },
};
</script>

<style scoped></style>
