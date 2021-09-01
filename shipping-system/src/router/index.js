import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Reports from "../views/Reports.vue";
import Orders from "../views/Orders.vue";
import Management from "../views/Management.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import ResetPassword from "../views/ResetPassword.vue";

Vue.use(VueRouter);

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
    },
    {
        path: "/orders",
        name: "Orders",
        component: Orders,
    },
    {
        path: "/reports",
        name: "Reports",
        component: Reports,
    },
    {
        path: "/management",
        name: "Management",
        component: Management,
    },
    {
        path: "/login",
        name: "Login",
        component: Login,
    },
    {
        path: "/register",
        name: "Register",
        component: Register,
    },
    {
        path: "/reset-password",
        name: "ResetPassword",
        component: ResetPassword,
    },
];

const router = new VueRouter({
    mode: "history",
    routes,
});

export default router;
