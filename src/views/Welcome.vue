<template>
    <!-- Div that covers the whole screen -->
    <div
        class="fixed flex inset-0 overflow-y-auto bg-slate-200 z-50 justify-center"
    >
        <div
            class="flex flex-col items-center justify-center text-slate-800 h-full"
        >
            <router-view />
        </div>
    </div>
</template>

<script>
export default {
    name: "Welcome",
};
</script>

<style></style>
