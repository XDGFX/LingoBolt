<template>
    <div class="text-center flex flex-col items-center m-4 md:m-8">
        <div class="text-2xl md:text-4xl mb-12">Hi there!</div>
        <div class="text-2xl">Welcome to...</div>
        <img src="@/assets/logo.svg" class="h-24 mb-12" alt="LingoBolt logo" />

        <PluieMascot></PluieMascot>
        <!-- Subtitle -->
        <h2 class="text-xl md:text-2xl pb-12">
            I'm here to help you learn your first 1000 words of a new language.
        </h2>

        <router-link
            to="/welcome/1"
            class="flex items-center justify-center h-12 w-48 rounded-full border-2 border-slate-300 p-4 m-8 text-xl md:text-2xl bg-white hover:bg-slate-100 outline-none"
        >
            Next
        </router-link>
    </div>
</template>

<script>
import PluieMascot from "@/components/PluieMascot.vue";

export default {
    name: "Welcome0",
    components: {
        PluieMascot,
    },
};
</script>

<style></style>
