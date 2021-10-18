import Vue from "vue";
import VueRouter from "vue-router";
// Management
import Profile from "../views/Management/Profile.vue";
import Reports from "../views/Management/Reports.vue";
import Management from "../views/Management/Management.vue";
// Orders
import Orders from "../views/Order/OrderList.vue";
import Order from "../views/Order/Order.vue";
import OrderCreate from "../views/Order/OrderCreate.vue";
// Auth
import Login from "../views/Auth/Login.vue";
import Register from "../views/Auth/Register.vue";
import ResetPassword from "../views/Auth/ResetPassword.vue";
// Error
import Unauthorized from "../views/Error/Unauthorized.vue";
// Others
import TestMap from "../views/Map.vue";
import Home from "../views/Home.vue";

import store from "../store/index";

Vue.use(VueRouter);

const routes = [
    /* 
        Routes required authentication
    */
    // Profile
    {
        path: "/profile",
        name: "Profile",
        component: Profile,
        meta: {
            name: "Profile",
            requiredAuth: true,
            adminOnly: false,
        },
    },
    // Orders
    {
        path: "/orders",
        name: "Orders",
        component: Orders,
        meta: {
            name: "Orders",
            requiredAuth: true,
            adminOnly: false,
        },
    },
    // Order detail
    {
        path: "/orders/detail/:id",
        name: "OrderDetail",
        component: Order,
        props: true,
        meta: {
            name: "Order Detail",
            requiredAuth: true,
            adminOnly: false,
        },
    },
    // Order create
    {
        path: "/orders/create/",
        name: "OrderCreate",
        component: OrderCreate,
        meta: {
            name: "Order Create",
            requiredAuth: true,
            adminOnly: false,
        },
    },
    // Report
    {
        path: "/reports",
        name: "Reports",
        component: Reports,
        meta: {
            name: "Reports",
            requiredAuth: "true",
            adminOnly: true,
        },
    },
    // Management
    {
        path: "/management",
        name: "Management",
        component: Management,
        meta: {
            name: "Manangement",
            requiredAuth: true,
            adminOnly: true,
        },
    },
    // Unauthorized
    {
        path: "/unauthorized",
        name: "Unauthorized",
        component: Unauthorized,
        meta: {
            name: "Unauthorized",
            requiredAuth: true,
            adminOnly: false,
        },
    },
    /* 
        Guest visist routes
    */
    // Home
    {
        path: "/",
        name: "Home",
        component: Home,
        meta: {
            name: "Home",
            requiredAuth: false,
        },
    },
    // Test Map
    {
        path: "/test",
        name: "Map",
        component: TestMap,
        meta: {
            name: "TestMap",
            requiredAuth: false,
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
            requiredAuth: false,
        },
    },
    // Register
    {
        path: "/register",
        name: "Register",
        component: Register,
        meta: {
            name: "Register",
            requiredAuth: false,
        },
    },
    // Reset password
    {
        path: "/reset-password",
        name: "ResetPassword",
        component: ResetPassword,
        meta: {
            name: "Reset Password",
            requiredAuth: false,
        },
    },
];

const router = new VueRouter({
    routes,
});

/* 
    Check local storage for token, 
    If there is one, use it to login
*/
router.beforeEach(async (to, from, next) => {
    if (!store.state.authenticated) {
        const token = localStorage.getItem("authToken");
        if (token !== "null" && token !== "") {
            const login = await store.dispatch("login", token);
        }
    }

    next();
});

/*  Check user authorization for each route */
router.beforeEach((to, from, next) => {
    if (store.state.authenticated && !to.meta.requiredAuth) {
        console.log("Logged in user not allowed to view this page");
        return from.name ? next(false) : next({ name: "Orders" });
    }

    if (!store.state.authenticated && to.meta.requiredAuth) {
        console.log("Log in first");
        return from.name ? next(false) : next({ name: "Home" });
    }

    return next();
});

/* Navigation guard for each role */
router.beforeEach((to, from, next) => {
    if (!store.state.authenticated) return next();

    if (store.getters.isAdmin) return next();
    else {
        if (to.meta.adminOnly) return next({ name: "Unauthorized" });
        else next();
    }
});

/* Changing the name of tab */
router.beforeEach((to, from, next) => {
    document.title = `${to.meta.name} | Kaz S.S`;
    return next();
});

export default router;
