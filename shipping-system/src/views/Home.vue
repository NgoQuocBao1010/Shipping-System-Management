<template>
    <div class="home">
        <HomeNav />
        <h1>This is the home page</h1>
        <router-link :to="{ name: 'Login' }">Login</router-link>
        <br />
        <router-link :to="{ name: 'Register' }">Register</router-link>
    </div>
</template>

<script>
import HomeNav from "../components/home/Nav.vue";

export default {
    name: "Home",
    components: {
        HomeNav,
    },
};
</script>

<style lang="scss" scoped>
.home {
    padding: 0 !important;
}
</style>
