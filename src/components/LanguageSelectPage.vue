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
            <div
                class="mx-4 md:mx-32 gap-8 justify-center hidden md:flex flex-wrap"
            >
                <div v-for="language in languages" :key="language">
                    <button
                        class="w-24 h-24 fib fis rounded-[18px] transition hover:scale-110 relative"
                        :class="`fi-${flagOverrides[language] || language}`"
                        @click="$emit('set-language', language)"
                        @mouseover="selectedLanguage = language"
                        @mouseleave="selectedLanguage = null"
                    >
                        <!-- New icon -->
                        <span
                            v-if="newLanguages.includes(language)"
                            class="absolute top-0 text-slate-900 font-bold bg-yellow-500 rounded-full px-2 py-1 text-xs translate-x-1/2 -translate-y-1/2"
                        >
                            NEW
                        </span>
                    </button>

                    <!-- Anglisised name -->
                    <div
                        class="text-center text-slate-900 transition pt-4"
                        :class="{
                            'text-slate-500': selectedLanguage !== language,
                        }"
                    >
                        {{
                            new Intl.DisplayNames(["en"], {
                                type: "language",
                            }).of(language)
                        }}
                    </div>
                </div>
            </div>

            <!-- Mobile side scrolling list of languages, snap to each to select
            -->
            <div
                ref="languageSelectIcons"
                class="md:hidden w-full py-4 flex overflow-x-auto snap-x snap-mandatory scrollbar-hide"
                @scroll="checkSelectedLanguage()"
            >
                <div
                    v-for="language in languages"
                    :language="language"
                    :key="language"
                    class="relative language-select-icon w-24 h-24 mx-8 first:ml-[100vw] last:mr-[100vw] shrink-0 snap-center snap-always fib fis rounded-[18px]"
                    :class="`fi-${flagOverrides[language] || language}`"
                >
                    <!-- New icon -->
                    <span
                        v-if="newLanguages.includes(language)"
                        class="absolute top-0 text-slate-900 font-bold bg-yellow-500 rounded-full px-2 py-1 text-xs translate-x-1/2 -translate-y-1/2"
                    >
                        NEW
                    </span>
                </div>
            </div>

            <div class="md:hidden flex items-center justify-center">
                {{
                    selectedLanguage == null
                        ? ""
                        : new Intl.DisplayNames(["en"], {
                              type: "language",
                          }).of(selectedLanguage)
                }}
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
                        href="https://github.com/XDGFX/LingoBolt/issues/new?title=Add%20language%20%5Blanguage%20name%5D"
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
    inject: ["languages", "newLanguages", "flagOverrides"],
    components: {
        PluieMascot,
    },
    data() {
        return {
            // Only used on mobile
            selectedLanguage: null,
        };
    },
    provide() {
        return {
            debugMode: this.debugMode,
        };
    },
    methods: {
        // Only used on mobile
        checkSelectedLanguage() {
            const div = this.$refs.languageSelectIcons;
            const icons = div.querySelectorAll(".language-select-icon");

            // Check which icon the scroll snap is currently on (which one has
            // the midle of the screen closest to it)
            for (let i = 0; i < icons.length; i++) {
                const icon = icons[i];
                const rect = icon.getBoundingClientRect();

                if (rect.left < window.innerWidth / 2) {
                    this.selectedLanguage = icon.getAttribute("language");
                }
            }
        },
    },
    computed: {
        selectedLanguageText() {
            if (!this.selectedLanguage) {
                return "...";
            }

            return {
                fr: "C'est parti!",
                es: "¡Vamos!",
                it: "Andiamo!",
                de: "Los geht's!",
                pt: "Vamos!",
                nl: "Laten we gaan!",
                lb: "A lass!",
                cs: "Pojďme!",
                no: "La oss gå!",
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
