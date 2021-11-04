<template>
    <div class="sidebar-container" :class="{ active: expand }">
        <ul class="links">
            <li
                v-for="(page, index) in pages"
                :key="index"
                class="link"
                :class="{ active: page.name === currentRoute }"
                v-show="(page.staffMember && isStaff) || !page.staffMember"
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
                    name: "Orders",
                    iconClass: "fas fa-box-open",
                    staffMember: false,
                },
                {
                    name: "Reports",
                    iconClass: "fas fa-clipboard-list",
                    staffMember: true,
                },
                {
                    name: "Management",
                    iconClass: "fas fa-users",
                    staffMember: true,
                },
                {
                    name: "PriceShipping",
                    iconClass: "fas fa-info-circle",
                    staffMember: false,
                },
            ],
            expand: false,
        };
    },
    computed: {
        currentRoute() {
            return this.$route.name;
        },
        isAdmin() {
            return this.$store.getters.isAdmin;
        },
        isStaff() {
            return this.$store.getters.isStaff;
        },
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
        width: 15rem;
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
        padding-left: 0.5rem;

        @media only screen and (min-width: 1200px) {
            padding-left: 1rem;
        }
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
                font-size: 14px;
                @media only screen and (min-width: 1200px) {
                    font-size: 1rem;
                }
                font-weight: 500;

                .icon {
                    position: relative;
                    display: block;
                    min-width: 60px;
                    height: 60px;
                    line-height: 60px;
                    text-align: center;

                    i {
                        font-size: 1.2rem;

                        @media only screen and (min-width: 1200px) {
                            font-size: 1.5rem;
                        }
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
        font-size: 1.2rem;
        color: #fff;
        cursor: pointer;
        transition: all 0.4s ease-in-out;

        &.active {
            transform: rotate(-180deg);
        }
    }
}
</style>
