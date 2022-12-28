<template>
    <div>
        <div class="bg-slate-200 rounded-full my-2 p-2">
            <div class="relative rounded-full">
                <div
                    class="flex w-full rounded-md leading-5 text-slate-500 focus:outline-none focus:shadow-outline-blue-300 transition duration-150 ease-in-out"
                >
                    <div
                        class="h-4 rounded-full motion-safe:transition-all"
                        :class="{
                            'bg-yellow-500': score == 20000,
                            'bg-emerald-500': score < 20000,
                        }"
                        :style="{
                            width: `${
                                ((score + 0.5 - minMax.min) /
                                    (minMax.max - minMax.min)) *
                                100
                            }%`,
                        }"
                    ></div>
                </div>
            </div>
        </div>
        <div class="flex mx-2">
            <div class="flex-1 text-start text-slate-500">
                Level {{ currentLevel }}
            </div>
            <div class="flex-1 text-center text-slate-500">Elo: {{ elo }}</div>
            <div class="flex-1 text-end text-slate-500">
                Level {{ currentLevel + 1 }}
            </div>
        </div>
    </div>
</template>

<script>
import JSConfetti from "js-confetti";

export default {
    name: "DifficultyRange",
    data() {
        // Calculate the levels
        const numLevels = 51;
        const maxScore = 20000;
        let levels = [];
        let current = 0;

        for (let i = 0; i < numLevels; i++) {
            levels.push(current);
            current += i;
        }

        levels = levels.map((level) => {
            return Math.round((level / levels[levels.length - 1]) * maxScore);
        });

        // Remove any duplicate level 0s
        levels = levels.filter((level, index) => {
            return level !== 0 || index === 0;
        });

        return {
            levels,
            maxScore,
            confetti: new JSConfetti(),
        };
    },
    props: {
        elo: {
            type: Number,
            required: true,
        },
        score: {
            type: Number,
            required: true,
        },
    },
    computed: {
        minMax() {
            // Find the min and max score for the current level
            return {
                min: this.levels[this.currentLevel - 1],
                max: this.levels[this.currentLevel],
            };
        },
        currentLevel() {
            if (this.score >= this.maxScore) {
                return this.levels.length - 1;
            }

            return this.levels.findIndex((level) => level > this.score);
        },
    },
    watch: {
        currentLevel: {
            handler(newValue, oldValue) {
                const prefersReducedMotion = window.matchMedia(
                    "(prefers-reduced-motion: reduce)"
                );

                if (prefersReducedMotion.matches) {
                    return;
                } else if (newValue > oldValue) {
                    this.confetti.addConfetti();
                }
            },
            immediate: true,
        },
    },
};
</script>
