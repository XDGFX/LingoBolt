import { createApp } from "vue";

import App from "./App.vue";

import router from "./lib/router";
import { createPinia } from "pinia";

import "./assets/main.css";

const app = createApp(App);

// So we can use computed() which allows reactive inject/provide
app.config.unwrapInjectedRef = true;

app.use(router);
app.use(createPinia());

app.mount("#app");
