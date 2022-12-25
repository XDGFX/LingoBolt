<template>
    <div class="bg-slate-300 rounded-full m-2 p-2">
        <div class="relative rounded-full">
            <div
                class="block w-full rounded-md leading-5 text-slate-500 focus:outline-none focus:shadow-outline-blue-300 transition duration-150 ease-in-out"
            >
                <div
                    class="h-4 bg-slate-200 rounded-full"
                    :class="
                        value === 1
                            ? 'bg-emerald-500'
                            : value === 2
                            ? 'bg-cyan-500'
                            : value === 3
                            ? 'bg-violet-500'
                            : 'bg-rose-500'
                    "
                    :style="{
                        width: `${(value / 4) * 100}%`,
                    }"
                ></div>
            </div>
            <div
                class="absolute top-0 left-0 -mt-0.5 ml-3 text-xs font-medium leading-5 text-white"
            >
                Easy
            </div>
            <div
                class="absolute top-0 right-0 -mt-0.5 mr-3 text-xs font-medium leading-5"
                :class="value === 4 ? 'text-white' : 'text-slate-500'"
            >
                Hard
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "DifficultyRange",
    props: {
        value: {
            type: Number,
            default: 1,
        },
    },
};
</script>
