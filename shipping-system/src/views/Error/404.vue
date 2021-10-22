<template>
    <div>
        <h1>Oops, this page is not available</h1>
        <p>
            Go back to
            <router-link :to="{ name: 'Orders' }"> your orders </router-link>
        </p>
    </div>
</template>

<script>
export default {
    name: "NotFound",
};
</script>

<style lang="scss" scoped></style>
