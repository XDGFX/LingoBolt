import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

import "./assets/main.css";

const app = createApp(App);

// So we can use computed() which allows reactive inject/provide
app.config.unwrapInjectedRef = true;

app.use(router);

app.mount("#app");
