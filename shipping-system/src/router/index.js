import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Profile from "../views/Profile.vue";
import Reports from "../views/Reports.vue";
import Orders from "../views/Orders.vue";
import OrderDetail from "../views/OrderDetail.vue";
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
        meta: {
            name: "Home",
        },
    },
    {
        path: "/profile",
        name: "Profile",
        component: Profile,
        meta: {
            name: "Profile",
        },
    },
    {
        path: "/orders",
        name: "Orders",
        component: Orders,
        meta: {
            name: "Orders",
        },
    },
    {
        path: "/orders/:id",
        name: "OrderDetail",
        component: OrderDetail,
        props: true,
        meta: {
            name: "Order Detail",
        },
    },
    {
        path: "/reports",
        name: "Reports",
        component: Reports,
        meta: {
            name: "Report",
        },
    },
    {
        path: "/management",
        name: "Management",
        component: Management,
        meta: {
            name: "Manangement",
        },
    },
    {
        path: "/login",
        name: "Login",
        component: Login,
        meta: {
            name: "Login",
        },
    },
    {
        path: "/register",
        name: "Register",
        component: Register,
        meta: {
            name: "Register",
        },
    },
    {
        path: "/reset-password",
        name: "ResetPassword",
        component: ResetPassword,
        meta: {
            name: "Reset Password",
        },
    },
];

const router = new VueRouter({
    mode: "history",
    routes,
});

router.beforeEach((to, from, next) => {
    document.title = `${to.meta.name} | Kaz S.S`;
    next();
});

export default router;
