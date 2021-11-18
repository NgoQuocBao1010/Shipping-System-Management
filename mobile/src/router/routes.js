const routes = [
    {
        path: "/",
        component: () => import("layouts/MainLayout.vue"),
        children: [
            {
                path: "",
                name: "home",
                component: () => import("pages/Index.vue"),
                meta: {
                    requireAuth: true,
                },
            },
        ],
    },
    {
        path: "/login",
        name: "login",
        component: () => import("pages/Login.vue"),
        meta: {
            nonAuthOnly: true,
        },
    },

    // Always leave this as last one,
    // but you can also remove it
    {
        path: "*",
        component: () => import("pages/Error404.vue"),
    },
];

export default routes;
