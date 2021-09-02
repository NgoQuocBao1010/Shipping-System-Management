<template>
    <div class="nav">
        <img
            class="logo"
            src="../assets/logo/Color logo - no background.png"
            alt=""
        />

        <form @submit.prevent="search" class="search__container">
            <input
                class="search__input"
                type="text"
                v-model="searchContent"
                placeholder="Enter order ID, customer name ..."
            />
        </form>

        <i class="fas fa-bell notification"></i>
    </div>
</template>

<script>
export default {
    name: "Navigation",
    data() {
        return {
            searchContent: "",
        };
    },
    methods: {
        search() {
            console.log(this.searchContent);
            this.searchContent = "";
        },
    },
};
</script>

<style lang="scss" scoped>
.nav {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.5rem 2rem;
    box-shadow: rgba(50, 50, 93, 0.25) 0px 13px 27px -5px,
        rgba(0, 0, 0, 0.3) 0px 8px 16px -8px;

    .logo {
        width: 8%;
    }

    .search {
        &__container {
            width: 40%;
            max-width: 400px;
        }

        &__input {
            width: 100%;
            padding: 12px 24px;

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
                outline: 0;
                border: 1px solid transparent;
                border-bottom: 1px solid #7dccff;
                border-radius: 0;
                background-position: 100% center;
            }
        }
    }

    .notification {
        font-size: 1.5rem;
        color: var(--primary-color);
        cursor: pointer;
    }
}
</style>
