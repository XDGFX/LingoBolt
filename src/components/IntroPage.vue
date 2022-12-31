<template>
    <!-- Div that covers the whole screen -->
    <div v-if="show" class="fixed inset-0 overflow-y-auto bg-slate-200 z-50">
        <div
            class="flex flex-col items-center justify-center text-slate-800 h-full"
        >
            <!-- Page 0 -->
            <div
                v-show="page == 0"
                class="text-center flex flex-col items-center m-2 md:m-8"
            >
                <PluieMascot></PluieMascot>

                <!-- Title -->
                <h1 class="text-4xl pt-8 pb-4">
                    <span class="text-slate-500">
                        When learning a new language,
                    </span>
                    <span class="text-slate-900 underline decoration-rose-500"
                        >the first 1000</span
                    >
                    <span class="text-slate-500">
                        words are the most important.
                    </span>
                </h1>

                <!-- Subtitle -->
                <h2 class="text-2xl pb-12">
                    I'm here to help you learn your first 1000 words of a new
                    language.
                </h2>

                <button
                    class="flex items-center justify-center h-8 md:h-12 w-48 rounded-full border-2 border-slate-300 p-4 m-8 text-xl md:text-2xl bg-white hover:bg-slate-200 outline-none"
                    @click="page = 1"
                >
                    Next
                </button>
            </div>

            <!-- Page 1 -->
            <div
                v-show="page == 1"
                class="mx-4 md:mx-32 text-xl gap-2 flex flex-col"
            >
                <h2 class="text-4xl pt-8 pb-4 text-slate-500 text-center">
                    Here are some tips:
                </h2>
                <ul class="list-disc">
                    <li>Revise 📖 new words on the following screen.</li>
                    <li>
                        When you are ready, go to the Practice 🎓 page to test
                        your knowledge!
                    </li>
                    <li>
                        With a strong focus on vocabulary 📚, I work best
                        alongside other learning tools.
                    </li>
                </ul>
                <button
                    class="flex self-center items-center justify-center h-8 md:h-12 w-48 rounded-full border-2 border-slate-300 p-4 m-8 text-xl md:text-2xl bg-white hover:bg-slate-200 outline-none"
                    @click="show = false"
                >
                    Let's go!
                </button>
            </div>
        </div>
    </div>
</template>

<script>
import PluieMascot from "@/components/PluieMascot.vue";

export default {
    name: "IntroPage",
    components: {
        PluieMascot,
    },
    data() {
        return {
            show: true,
            page: 0,
        };
    },
};
</script>

<style></style>
