<template>
    <nav>
        <p>Kaz Delivery System</p>

        <div class="icons">
            <q-icon name="logout" @click="logout"></q-icon>
        </div>
    </nav>
</template>
<script>
export default {
    name: "Nav",
    methods: {
        logout() {
            this.$store.commit("logout");
        },
    },
};
</script>
<style lang="scss" scoped>
nav {
    width: 100%;
    height: 8vh;
    max-height: 8vh;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 2rem;
    background: var(--primary-color);

    p {
        margin: 0;
        padding: 0;
        font-weight: bold;
        font-size: 1.2rem;
        color: #fff;
    }

    i {
        padding: 0.5rem;
        border-radius: 50%;
        color: #fff;
        background: rgb(255, 57, 57);
        font-size: 1.2rem;
    }
}
</style>
