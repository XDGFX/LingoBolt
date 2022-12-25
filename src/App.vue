<template>
    <div
        id="app"
        class="flex flex-col items-center bg-white h-screen bg-slate-100 text-slate-900 px-4 py-8"
    >
        <!-- Heading -->
        <h1 class="text-4xl pt-8 pb-12">
            <span class="text-slate-500">When learning a new language, </span>
            <span class="text-slate-900 underline decoration-pink-500"
                >the first 1000</span
            >
            <span class="text-slate-500"> words are the most important.</span>
        </h1>

        <!-- Search box -->
        <div class="flex flex-row items-center justify-center">
            <input
                v-model="search"
                class="w-96 h-12 rounded-[24px] border-2 border-slate-200 p-4 text-2xl"
                type="text"
                placeholder="Search for a word"
            />
        </div>

        <carousel :words="words"></carousel>
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
