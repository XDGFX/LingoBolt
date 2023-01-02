<template>
    <div class="fixed inset-0 overflow-y-auto bg-slate-200 z-40">
        <div
            class="flex flex-col items-center text-center justify-center text-slate-800 h-full"
        >
            <div v-if="debugMode" class="text-left">
                <code>
                    selectedLanguage: {{ selectedLanguage }} <br />
                    selectedLanguageText:{{ selectedLanguageText }} <br />
                    languages: {{ languages }} <br />
                </code>
            </div>

            <PluieMascot
                mood="grin"
                :speech="selectedLanguageText"
                speechPosition="top"
            ></PluieMascot>

            <div class="m-2 md:m-8">
                <h1 class="text-4xl pb-4">
                    <span class="text-slate-500"
                        >Which language do you want to learn?</span
                    >
                </h1>
            </div>

            <!-- Desktop list of languages, click to select -->
            <div class="mx-4 md:mx-32 gap-8 justify-center hidden md:flex">
                <button
                    v-for="language in languages"
                    :key="language"
                    class="w-24 h-24 fib fis rounded-[18px] transition hover:scale-110"
                    :class="`fi-${language}`"
                    @click="$emit('set-language', language)"
                    @mouseover="selectedLanguage = language"
                    @mouseleave="selectedLanguage = null"
                ></button>
            </div>

            <!-- Mobile side scrolling list of languages, snap to each to select
            -->
            <div
                ref="languageSelectIcons"
                class="md:hidden w-full flex overflow-x-auto snap-x snap-mandatory my-4 scrollbar-hide"
                @scroll="checkSelectedLanguage()"
            >
                <div
                    v-for="language in languages"
                    :language="language"
                    :key="language"
                    class="language-select-icon w-24 h-24 mx-8 first:ml-[100vw] last:mr-[100vw] shrink-0 snap-center snap-always fib fis rounded-[18px]"
                    :class="`fi-${language}`"
                ></div>
            </div>

            <button
                :disabled="selectedLanguage == null"
                class="md:hidden flex items-center justify-center h-12 w-48 rounded-full border-2 border-slate-300 p-4 m-8 text-xl bg-white outline-none"
                @click="$emit('set-language', selectedLanguage)"
            >
                Select
            </button>

            <div class="hidden md:inline m-2 md:m-8">
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

import PluieMascot from "@/components/PluieMascot.vue";

export default {
    name: "LanguageSelectPage",
    inject: ["debugMode"],
    emits: ["set-language"],
    components: {
        PluieMascot,
    },
    data() {
        return {
            languages: ["fr", "es", "de"],

            // Only used on mobile
            selectedLanguage: null,
        };
    },
    methods: {
        // Only used on mobile
        checkSelectedLanguage() {
            const div = this.$refs.languageSelectIcons;
            const icons = div.querySelectorAll(".language-select-icon");

            // Check which icon the scroll snap is currently on
            for (let i = 0; i < icons.length; i++) {
                const icon = icons[i];
                const rect = icon.getBoundingClientRect();
                if (rect.x > 0 && rect.x < window.innerWidth) {
                    this.selectedLanguage = icon.getAttribute("language");
                    break;
                }
            }
        },
    },
    computed: {
        // Only used on mobile
        selectedLanguageText() {
            if (!this.selectedLanguage) {
                return "...";
            }

            return {
                fr: "C'est parti!",
                es: "¡Vamos!",
                de: "Los geht's!",
            }[this.selectedLanguage];
        },
    },
};
</script>

<style scoped>
/* For Webkit-based browsers (Chrome, Safari and Opera) */
.scrollbar-hide::-webkit-scrollbar {
    display: none;
}

/* For IE, Edge and Firefox */
.scrollbar-hide {
    -ms-overflow-style: none; /* IE and Edge */
    scrollbar-width: none; /* Firefox */
}
</style>
