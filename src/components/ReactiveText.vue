<template>
    <div ref="parent" class="w-full"></div>
    <span
        ref="text"
        :style="{ transform: `scale(${scale})`, fontSize: initialSize }"
    >
        <slot></slot>
    </span>
</template>

<script>
export default {
    name: "ReactiveText",
    props: {
        // The initial font size
        initialSize: {
            type: String,
            default: "6rem",
        },
        maxScale: {
            type: Number,
            default: 1,
        },
        minScale: {
            type: Number,
            default: 0,
        },

        // Used to force an update
        state: {
            type: String,
            default: "",
        },
    },
    data() {
        return {
            scale: 1,
            obverver: null,
        };
    },
    mounted() {
        // Add a listener which resizes the text whenever the window is resized,
        // or when the card is visible on the screen
        window.addEventListener("resize", this.updateReactiveText);

        // Add a window observer to resize the text when ref="text" is visible
        this.observer = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    this.updateReactiveText();
                }
            });
        });

        this.observer.observe(this.$refs.text);

        // Initial resize
        this.updateReactiveText();
    },
    beforeUnmount() {
        // Remove resize listener
        window.removeEventListener("resize", this.updateReactiveText);

        // Remove window observer
        this.observer.unobserve(this.$refs.text);
    },
    watch: {
        state() {
            console.log("state changed");

            this.updateReactiveText();
        },
    },
    methods: {
        updateReactiveText() {
            // Add callback to wait for the element to be rendered
            this.$nextTick(() => {
                // Get the width of the parent element
                const cardWidth = this.$refs.parent.offsetWidth;

                // Get the width of the text element
                const textWidth = this.$refs.text.offsetWidth;

                // Scale down the text so it's the same width as the parent element
                this.scale = Math.max(
                    this.minScale,
                    Math.min(this.maxScale, cardWidth / textWidth)
                );
            });
        },
    },
};
</script>

<style scoped></style>
