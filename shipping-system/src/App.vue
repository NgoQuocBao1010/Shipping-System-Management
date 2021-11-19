<template>
    <div id="app">
        <Sidebar v-if="showNav" />
        <div class="container">
            <AuthNavigation v-if="showNav" />
            <UnauthNav
                v-if="
                    !showNav &&
                    !['Login', 'Register', 'ResetPassword'].includes($route.name)
                "
            />
            <router-view class="container__content" :key="$route.path" />
        </div>
    </div>
</template>

<script>
import "vue-toast-notification/dist/theme-sugar.css";
import { mapMutations, mapActions } from "vuex";

// Leaflet requirements
import "leaflet/dist/leaflet.css";
import "leaflet-routing-machine/dist/leaflet-routing-machine.css";
import L from "leaflet";
import { IRouter, IGeocoder, LineOptions } from "leaflet-routing-machine";

import Sidebar from "./components/Sidebar.vue";
import AuthNavigation from "./components/Navigation.vue";
import UnauthNav from "./components/home/Nav.vue";

export default {
    name: "App",
    components: {
        Sidebar,
        AuthNavigation,
        UnauthNav,
    },
    computed: {
        showNav() {
            return this.$store.getters.isAuthenticated;
        },
    },
    methods: {
        ...mapMutations(["saveProvinceInfo"]),
        ...mapActions(["login"]),
    },
    async beforeCreate() {
        const districts = await this.$province.getAllDistricts();
        this.saveProvinceInfo(districts);
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

html {
    scroll-behavior: smooth;
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

a.normal-link {
    text-decoration: none;
    color: var(--primary-color);
    font-weight: 900;
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
    max-width: 120px;
    padding: 5px 10px;
    font-size: 14px;
    font-weight: 600;
    border-radius: 20px;
    color: #fff;
    text-align: center;
    text-transform: capitalize;
}

.order-processing {
    background-color: #8fd6e1;
}

.order-delivering {
    background-color: var(--secondary-color);
}

.order-delivered {
    font-weight: bold;
    color: var(--dark-color);
    background-color: lightgreen;
}

.close,
.order-failed {
    background-color: #ee4e4e;
}

.role {
    font-size: 0.8rem;
    width: max-content;
    min-width: 120px;
    padding: 0.2rem 0.5rem;
    margin: 0.2rem 0;
    text-align: center;
    font-weight: 600;
    border-radius: 20px;
}

.color {
    &.manager {
        background-color: rgb(255, 184, 184);
    }

    &.driver {
        background-color: lightgreen;
    }

    &.customer {
        background-color: var(--secondary-color);
    }
}

.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-to {
    opacity: 0;
}
</style>
