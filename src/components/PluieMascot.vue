<template>
    <div
        class="flex items-center justify-center"
        :class="{
            'flex-wrap-reverse w-min': speechPosition === 'top',
            'flex-nowrap': speechPosition === 'right',
        }"
    >
        <div
            class="relative shrink-0 pointer-events-none select-none"
            :class="sizeClass"
        >
            <img
                class="absolute floating delayed z-10"
                :class="sizeClass"
                src="@/assets/pluie/bobble.svg"
            />
            <div class="absolute floating" :class="sizeClass">
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
            </div>
        </div>
        <div
            v-if="speech"
            class="relative text-center m-4 p-2 max-w-[12em] min-w-[4em] rounded-[24px] bg-white border-2 border-slate-300"
        >
            <p>{{ speech }}</p>
            <div
                v-if="speechPosition === 'top'"
                class="absolute left-1/2 bottom-0 translate-y-[7.5px] -translate-x-1/2 -rotate-45 h-3 w-3 rounded-bl bg-white border-l-2 border-b-2 border-slate-300"
            ></div>
            <div
                v-if="speechPosition === 'right'"
                class="absolute bottom-1/2 left-0 -translate-x-[6.5px] translate-y-1/2 rotate-45 h-3 w-3 rounded-bl bg-white border-l-2 border-b-2 border-slate-300"
            ></div>
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
        speech: {
            type: String,
            default: "",
        },
        speechPosition: {
            type: String,
            default: "right",
            validator: (value) => ["right", "top"].includes(value),
        },
        size: {
            type: String,
            default: "lg",
            validator: (value) => ["sm", "md", "lg"].includes(value),
        },
    },
    computed: {
        sizeClass() {
            // If size is lg, return "w-48 h-48 md:w-64 md:h-64"
            // If size is md, return "w-32 h-32 md:w-48 md:h-48"
            // If size is sm, return "w-24 h-24 md:w-32 md:h-32"
            return `w-${
                this.size === "lg" ? 48 : this.size === "md" ? 32 : 24
            } h-${
                this.size === "lg" ? 48 : this.size === "md" ? 32 : 24
            } md:w-${
                this.size === "lg" ? 64 : this.size === "md" ? 48 : 32
            } md:h-${this.size === "lg" ? 64 : this.size === "md" ? 48 : 32}`;
        },
    },
};
</script>

<style scoped>
/* Animation slow float up and down on loop */
@keyframes float {
    0% {
        transform: translateY(5px);
    }
    50% {
        transform: translateY(-5px);
    }
    100% {
        transform: translateY(5px);
    }
}

.floating {
    animation: float 4s ease-in-out infinite;
}

.floating.delayed {
    animation-delay: 0.5s;
}
</style>
