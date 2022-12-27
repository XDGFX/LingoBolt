<template>
    <!-- <audio ref="audio" crossorigin="anonymous"></audio> -->
    <button @click="playAudio" ref="btn" class="disabled:opacity-50">
        <img class="h-6 w-6" src="../assets/speaker.svg" alt="Speaker icon" />
    </button>
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

            // Disable the button until the audio is done playing
            this.$refs.btn.disabled = true;

            // Re-enable the button after the audio is done playing
            utterance.onend = () => {
                this.$refs.btn.disabled = false;
            };
        },
    },
};
</script>
