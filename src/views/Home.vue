<template>
    <section
        class="flex flex-col items-center h-screen bg-slate-100 text-slate-900 md:px-4 md:py-8 pb-16"
    >
        <!-- Desktop menu -->
        <div class="w-full lg:w-[990px] hidden md:flex flex-wrap items-center">
            <h1 class="text-4xl flex-1">
                <img
                    src="@/assets/logo.svg"
                    alt="LingoBolt logo"
                    class="h-12"
                />
            </h1>

            <div class="flex flex-2 gap-4 items-center">
                <!-- Search box -->
                <input
                    v-model="search"
                    class="h-12 shrink rounded-full border-2 border-slate-200 p-4 text-2xl focus:border-rose-500 outline-none"
                    type="text"
                    placeholder="Search"
                />

                <!-- Hide translations -->
                <button
                    class="h-12 w-12 flex justify-center items-center rounded-full border-2 border-slate-200 p-4 text-2xl bg-white hover:bg-slate-100 outline-none"
                    @click="hideTranslations = !hideTranslations"
                    title="Hide translations"
                >
                    <span>🔖</span>
                </button>

                <span class="text-slate-300 text-4xl select-none -translate-y-1"
                    >·</span
                >

                <!-- Quiz button -->
                <router-link
                    to="/quiz"
                    class="h-12 w-12 flex justify-center items-center rounded-full border-2 border-slate-200 text-slate-500 p-4 text-2xl bg-white hover:bg-slate-100 outline-none"
                    title="Practice"
                >
                    <span class="translate-y-px"> 🎓 </span>

                    <!-- Notification circle -->
                    <div
                        v-if="settings.firstLoad"
                        class="absolute h-4 w-4 translate-x-full -translate-y-full"
                    >
                        <div
                            class="h-4 w-4 rounded-full bg-cyan-400 animate-ping"
                        ></div>
                        <div
                            class="h-4 w-4 rounded-full bg-cyan-400 -translate-y-full"
                        ></div>
                    </div>
                </router-link>

                <!-- Language select -->
                <router-link
                    to="/language-select"
                    class="h-12 w-12 flex justify-center items-center rounded-full border-2 border-slate-200 p-4 text-2xl bg-white hover:bg-slate-100 outline-none"
                    title="Change language"
                >
                    <span class="translate-y-px">🌐</span>
                </router-link>
            </div>
        </div>

        <!-- <carousel
            :words="wordsFiltered"
            :wordScores="settings.stats[settings.language].wordScores"
            :hide-translations="hideTranslations"
        ></carousel> -->

        <!-- Mobile menu -->
        <div
            class="fixed bottom-0 w-full z-[999] md:hidden flex justify-around bg-slate-200 p-2 border-t-2 rounded-t-[24px] border-slate-300"
        >
            <div class="flex gap-4 items-center justify-between w-full">
                <!-- Search box -->
                <input
                    v-model="search"
                    class="h-12 w-12 shrink focus:w-full peer transition-all flex justify-center p-4 rounded-full border-2 border-slate-200 outline-none text-2xl bg-white"
                    type="text"
                />

                <!-- Div which overlays the previous input -->
                <div
                    v-if="search === ''"
                    class="h-12 w-12 peer-focus:hidden pointer-events-none absolute flex justify-center items-center rounded-full border-2 border-slate-200 text-2xl bg-white"
                >
                    <span>🔎</span>
                </div>

                <!-- Clear search button -->
                <button
                    v-else
                    class="h-12 w-12 peer-focus:hidden absolute flex justify-center items-center rounded-full border-2 border-slate-200 text-2xl bg-white"
                    @click="search = ''"
                >
                    <span>❌</span>
                </button>

                <!-- Hide translations -->
                <button
                    class="h-12 w-12 peer-focus:hidden flex justify-center items-center rounded-full border-2 border-slate-200 text-2xl bg-white"
                    @click="hideTranslations = !hideTranslations"
                    title="Hide translations"
                >
                    🔖
                </button>

                <!-- Quiz button -->
                <router-link
                    to="/quiz"
                    class="h-12 w-12 peer-focus:hidden flex justify-center items-center rounded-full border-2 border-slate-200 text-2xl bg-white"
                    title="Practice"
                >
                    <span class="translate-y-px"> 🎓 </span>

                    <!-- Notification circle -->
                    <div
                        v-if="settings.firstLoad"
                        class="absolute h-4 w-4 translate-x-full -translate-y-full"
                    >
                        <div
                            class="h-4 w-4 rounded-full bg-cyan-400 animate-ping"
                        ></div>
                        <div
                            class="h-4 w-4 rounded-full bg-cyan-400 -translate-y-full"
                        ></div>
                    </div>
                </router-link>

                <!-- Language select -->
                <router-link
                    to="/language-select"
                    class="h-12 w-12 peer-focus:hidden flex justify-center items-center rounded-full border-2 border-slate-200 text-2xl bg-white"
                    title="Change language"
                >
                    <span class="translate-y-px">🌐</span>
                </router-link>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: "Home",
    data() {
        return {
            search: "",
            hideTranslations: false,
        };
    },
};
</script>

<style></style>
