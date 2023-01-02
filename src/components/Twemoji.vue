<template>
    <div ref="twemoji">
        <slot></slot>
    </div>
</template>

<script>
import twemoji from "twemoji";

export default {
    name: "Twemoji",
    mounted() {
        this.updateTwemoji();
    },
    watch: {
        emoji() {
            this.updateTwemoji();
        },
    },
    methods: {
        updateTwemoji() {
            // Convert all emojis to images
            twemoji.parse(this.$refs.twemoji, {
                ext: ".svg",
            });
        },
    },
};
</script>

<style></style>
