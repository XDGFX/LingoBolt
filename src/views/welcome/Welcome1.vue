<template>
    <div class="m-8 md:mx-32 gap-2 flex flex-col text-center">
        <h2 class="text-4xl pt-8 pb-4 text-slate-500">Here are some tips:</h2>
        <ul class="text-xl md:text-2xl gap-4 flex flex-col">
            <li>Revise 📖 new words on the following screen.</li>
            <li>
                When you are ready, go to the Practice 🎓 page to test your
                knowledge!
            </li>
            <li>
                With a strong focus on vocabulary&nbsp📚, I work best alongside
                other learning tools.
            </li>
        </ul>

        <h2 class="text-2xl pt-8 pb-4 text-slate-500">Disclaimer:</h2>
        <p class="text-s gap-4 flex flex-col lg:w-[990px]">
            While I strive to provide accurate and reliable translations, please
            keep in mind that language is constantly evolving and that my
            translations may not always reflect the most current usage. Use this
            site as a guide to help you understand new words and phrases, but be
            open to learning and growing as you continue your language learning
            journey!
        </p>

        <router-link
            to="/"
            class="flex self-center items-center justify-center h-12 w-48 rounded-full border-2 border-slate-300 p-4 m-8 text-xl md:text-2xl bg-white hover:bg-slate-100 outline-none"
        >
            Let's go!
        </router-link>
    </div>
</template>

<script>
export default {
    name: "Welcome1",
};
</script>

<style></style>
