<template>
    <div class="home">
        <h1>This is the home page</h1>
        <router-link :to="{ name: 'Login' }">Login</router-link>
        <br />
        <router-link :to="{ name: 'Register' }">Register</router-link>
    </div>
</template>

<script>
export default {
    name: "Home",
    components: {},
};
</script>

<style lang="scss" scoped>
.home {
    .block {
        width: 200px;
        aspect-ratio: 1 / 1;
        background: lightgreen;
        margin: 1rem 0;
    }
}
</style>
