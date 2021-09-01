<template>
    <div id="app">
        <div id="nav" v-if="navigation">
            <router-link to="/">Home</router-link> |
            <router-link to="/about">About</router-link>
        </div>
        <router-view />
    </div>
</template>

<script>
export default {
    name: "App",
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
            // Check if there is navigation bar in the route
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
.app {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}
.container {
    max-width: 1440px;
    margin: 0 auto;
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
