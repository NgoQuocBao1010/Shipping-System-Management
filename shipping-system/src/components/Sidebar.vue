<template>
    <div class="sidebar-container" :class="{ active: expand }">
        <ul class="links">
            <li
                v-for="(page, index) in pages"
                :key="index"
                class="link"
                :class="{ active: page.name === currentRoute }"
            >
                <router-link :to="{ name: page.name }">
                    <span class="icon"><i :class="page.iconClass"></i></span>
                    <span class="title">{{ page.name }}</span>
                </router-link>
            </li>
        </ul>

        <i
            class="fas fa-chevron-right toggle-arrow"
            :class="{ active: expand }"
            @click="expand = !expand"
        ></i>
    </div>
</template>

<script>
export default {
    name: "Sidebar",
    data() {
        return {
            pages: [
                {
                    name: "Home",
                    iconClass: "fas fa-house-user",
                },
                {
                    name: "Management",
                    iconClass: "fas fa-users",
                },
                {
                    name: "Reports",
                    iconClass: "fas fa-clipboard-list",
                },
                {
                    name: "Orders",
                    iconClass: "fas fa-shipping-fast",
                },
            ],
            expand: false,
        };
    },
    computed: {
        currentRoute() {
            return this.$route.name;
        },
    },
    created() {
        console.log(this.expand);
    },
};
</script>

<style lang="scss" scoped>
.sidebar-container {
    position: relative;
    top: 0;
    left: 0;
    bottom: 0;
    background: var(--primary-color);
    width: 80px;
    min-height: 100vh;
    transition: all 0.5s ease;
    overflow-x: hidden;

    &.active {
        width: 300px;
    }

    .logo {
        width: 100%;
        img {
            padding: 1rem 0;
            width: 80px;
            display: block;
            margin: 0 auto !important;
            transition: all 0.2s ease;
        }
    }

    .links {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        padding-left: 1rem;
        padding-top: 10rem;

        .link {
            position: relative;
            list-style: none;
            width: 100%;
            border-top-left-radius: 20px;
            border-bottom-left-radius: 20px;

            &.active {
                background: #fff;

                a {
                    color: var(--primary-color);
                    font-weight: 600;
                }
            }

            a {
                position: relative;
                display: block;
                width: 100%;
                display: flex;
                text-decoration: none;
                color: #fff;
                font-size: 16px;
                font-weight: 500;

                .icon {
                    position: relative;
                    display: block;
                    min-width: 60px;
                    height: 60px;
                    line-height: 60px;
                    text-align: center;

                    i {
                        font-size: 1.5rem;
                    }
                }

                .title {
                    position: relative;
                    display: block;
                    padding-left: 10px;
                    height: 60px;
                    line-height: 60px;
                    white-space: normal;
                }
            }
        }
    }

    .toggle-arrow {
        position: absolute;
        right: 20px;
        bottom: 20px;
        font-size: 2rem;
        color: #fff;
        cursor: pointer;
        transition: all 0.4s ease-in-out;

        &.active {
            transform: rotate(-180deg);
        }
    }
}
</style>
