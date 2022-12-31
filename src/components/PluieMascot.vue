<template>
    <div class="w-48 h-48 md:w-64 md:h-64 pointer-events-none select-none">
        <img
            class="absolute w-48 h-48 md:w-64 md:h-64 floating delayed"
            src="@/assets/pluie/bobble.svg"
        />
        <img
            class="absolute w-48 h-48 md:w-64 md:h-64 floating"
            src="@/assets/pluie/default.svg"
            alt="Pluie mascot"
        />
    </div>
</template>

<script>
export default {
    name: "PluieMascot",
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
