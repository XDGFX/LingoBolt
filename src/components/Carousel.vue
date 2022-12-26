<template>
    <div
        class="m-4 h-full w-full lg:w-[990px] overflow-auto rounded-[24px] bg-white border-2 border-slate-200"
    >
        <!-- <TransitionGroup appear name="slide-fade">
            <card v-for="word in words" :key="word.word" :word="word"></card>
        </TransitionGroup> -->
        <div
            v-if="words.length === 0"
            class="text-4xl p-4 h-full flex justify-center items-center"
        >
            <p class="pb-4">No results found :(</p>
        </div>

        <RecycleScroller
            v-else
            class="h-full w-full"
            :items="words"
            :item-size="384 + 8"
            :key-field="'word'"
        >
            <template #default="{ item }">
                <card :word="item" :showTTS="showTTS"></card>
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
    props: {
        words: {
            type: Array,
            required: true,
        },
    },
    computed: {
        word() {
            // Return a random word from the words array
            return this.words[Math.floor(Math.random() * this.words.length)];
        },
    },
};
</script>

<style scoped>
.slide-fade-enter-active,
.slide-fade-leave-active {
    transition: all 0.5s cubic-bezier(0, 1, 0, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
    scale: 0.8;
    opacity: 0;
}
</style>
