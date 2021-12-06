<template>
    <div class="nav">
        <!-- Logo -->
        <router-link class="logo" :to="{ name: 'Orders' }">
            <img src="../assets/logo/Color logo - no background.png" alt="" />
        </router-link>

        <!-- Search bar -->
        <form @submit.prevent="search" class="search__container">
            <input
                class="search__input"
                type="text"
                v-model="searchContent"
                placeholder="Enter order ID"
            />
        </form>

        <!-- Noti, profile, ... -->
        <div class="nav__icons">
            <router-link :to="{ name: 'OrderCreate' }" class="btn">
                <i class="fas fa-pen"></i>Make order
            </router-link>
            <i class="fas fa-bell notification"></i>
            <router-link
                class="profile-link"
                :to="{
                    name: 'Profile',
                    params: { email: $store.getters.email },
                }"
            >
                <img class="avatar" src="../assets/test/user-icon.jpg" alt="" />
                <i v-if="$store.getters.isAdmin" class="fas fa-crown"></i>
            </router-link>
        </div>
    </div>
</template>

<script>
import { RepositoryFactory } from "../api/backend/Factory";

export default {
    name: "Navigation",
    data() {
        return {
            searchContent: "",
        };
    },
    watch: {
        $route(to, from) {
            if (to.name === "Orders") {
                this.makeOrder = true;
            } else {
                this.makeOrder = false;
            }
        },
    },
    methods: {
        async search() {
            /* Search order id */
            const OrderRepo = RepositoryFactory.get("order");

            try {
                const { data } = await OrderRepo.get(this.searchContent);

                this.$router.push({
                    name: "OrderDetail",
                    params: { id: data.id },
                });
            } catch (e) {
                if (
                    e.response.status === 404 ||
                    e.response.status === 400 ||
                    e.response.status === 401
                ) {
                    this.$router.push({ name: "NotFoundError" });
                }
            } finally {
                this.searchContent = "";
            }
        },
    },
};
</script>

<style lang="scss" scoped>
.nav {
    width: 100%;
    min-height: 9vh;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 2rem;
    box-shadow: rgba(0, 0, 0, 0.02) 0px 1px 3px 0px,
        rgba(27, 31, 35, 0.15) 0px 0px 0px 1px;
    z-index: 1000;

    /* Logo */
    .logo {
        width: 8%;
        cursor: pointer;

        img {
            width: 100%;
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
            font-weight: 600;
            line-height: 18px;

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

    /* Icons */
    &__icons {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100%;

        gap: 1.2rem;

        .btn {
            font-size: 1rem;
            padding: 0.5rem 1rem;
            border-radius: 5px;
        }

        .notification {
            font-size: 1.5rem;
            color: var(--primary-color);
            cursor: pointer;
        }

        .profile-link {
            position: relative;

            .avatar {
                max-height: 40px;
                aspect-ratio: 1 / 1;
                border-radius: 50%;
            }

            i {
                position: absolute;
                color: var(--primary-color);
                left: -10px;
                top: 0;
            }
        }
    }
}
</style>
