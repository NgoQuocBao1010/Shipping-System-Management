<template>
    <div class="home">
        <div class="hero">
            <img src="../assets/hero.jpg" alt="" />

            <router-link class="btn btn-hero" :to="{ name: 'Login' }">
                Place Your First Order Now
            </router-link>
        </div>

        <section>
            <a href="#price" class="stuff">
                <i class="fas fa-money-check-alt"></i>
                <p>Pricing List</p>
            </a>
            <a href="#contact" class="stuff">
                <i class="fas fa-address-book"></i>
                <p>Contacts</p>
            </a>
        </section>

        <section>
            <PriceShipping class="price" />
        </section>
    </div>
</template>

<script>
import PriceShipping from "./PriceShipping.vue";

export default {
    name: "Home",
    components: {
        PriceShipping,
    },
};
</script>

<style lang="scss" scoped>
.home {
    padding: 0 !important;
    scroll-behavior: smooth;

    .hero {
        width: 100%;
        min-height: 60vh;
        max-height: 60vh;
        overflow: hidden;
        position: relative;

        img {
            width: 100%;
            position: absolute;
            bottom: -100px;
        }

        a.btn-hero {
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

    section {
        width: 100%;
        padding: 2rem 0;
        display: flex;
        justify-content: space-around;
        margin-bottom: 100px;

        .stuff {
            flex: 1 1 40%;
            max-width: 250px;
            padding: 1rem;
            color: black;
            text-decoration: none;
            display: flex;
            flex-direction: column;
            align-items: center;
            border-radius: 10px;
            box-shadow: rgba(0, 0, 0, 0.05) 0px 6px 24px 0px,
                rgba(0, 0, 0, 0.08) 0px 0px 0px 1px;
            cursor: pointer;
            transition: all 0.2s ease;

            &:hover {
                transform: scale(1.03);
            }

            i {
                font-size: 6rem;
            }

            p {
                margin-top: 3rem;
                font-size: 1.2rem;
                font-weight: 500;
            }
        }

        .price {
            width: 90%;
        }
    }
}
</style>
