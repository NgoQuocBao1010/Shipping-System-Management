<template>
    <div>
        <h1>Oops, this page is not available</h1>
        <p>
            Go back to
            <router-link
                v-if="$store.getters.isAuthenticated"
                :to="{ name: 'Orders' }"
            >
                your orders
            </router-link>
            <router-link v-else :to="{ name: 'Home' }"> Home page </router-link>
        </p>
    </div>
</template>

<script>
export default {
    name: "NotFound",
};
</script>

<style lang="scss" scoped></style>
