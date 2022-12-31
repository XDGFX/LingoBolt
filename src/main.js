import { createApp } from "vue";
import App from "./App.vue";

import "./assets/main.css";

const app = createApp(App);

// So we can use computed() which allows reactive inject/provide
app.config.unwrapInjectedRef = true;

app.mount("#app");
