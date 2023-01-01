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

            <!-- Face -->
            <img
                v-if="mood === 'smile'"
                class="absolute z-30"
                src="@/assets/pluie/face_smile.svg"
            />
            <img
                v-else-if="mood === 'grin'"
                class="absolute z-30"
                src="@/assets/pluie/face_grin.svg"
            />
            <img
                v-else-if="mood === 'interest'"
                class="absolute z-30"
                src="@/assets/pluie/face_interest.svg"
            />
            <img
                v-else-if="mood === 'content'"
                class="absolute z-30"
                src="@/assets/pluie/face_content.svg"
            />

            <!-- Accessories -->
            <img
                v-if="accessory === 'hat'"
                class="absolute z-40"
                src="@/assets/pluie/accessory_hat.svg"
            />
            <img
                v-else-if="accessory === 'glasses'"
                class="absolute z-40"
                src="@/assets/pluie/accessory_glasses.svg"
            />

            <img
                v-if="speaking"
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
