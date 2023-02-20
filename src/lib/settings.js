import { defineStore } from "pinia";
import { watch } from "vue";

// Default settings object
const defaultSettings = {
    firstLoad: true,
    language: null,
    hideTranslations: false,
    stats: {},
};

const defaultStats = {
    elo: 500,
    score: 0,
    count: 0,
    wordScores: null,
};

let settings = JSON.parse(localStorage.getItem("settings"));

// If settings is defined, set firstLoad to false
if (settings) {
    settings.firstLoad = false;
} else {
    settings = defaultSettings;
}

// Make sure all the requred keys are present
for (const key in defaultSettings) {
    if (!(key in settings)) {
        // Make a deep copy of the default settings
        settings[key] = JSON.parse(JSON.stringify(defaultSettings[key]));
    }
}

export const useSettingsStore = defineStore("settings", {
    state: () => ({
        ...settings,
    }),
    getters: {
        // Get the user's stats for a language
        getStats: (state) => (language) => {
            if (language in state.stats) {
                return state.stats[language];
            } else {
                return defaultStats;
            }
        },
    },
});

// Watch for changes to the settings object and save them to localStorage
watch(
    () => useSettingsStore().$state,
    (newSettings) => {
        localStorage.setItem("settings", JSON.stringify(newSettings));
    }
);
