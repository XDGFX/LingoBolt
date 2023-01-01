<template>
    <div class="w-48 h-48 md:w-64 md:h-64 pointer-events-none select-none">
        <img
            class="absolute w-48 h-48 md:w-64 md:h-64 floating delayed z-10"
            src="@/assets/pluie/bobble.svg"
        />
        <div class="absolute w-48 h-48 md:w-64 md:h-64 floating">
            <img
                ref="base"
                class="absolute z-10"
                src="@/assets/pluie/base.svg"
                alt="Pluie mascot"
            />
            <img class="absolute z-30" :src="`${baseUrl}face_${mood}.svg`" />
            <img
                v-show="accessory !== ''"
                class="absolute z-40"
                :src="`${baseUrl}accessory_${accessory}.svg`"
            />
            <img
                v-show="speaking"
                class="absolute z-10"
                src="@/assets/pluie/speech.svg"
            />
        </div>
    </div>
</template>

<script>
export default {
    name: "PluieMascot",
    props: {
        mood: {
            type: String,
            default: "smile",
            validator: (value) =>
                ["smile", "grin", "interest", "content"].includes(value),
        },
        accessory: {
            type: String,
            default: "",
            validator: (value) => ["", "hat", "glasses"].includes(value),
        },
        speaking: {
            type: Boolean,
            default: false,
        },
    },
    data() {
        return {
            baseUrl: "",
        };
    },
    mounted() {
        // Split by "/" and remove last element ("base.svg") to get base URL
        this.baseUrl =
            this.$refs.base
                .getAttribute("src")
                .split("/")
                .slice(0, -1)
                .join("/") + "/";
    },
};
</script>

<style scoped>
/* Animation slow float up and down on loop */
@keyframes float {
    0% {
        transform: translateY(0);
    }
    50% {
        transform: translateY(-10px);
    }
    100% {
        transform: translateY(0);
    }
}

.floating {
    animation: float 4s ease-in-out infinite;
}

.floating.delayed {
    animation-delay: 0.5s;
}
</style>
