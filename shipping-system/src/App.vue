<template>
    <div id="app">
        <Sidebar v-if="navigation" />
        <div class="container">
            <Navigation v-if="navigation" />
            <router-view class="container__content" />
        </div>
    </div>
</template>

<script>
import { mapActions } from "vuex";
import axios from "axios";

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
        ...mapActions(["login"]),
        checkRoute() {
            // Hide and show navigation bar depending on the page
            const routesWithNoNav = [
                "Login",
                "Register",
                "ResetPassword",
                "Home",
            ];

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
    mounted() {},
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
    max-height: 100vh;

    display: flex;
    flex-direction: column;

    &__content {
        padding: 2rem;
        flex: 1 1 80%;
        overflow-y: scroll;
    }
}

.btn,
button {
    padding: 0.5rem 2rem;
    border: none;
    text-decoration: none;
    border-radius: 20px;
    font-size: 16px;
    color: #fff;
    background-color: var(--primary-color);
    cursor: pointer;
    transition: 0.3s ease-in-out all;

    i {
        margin-right: 5px;
        font-size: 0.8rem;
    }

    &:focus {
        outline: none;
    }

    &:hover {
        background-color: var(--secondary-color);
    }

    &.small {
        padding: 0.5rem 1rem;
        border-radius: 5px;
        font-size: 12px;
    }
}

select {
    -webkit-appearance: none;
    -moz-appearance: none;
    -ms-appearance: none;
    appearance: none;
    outline: 0;
    box-shadow: none;
    border: 0 !important;
    // background: var(--primary-color);
    background-image: none;

    &::-ms-expand {
        display: none;
    }
}

input::-webkit-calendar-picker-indicator {
    cursor: pointer;
}

.order-processing,
.order-delivering,
.order-delivered,
.order-failed {
    padding: 5px 10px;
    font-size: 14px;
    font-weight: 500;
    border-radius: 20px;
    color: #fff;
    text-align: center;
    text-transform: capitalize;
}

.order-processing,
.order-delivering {
    background-color: var(--secondary-color);
}

.order-delivered {
    background-color: lightgreen;
}

.order-failed {
    background-color: rgb(238, 78, 78);
}

.role {
    font-size: 0.8rem;
    width: 80px;
    padding: 0.2rem 0.5rem;
    margin: 0.2rem 0;
    text-align: center;
    text-transform: capitalize;
    font-weight: 600;
    border-radius: 20px;

    &.manager {
        background-color: rgb(255, 184, 184);
    }

    &.driver {
        background-color: var(--secondary-color);
    }

    &.customer {
        background-color: lightgreen;
    }
}
</style>
