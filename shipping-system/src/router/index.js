import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Profile from "../views/Profile.vue";
import Reports from "../views/Reports.vue";
import Orders from "../views/Orders.vue";
import OrderDetail from "../views/OrderDetail.vue";
import OrderCreate from "../views/OrderCreate.vue";
import Management from "../views/Management.vue";
import TestMap from "../views/Map.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import ResetPassword from "../views/ResetPassword.vue";

import store from "../store/index";

Vue.use(VueRouter);

const routes = [
    // Home
    {
        path: "/",
        name: "Home",
        component: Home,
        meta: {
            name: "Home",
            guest: true,
        },
    },
    // Profile
    {
        path: "/profile",
        name: "Profile",
        component: Profile,
        meta: {
            name: "Profile",
            guest: false,
        },
    },
    // Orders
    {
        path: "/orders",
        name: "Orders",
        component: Orders,
        meta: {
            name: "Orders",
            guest: false,
        },
    },
    // Order detail
    {
        path: "/orders/detail/:id",
        name: "OrderDetail",
        component: OrderDetail,
        props: true,
        meta: {
            name: "Order Detail",
            guest: false,
        },
    },
    // Order create
    {
        path: "/orders/create/",
        name: "OrderCreate",
        component: OrderCreate,
        meta: {
            name: "OrderCreate",
            guest: false,
        },
    },
    // Report
    {
        path: "/reports",
        name: "Reports",
        component: Reports,
        meta: {
            name: "Report",
            guest: false,
        },
    },
    // Management
    {
        path: "/management",
        name: "Management",
        component: Management,
        meta: {
            name: "Manangement",
            guest: false,
        },
    },
    // Management
    {
        path: "/test",
        name: "Map",
        component: TestMap,
        meta: {
            name: "TestMap",
            guest: false,
        },
    },
    // Login
    {
        path: "/login",
        name: "Login",
        component: Login,
        props: true,
        meta: {
            name: "Login",
            guest: true,
        },
    },
    // Register
    {
        path: "/register",
        name: "Register",
        component: Register,
        meta: {
            name: "Register",
            guest: true,
        },
    },
    // Reset password
    {
        path: "/reset-password",
        name: "ResetPassword",
        component: ResetPassword,
        meta: {
            name: "Reset Password",
            guest: true,
        },
    },
];

const router = new VueRouter({
    mode: "history",
    routes,
});

// Routing resctrition
router.beforeEach(async (to, from, next) => {
    // Not Authenticated
    if (!store.state.authenticated) {
        let login = false;
        const token = localStorage.getItem("authToken");
        if (token !== "null" && token !== "") {
            login = await store.dispatch("login", token);
        }

        if (!login && !to.meta.guest) return next({ name: "Home" });
        if (login && to.meta.guest) return next({ name: "Reports" });
        else next();
    } else {
        // Authenticated
        if (to.meta.guest) return next({ name: "Reports" });
        return next();
    }
});

// Changing name
router.beforeEach((to, from, next) => {
    document.title = `${to.meta.name} | Kaz S.S`;
    return next();
});

export default router;
