<template>
    <div class="management">
        <div class="management__header">
            <h1 class="title">Human Resources Management</h1>
            <div class="btn-header">
                <button><i class="fas fa-plus-circle"></i>Add Employee</button>
                <button>Status</button>
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

            <div class="content">
                <!-- <LoadingAnimation v-if="!profileList" /> -->

                <transition name="fade">
                    <div class="profile-cards" v-if="profileList">
                        <EmployeeCard
                            v-for="profile in profileList"
                            :key="profile.id"
                            :profile="profile"
                        />

                        <EmployeeCard />
                        <EmployeeCard />
                        <EmployeeCard />
                        <EmployeeCard />
                    </div>
                </transition>
            </div>
        </div>
    </div>
</template>

<script>
import { mapState } from "vuex";
import axios from "axios";

import EmployeeCard from "@/components/management/EmployeeCard.vue";
import LoadingAnimation from "../../components/CircleAnimation.vue";

export default {
    name: "Management",
    components: {
        EmployeeCard,
        LoadingAnimation,
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
    },
    methods: {
        async changeCategory(index) {
            this.selectedIndex = index;
            this.profileList = null;

            await this.queryProfile();
        },
        async queryProfile() {
            /* Call backend API for profile base on role */
            try {
                const role = this.categories[this.selectedIndex];

                const url = `http://127.0.0.1:8000/account/staff?q=${role}`;
                const response = await axios.get(url, {
                    headers: {
                        Authorization: `Token ${this.token}`,
                    },
                });

                console.log(response.data);
                this.profileList = response.data;
            } catch (e) {
                console.log(e);
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

            .profile-cards {
                width: 100%;
                display: flex;
                flex-wrap: wrap;
                gap: 3rem;
            }
        }
    }
}
</style>
