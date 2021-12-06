import Vue from "vue";
import VueRouter from "vue-router";
// Management
import Profile from "../views/Management/Profile.vue";
import Reports from "../views/Management/Reports.vue";
import Management from "../views/Management/Management.vue";
import DriverAdminis from "@/views/Management/DriverAdminis.vue";
// Orders
import Orders from "../views/Order/OrderList.vue";
import Order from "../views/Order/Order.vue";
import OrderCreate from "../views/Order/OrderCreate.vue";
import OrderEdit from "../views/Order/OrderEdit.vue";
import OrderPreview from "../views/Order/OrderPreview.vue";
// Authorization
import Login from "../views/Auth/Login.vue";
import Register from "../views/Auth/Register.vue";
import ResetPassword from "../views/Auth/ResetPassword.vue";
// Error
import Unauthorized from "../views/Error/Unauthorized.vue";
import InternalError from "../views/Error/500.vue";
import NotFoundError from "../views/Error/404.vue";
// Others
import Home from "../views/Home.vue";
import PriceShipping from "../views/PriceShipping.vue";

import store from "../store/index";

Vue.use(VueRouter);

const routes = [
    //    * Routes required authentication
    // Profile
    {
        path: "/profile/:email",
        name: "Profile",
        component: Profile,
        props: true,
        meta: {
            name: "Profile",
            authOnly: true,
            adminOnly: false,
        },
    },
    // Orders List for Management
    {
        path: "/orders",
        name: "Orders",
        component: Orders,
        meta: {
            name: "Orders",
            authOnly: true,
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
            authOnly: true,
            adminOnly: false,
        },
    },
    // Order Edit
    {
        path: "/orders/edit/:id",
        name: "OrderEdit",
        component: OrderEdit,
        props: (route) => ({
            id: route.params.id,
            orderInstance: route.params.orderInstance,
        }),
        meta: {
            name: "Order Edit",
            authOnly: true,
            adminOnly: true,
        },
    },
    // Order create
    {
        path: "/orders/create/",
        name: "OrderCreate",
        component: OrderCreate,
        meta: {
            name: "Order Create",
            authOnly: true,
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
            authOnly: true,
            adminOnly: true,
        },
    },
    // Driver Account Administrator
    {
        path: "/driver-adminis",
        name: "DriverAdministrator",
        component: DriverAdminis,
        meta: {
            name: "Driver Administrator",
            authOnly: true,
            adminOnly: true,
        },
    },
    // * Error page, access for all kind of user
    // Unauthorized
    {
        path: "/unauthorized",
        name: "Unauthorized",
        component: Unauthorized,
        meta: {
            name: "Unauthorized",
            authOnly: true,
            adminOnly: false,
        },
    },
    // Internal Error
    {
        path: "/500",
        name: "InternalError",
        component: InternalError,
        meta: {
            name: "Internal Error",
            authOnly: true,
            adminOnly: false,
        },
    },
    // 404 Error
    {
        path: "/404",
        name: "NotFoundError",
        component: NotFoundError,
        meta: {
            name: "Not Found",
            easy: true,
        },
    },
    // * Guest visist routes
    // Home
    {
        path: "/",
        name: "Home",
        component: Home,
        meta: {
            name: "Home",
            nonAuthOnly: true,
        },
    },
    // Shipping Price
    {
        path: "/price-shipping",
        name: "PriceShipping",
        component: PriceShipping,
        meta: {
            name: "Shipping Price",
            easy: true,
        },
    },
    // Order Preview
    {
        path: "/preview/:id",
        name: "OrderPreview",
        props: true,
        component: OrderPreview,
        meta: {
            name: "Order Preview",
            easy: true,
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
            nonAuthOnly: true,
        },
    },
    // Register
    {
        path: "/register",
        name: "Register",
        component: Register,
        meta: {
            name: "Register",
            nonAuthOnly: true,
        },
    },
    // Reset password
    {
        path: "/reset-password",
        name: "ResetPassword",
        component: ResetPassword,
        meta: {
            name: "Reset Password",
            nonAuthOnly: true,
        },
    },
    // * Catch non-existance path
    { path: "/:pathMatch(.*)*", component: NotFoundError },
];

const router = new VueRouter({
    mode: "history",
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
    // Easy page can access whether user is auth or not
    if (to.meta.easy) return next();

    // Restrict auth user to visit un-auth page
    if (store.state.authenticated && to.meta.nonAuthOnly) {
        console.log("Logged in user not allowed to view this page");
        return from.name ? next(false) : next({ name: "Orders" });
    }

    // Resctrict un-auth user to visit auth only page
    if (!store.state.authenticated && to.meta.authOnly) {
        console.log("Unauth user not allowed to view this page in first");
        return from.name ? next(false) : next({ name: "Home" });
    }

    return next();
});

/* Navigation guard for each role */
router.beforeEach((to, from, next) => {
    // Unauth user or access easy page
    if (!store.state.authenticated || to.meta.easy) return next();

    // Auth user
    if (store.getters.isAdmin || store.getters.isStaff) return next();
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
