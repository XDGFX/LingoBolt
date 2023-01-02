<template>
    <div
        class="md:my-4 h-full w-full lg:w-[990px] overflow-auto overscroll-contain md:rounded-[24px] bg-white md:border-2 border-slate-200"
    >
        <div
            v-if="words.length === 0"
            class="text-4xl p-4 h-full flex justify-center items-center"
        >
            <p class="pb-4">No results found :(</p>
        </div>

        <!-- Consider adding `scrollbar-hide` class -->
        <RecycleScroller
            v-show="words.length > 0"
            ref="scroller"
            class="h-full w-full"
            :items="words"
            :item-size="384 + 8"
            :key-field="'word'"
            :buffer="1000"
        >
            <template #default="{ item }">
                <card
                    :word="item"
                    :wordScore="wordScores[item.word]"
                    :showTTS="showTTS"
                    :hideTranslations="hideTranslations"
                ></card>
            </template>
        </RecycleScroller>
    </div>
</template>

<script>
import { RecycleScroller } from "vue-virtual-scroller";
import "vue-virtual-scroller/dist/vue-virtual-scroller.css";

import Card from "@/components/Card.vue";

export default {
    name: "Carousel",
    components: { Card, RecycleScroller },
    data() {
        return {
            showTTS: false,
        };
    },
    props: {
        words: {
            type: Array,
            required: true,
        },
        wordScores: {
            type: Object,
            required: true,
        },
        hideTranslations: {
            type: Boolean,
            default: false,
        },
    },
    computed: {
        word() {
            // Return a random word from the words array
            return this.words[Math.floor(Math.random() * this.words.length)];
        },
    },
    async mounted() {
        let voices = speechSynthesis.getVoices();

        if (voices.length === 0) {
            await new Promise((resolve) => {
                speechSynthesis.onvoiceschanged = resolve;
            });

            voices = speechSynthesis.getVoices();
        }

        // TODO: Update this to work for each language
        // // Find a voice that speaks French (fr-FR or fr_FR)
        // this.showTTS = voices.find((voice) => {
        //     return voice.lang === "fr-FR" || voice.lang === "fr_FR";
        // })
        //     ? true
        //     : false;
        this.showTTS = false;
    },
    watch: {
        words() {
            // If the words array changes, reset the scroll position
            this.$refs.scroller.scrollToItem(0);
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
