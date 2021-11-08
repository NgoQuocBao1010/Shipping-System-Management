<template>
    <div class="wrapper">
        <router-link :to="{ name: 'Home' }" class="header">
            <img src="@/assets/logo/Color logo - no background.png" alt="" />
            <p>Kaz Shipping Company</p>
        </router-link>

        <!-- Search bar -->
        <form @submit.prevent="search" class="search__container">
            <input
                class="search__input"
                type="text"
                v-model="orderId"
                placeholder="Look for your order here"
            />
        </form>

        <div class="navigation">
            <router-link :to="{ name: 'Login' }" class="btn small">
                <i class="fas fa-sign-in-alt"></i> Login
            </router-link>
            <router-link :to="{ name: 'Register' }" class="btn small register">
                <i class="fas fa-user-edit"></i> Register
            </router-link>
        </div>
    </div>
</template>

<script>
export default {
    name: "HomeNav",
    data() {
        return {
            orderId: null,
        };
    },
    methods: {
        async search() {
            /* Search order id */
            this.$router.push({
                name: "OrderPreview",
                params: { id: this.orderId },
            });

            this.orderId = null;
        },
    },
};
</script>

<style lang="scss" scoped>
.wrapper {
    width: 100%;
    padding: 0.2rem 2rem;
    min-height: 8vh;
    display: flex;
    align-items: center;
    justify-content: space-between;

    box-shadow: rgba(0, 0, 0, 0.02) 0px 1px 3px 0px,
        rgba(27, 31, 35, 0.15) 0px 0px 0px 1px;

    /* Image Logo */
    .header {
        text-decoration: none;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;

        img {
            max-height: 50px;
        }

        p {
            font-weight: bold;
            font-size: 20px;
            color: var(--primary-color);
        }
    }

    /* Search bar */
    .search {
        &__container {
            width: 50%;
            max-width: 400px;
        }

        &__input {
            width: 100%;
            padding: 6px 12px;
            @media only screen and (min-width: 1200px) {
                padding: 8px 16px;
            }

            background-color: transparent;
            transition: transform 250ms ease-in-out;
            font-size: 1rem;
            line-height: 18px;

            color: #575756;
            background-color: transparent;

            background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3Cpath d='M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z'/%3E%3Cpath d='M0 0h24v24H0z' fill='none'/%3E%3C/svg%3E");
            background-repeat: no-repeat;
            background-size: 18px 18px;
            background-position: 95% center;
            border-radius: 50px;
            border: 1px solid #7dccff;
            transition: all 250ms ease-in-out;
            backface-visibility: hidden;
            transform-style: preserve-3d;

            &::placeholder {
                color: color(#7dccff a(0.8));
                letter-spacing: 1;
            }

            &:hover,
            &:focus {
                padding: 12px 0;
                @media only screen and (min-width: 1200px) {
                    padding: 6px 0;
                }
                outline: 0;
                border: 1px solid transparent;
                border-bottom: 1px solid #7dccff;
                border-radius: 0;
                background-position: 100% center;
            }
        }
    }

    /* Navigation */
    .navigation {
        > * {
            margin-left: 1rem;
        }

        .register {
            background: orange;

            &:hover {
                background: white;
                color: orange;
                box-shadow: rgba(0, 0, 0, 0.02) 0px 1px 3px 0px,
                    rgba(27, 31, 35, 0.15) 0px 0px 0px 1px;
            }
        }
    }
}
</style>
