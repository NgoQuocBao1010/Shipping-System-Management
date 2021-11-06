<template>
    <div class="home">
        <div class="hero">
            <img src="../assets/hero.jpg" alt="" />

            <button>Place Your First Order Now</button>
        </div>
    </div>
</template>

<script>
export default {
    name: "Home",
};
</script>

<style lang="scss" scoped>
.home {
    padding: 0 !important;

    .hero {
        width: 100%;
        height: 50vh;
        overflow: hidden;
        position: relative;

        img {
            width: 100%;
            position: absolute;
            bottom: -100px;
        }

        button {
            padding: 1rem 2rem;
            font-size: 1.2rem;
            font-weight: bold;
            position: absolute;
            z-index: 1000;
            top: 60%;
            left: 50%;
            transform: translate(-50%, -50%);
        }
    }
}
</style>
