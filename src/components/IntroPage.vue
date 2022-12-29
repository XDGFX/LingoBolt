<template>
    <!-- Div that covers the whole screen -->
    <div v-if="show" class="fixed inset-0 overflow-y-auto bg-slate-200 z-50">
        <div
            class="flex flex-col items-center justify-center text-slate-800 h-full"
        >
            <div class="text-center m-2 md:m-8">
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
                    <span class="">
                        Here you can learn your first 1000 words of a new
                        language.
                    </span>
                </h2>
            </div>

            <div class="mx-4 md:mx-32 text-xl text-center gap-2 flex flex-col">
                <div>Revise 📖 new words on the following screen.</div>
                <div>
                    When you are ready, go to the Practice 🎓 page to test your
                    knowledge!
                </div>
                <div>
                    With a strong focus on vocabulary 📚, I work best alongside
                    other learning tools.
                </div>
            </div>
            <button
                class="flex self-center items-center justify-center h-8 md:h-12 w-48 rounded-full border-2 border-slate-300 p-4 m-8 text-xl md:text-2xl bg-white hover:bg-slate-200 outline-none"
                @click="show = false"
            >
                Ready?
            </button>
        </div>
    </div>
</template>

<script>
export default {
    name: "IntroPage",
    data() {
        return {
            show: true,
        };
    },
};
</script>

<style></style>
