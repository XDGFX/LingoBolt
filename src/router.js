import { createWebHistory, createRouter } from "vue-router";

import Welcome from "./views/Welcome.vue";
import Welcome0 from "./views/welcome/Welcome0.vue";
import Welcome1 from "./views/welcome/Welcome1.vue";
import Home from "./views/Home.vue";
import Quiz from "./views/Quiz.vue";
import LanguageSelect from "./views/LanguageSelect.vue";

const routes = [
    {
        path: "/welcome",
        component: Welcome,
        redirect: "/welcome/0",
    },
    {
        path: "/welcome",
        component: Welcome,
        children: [
            {
                path: "/welcome/0",
                component: Welcome0,
            },
            {
                path: "/welcome/1",
                component: Welcome1,
            },
        ],
    },
    {
        path: "/",
        component: Home,
        exact: true,
    },
    {
        path: "/quiz",
        component: Quiz,
        exact: true,
    },
    {
        path: "/language-select",
        component: LanguageSelect,
        exact: true,
    },
];

const router = new createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
