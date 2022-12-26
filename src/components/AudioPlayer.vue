<template>
    <div>
        <!-- <audio ref="audio" crossorigin="anonymous"></audio> -->
        <button @click="playAudio">
            <!-- <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-6 w-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
            >
            </svg> -->
            <!-- Speaker icon -->
            <img
                class="h-6 w-6 fill-slate-300"
                src="../assets/speaker.svg"
                alt="Speaker icon"
            />
        </button>
    </div>
</template>

<script>
export default {
    name: "AudioPlayer",
    props: {
        word: {
            type: String,
            required: true,
        },
    },
    data() {
        return {
            audioUrl:
                "https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=fr&q=" +
                this.word,
        };
    },
    methods: {
        playAudio() {
            const utterance = new SpeechSynthesisUtterance(this.word);
            utterance.lang = "fr";
            utterance.rate = 0.8;

            speechSynthesis.speak(utterance);
        },
    },
};
</script>
