<template>
    <div class="fixed inset-0 overflow-y-auto bg-slate-200 z-40">
        <div
            class="flex flex-col items-center text-center justify-center text-slate-800 h-full"
        >
            <div class="m-2 md:m-8">
                <h1 class="text-4xl pb-4">
                    <span class="text-slate-500"
                        >Which language do you want to learn?</span
                    >
                </h1>
            </div>

            <div class="mx-4 md:mx-32 flex gap-4 justify-center">
                <button
                    v-for="language in languages"
                    :key="language"
                    class="w-24 h-24 fib fis rounded-[18px] border-2 border-slate-300 transition hover:scale-110"
                    :class="`fi-${language}`"
                    @click="$emit('set-language', language)"
                ></button>
            </div>

            <div class="m-2 md:m-8">
                <h2 class="pb-12 text-slate-500">
                    Language not listed?
                    <a
                        class="text-slate-900 underline decoration-rose-500"
                        href="https://github.com/XDGFX/the-first-1000/issues/new?title=Add%20language%20%5Blanguage%20name%5D"
                        target="_blank"
                    >
                        Suggest one here!</a
                    >
                </h2>
            </div>
        </div>
    </div>
</template>

<script>
import "@/../node_modules/flag-icons/css/flag-icons.min.css";

export default {
    name: "LanguageSelectPage",
    emits: ["set-language"],
    data() {
        return {
            languages: ["fr", "es"],
        };
    },
};
</script>

<style></style>
