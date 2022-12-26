<template>
    <div
        id="app"
        class="flex flex-col items-center bg-white h-screen bg-slate-100 text-slate-900 px-4 py-8 selection:bg-rose-500 selection:text-white"
    >
        <!-- Heading desktop -->
        <div class="collapse md:visible text-center">
            <h1 class="text-4xl pt-8 pb-4">
                <span class="text-slate-500">
                    When learning a new language,
                </span>
                <span class="text-slate-900 underline decoration-rose-500">
                    the first 1000
                </span>
                <span class="text-slate-500">
                    words are the most important.
                </span>
            </h1>

            <!-- Subtitle -->
            <h2 class="text-2xl pb-12">
                <span class="text-slate-400">
                    Here you can learn your first 1000 words in French 🇫🇷.
                </span>
            </h2>
        </div>

        <!-- Heading mobile -->
        <div class="visible md:collapse">
            <h1 class="text-4xl pb-4">
                <span class="text-slate-900 underline decoration-rose-500">
                    the first 1000
                </span>
            </h1>
        </div>

        <div class="flex">
            <!-- Search box -->
            <input
                v-model="search"
                class="h-8 md:h-12 w-full md:w-96 rounded-full border-2 border-slate-200 p-4 text-xl md:text-2xl focus:border-rose-500 outline-none"
                type="text"
                placeholder="Search for a word"
            />

            <!-- Hide translations -->
            <div class="flex items-center mx-4">
                <input
                    v-model="hideTranslations"
                    class="h-6 w-6 mr-2 rounded-full"
                    type="checkbox"
                />
                <span class="text-sm">Hide translations</span>
            </div>
        </div>

        <carousel
            :words="words"
            :hide-translations="hideTranslations"
        ></carousel>
    </div>
</template>

<script>
import Fuse from "fuse.js";

import words from "@/french.json";
import Carousel from "@/components/Carousel.vue";

export default {
    name: "App",
    components: {
        Carousel,
    },
    data() {
        return {
            search: "",
            hideTranslations: false,
        };
    },
    computed: {
        words() {
            // If the search box is empty, return all words
            if (this.search === "") {
                return words;
            }

            // Otherwise, return the words that match the search query
            const fuse = new Fuse(words, {
                keys: [
                    { name: "word", weight: 4 },
                    { name: "translation", weight: 4 },
                    "example",
                    "example_en",
                    { name: "tags", weight: 2 },
                    { name: "synonyms", weight: 3 },
                ],
                shouldSort: true,
            });
            const results = fuse.search(
                this.search.replace(/\s+/g, " ").toLowerCase()
            );

            return results.map((result) => result.item);
        },
    },
};
</script>

<style>
/* Add your CSS here */
</style>
