<template>
    <div class="bg-slate-200 rounded-full m-2 p-2">
        <div class="relative rounded-full">
            <div
                class="flex w-full rounded-md leading-5 text-slate-500 focus:outline-none focus:shadow-outline-blue-300 transition duration-150 ease-in-out"
            >
                <div
                    class="h-4 bg-cyan-400 rounded-full transition-all"
                    :style="{
                        width: `${
                            ((elo + 1 - minMax.min) /
                                (minMax.max - minMax.min)) *
                            100
                        }%`,
                    }"
                ></div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "DifficultyRange",
    data() {
        // Calculate the levels
        const numLevels = 50;
        let levels = [];
        let current = 0;

        for (let i = 0; i < numLevels; i++) {
            levels.push(current);
            current += i;
        }

        levels = levels.map((level) => {
            return Math.round((level / levels[levels.length - 1]) * 2000);
        });

        return {
            levels,
        };
    },
    props: {
        elo: {
            type: Number,
            required: true,
        },
    },
    computed: {
        minMax() {
            // Find the min and max elo for the current level
            return {
                min: this.levels[this.currentLevel - 1],
                max: this.levels[this.currentLevel],
            };
        },
        currentLevel() {
            return this.levels.findIndex((level) => level > this.elo);
        },
    },
};
</script>