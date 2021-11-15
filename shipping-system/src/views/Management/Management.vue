<template>
    <div class="management">
        <div class="management__header">
            <h1 class="title">Human Resources Management</h1>
            <div class="btn-header">
                <router-link class="btn" :to="{ name: 'DriverAdministrator' }">
                    <i class="fas fa-plus-circle"></i>Driver
                </router-link>
            </div>
        </div>

        <!-- Content -->
        <div class="management__content">
            <div class="navigation">
                <div
                    class="category"
                    v-for="(category, index) in categories"
                    :key="index"
                    :class="{ active: index === selectedIndex }"
                    @click="changeCategory(index)"
                >
                    {{ category }}
                </div>
            </div>

            <!-- Display all profile list -->
            <div class="content">
                <component
                    v-if="profileList"
                    :is="displayComp"
                    :profileList="profileList"
                />
            </div>
        </div>
    </div>
</template>

<script>
import { mapState } from "vuex";

import { RepositoryFactory } from "../../api/backend/Factory";
const AccountAPI = RepositoryFactory.get("account");

import CardWrapper from "@/components/management/CardWrapper.vue";
import CustomerTable from "@/components/management/CustomerTable.vue";
import LoadingAnimation from "../../components/CircleAnimation.vue";

export default {
    name: "Management",
    components: {
        LoadingAnimation,
        CustomerTable,
        CardWrapper,
    },
    data() {
        return {
            categories: ["Employee", "Consignor", "Consignee"],
            selectedIndex: 0,
            profileList: null,
        };
    },
    computed: {
        ...mapState(["token"]),
        displayComp() {
            return this.categories[this.selectedIndex] === "Employee"
                ? "CardWrapper"
                : "CustomerTable";
        },
    },
    methods: {
        async changeCategory(index) {
            /* Change category */
            this.selectedIndex = index;
            this.profileList = null;

            await this.queryProfile();
        },
        async queryProfile() {
            /* Call backend API for profile base on role */
            try {
                const role = this.categories[this.selectedIndex];

                const { data } = await AccountAPI.queryProfile({ role });

                this.profileList = data;
            } catch (e) {
                console.log(`[Management Page Error]: ${e}`);
            }
        },
    },
    async created() {
        await this.queryProfile();
    },
};
</script>

<style lang="scss" scoped>
.management {
    &__header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 0.8rem;

        .title {
            font-size: 1.5rem;
        }

        .btn-header {
            .btn,
            button {
                padding-left: 1rem;
                padding-right: 1rem;
                margin: 0 0.5rem;
                border-radius: 10px;

                i {
                    margin-right: 0.5rem;
                }
            }
        }
    }

    &__content {
        padding: 2rem 0;

        .navigation {
            max-width: max-content;
            display: flex;
            border-radius: 10000px;

            .category {
                padding: 5px 10px;
                font-size: 1.2rem;
                font-weight: 500;
                border-bottom: 2px solid #fff;
                cursor: pointer;
                transition: all 0.2s ease-in;

                &.active {
                    border-bottom: 2px solid var(--primary-color);
                    background: rgb(202, 221, 228);
                }
            }
        }

        .content {
            margin-top: 1rem;
            padding: 20px;
            border-radius: 15px;
            box-shadow: rgba(14, 30, 37, 0.12) 0px 2px 4px 0px,
                rgba(14, 30, 37, 0.32) 0px 2px 16px 0px;

            display: flex;
            justify-content: center;
            align-items: center;
        }
    }
}
</style>
