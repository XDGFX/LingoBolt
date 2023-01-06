<template>
    <!-- Div that covers the whole screen -->
    <div
        v-if="show"
        class="fixed flex inset-0 overflow-y-auto bg-slate-200 z-50 justify-center"
    >
        <div
            class="flex flex-col items-center justify-center text-slate-800 h-full"
        >
            <!-- Page 0 -->
            <div
                v-show="page == 0"
                class="text-center flex flex-col items-center m-4 md:m-8"
            >
                <PluieMascot></PluieMascot>

                <!-- Title -->
                <h1 class="text-2xl md:text-4xl pt-8 pb-4">
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
                <h2 class="text-xl md:text-2xl pb-12">
                    I'm here to help you learn your first 1000 words of a new
                    language.
                </h2>

                <button
                    class="flex items-center justify-center h-12 w-48 rounded-full border-2 border-slate-300 p-4 m-8 text-xl md:text-2xl bg-white hover:bg-slate-100 outline-none"
                    @click="page = 1"
                >
                    Next
                </button>
            </div>

            <!-- Page 1 -->
            <div
                v-show="page == 1"
                class="m-8 md:mx-32 gap-2 flex flex-col text-center"
            >
                <h2 class="text-4xl pt-8 pb-4 text-slate-500">
                    Here are some tips:
                </h2>
                <ul class="text-xl md:text-2xl gap-4 flex flex-col">
                    <li>Revise 📖 new words on the following screen.</li>
                    <li>
                        When you are ready, go to the Practice 🎓 page to test
                        your knowledge!
                    </li>
                    <li>
                        With a strong focus on vocabulary&nbsp📚, I work best
                        alongside other learning tools.
                    </li>
                </ul>

                <h2 class="text-2xl pt-8 pb-4 text-slate-500">Disclaimer:</h2>
                <p class="text-s gap-4 flex flex-col lg:w-[990px]">
                    While I strive to provide accurate and reliable
                    translations, please keep in mind that language is
                    constantly evolving and that my translations may not always
                    reflect the most current usage. Use this site as a guide to
                    help you understand new words and phrases, but be open to
                    learning and growing as you continue your language learning
                    journey!
                </p>

                <button
                    class="flex self-center items-center justify-center h-12 w-48 rounded-full border-2 border-slate-300 p-4 m-8 text-xl md:text-2xl bg-white hover:bg-slate-100 outline-none"
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
