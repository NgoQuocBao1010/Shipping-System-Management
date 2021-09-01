<template>
    <div id="app">
        <Sidebar v-if="navigation" />
        <div class="container">
            <Navigation />
            <router-view />
        </div>
    </div>
</template>

<script>
import Sidebar from "./components/Sidebar.vue";
import Navigation from "./components/Navigation.vue";

export default {
    name: "App",
    components: {
        Sidebar,
        Navigation,
    },
    data() {
        return {
            navigation: null,
        };
    },
    watch: {
        $route() {
            this.checkRoute();
        },
    },
    methods: {
        checkRoute() {
            // Hide and show navigation bar depending on the page
            const routesWithNoNav = ["Login", "Register", "ResetPassword"];

            if (routesWithNoNav.includes(this.$route.name)) {
                this.navigation = false;
                return;
            }

            this.navigation = true;
        },
    },
    created() {
        this.checkRoute();
    },
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;500;600;700&display=swap");
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Quicksand", sans-serif;
}
:root {
    --primary-color: #1190cb;
    --secondary-color: #7dccff;
    --dark-color: #362222;
    --white: #ffffff;
}
#app {
    display: flex;
    min-height: 100vh;
}
.container {
    width: 100%;
}
button {
    padding: 0.5rem 2rem;
    border: none;
    border-radius: 20px;
    font-size: 16px;
    color: #fff;
    background-color: var(--primary-color);
    cursor: pointer;
    transition: 0.3s ease-in-out all;

    &:focus {
        outline: none;
    }

    &:hover {
        background-color: var(--secondary-color);
    }
}
</style>
