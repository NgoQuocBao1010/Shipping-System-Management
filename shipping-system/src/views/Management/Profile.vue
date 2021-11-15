<template>
    <div class="profile">
        <!-- Headers -->
        <div class="profile__header">
            <h1 class="title">
                {{ email }}
                <span class="role color" :class="role" style="text-transform: capitalize">
                    {{ role }}
                </span>
                <button class="small" @click="signOut" v-if="isCurrentUser">
                    <i class="fas fa-sign-out-alt"></i>Logout
                </button>
            </h1>
        </div>

        <!-- Main content -->
        <div class="profile__content">
            <TabWrapper :preferredTab="tab">
                <!-- Edit Profile form -->
                <Tab title="Profile">
                    <div class="form-container">
                        <form class="profile__content">
                            <!-- Name -->
                            <div class="input">
                                <label for="name">Full Name: </label>
                                <input
                                    :class="{ active: edit }"
                                    name="name"
                                    type="text"
                                    v-model="profile.fullName"
                                    :readonly="!edit"
                                    required
                                />
                            </div>

                            <!-- Email -->
                            <div class="input">
                                <label for="email">Email: </label>
                                <input
                                    name="email"
                                    type="email"
                                    v-model="profile.email"
                                    readonly="true"
                                    required
                                />
                            </div>

                            <!-- Driver License -->
                            <div class="input" v-if="profile.driverLicense">
                                <label for="license">Driver License: </label>
                                <input
                                    name="driverLicense"
                                    type="text"
                                    v-model="profile.driverLicense"
                                    :readonly="!edit"
                                    required
                                />
                            </div>

                            <!-- Phone Number -->
                            <div class="input">
                                <label for="phone">Phone Number: </label>
                                <input
                                    :class="{ active: edit }"
                                    name="phone"
                                    type="text"
                                    v-model="profile.phone"
                                    :readonly="!edit"
                                    required
                                />
                            </div>

                            <!-- Date of birth -->
                            <div class="input">
                                <label for="dob">Date of birth: </label>
                                <input
                                    name="dob"
                                    type="date"
                                    v-model="profile.dateOfBirth"
                                    :readonly="!edit"
                                    :class="{ active: edit }"
                                />
                            </div>

                            <!-- Address -->
                            <div class="input">
                                <label for="address">Address: </label>
                                <input
                                    :class="{ active: edit }"
                                    name="address"
                                    v-model="profile.address"
                                    type="text"
                                    :readonly="!edit"
                                />
                            </div>

                            <!-- Ward -->
                            <div class="input">
                                <label for="subdistrict">Ward</label>
                                <div class="select" :class="{ active: edit }">
                                    <i class="fas fa-chevron-down"></i>
                                    <select
                                        name="subdistrict"
                                        v-model="profile.wardId"
                                        :disabled="!edit"
                                    >
                                        <option
                                            v-for="ward in wards"
                                            :key="ward.id"
                                            :value="ward.id"
                                        >
                                            {{ ward.name }}
                                        </option>
                                    </select>
                                </div>
                            </div>

                            <!-- District -->
                            <div class="input">
                                <label for="province">District - City</label>
                                <div class="select" :class="{ active: edit }">
                                    <i class="fas fa-chevron-down"></i>
                                    <select
                                        name="province"
                                        v-model="profile.districtId"
                                        :disabled="!edit"
                                    >
                                        <option
                                            v-for="dstr in provinces"
                                            :key="dstr.id"
                                            :value="dstr.id"
                                        >
                                            {{ dstr.name }}
                                        </option>
                                    </select>
                                </div>
                            </div>

                            <!-- Error for validations -->
                            <p class="error" v-show="error">
                                <i class="fas fa-exclamation-circle"></i> Please fill out
                                all the input
                            </p>

                            <!-- Editing section -->
                            <CircleAnimation class="animation" v-show="loadingData" />
                            <div class="edit-buttons">
                                <div
                                    class="btn small"
                                    @click="edit = true"
                                    v-show="!edit && isCurrentUser"
                                >
                                    <i class="far fa-edit"></i>Edit
                                </div>
                                <div class="btn small editing" v-show="edit">
                                    <i class="far fa-edit"></i>Editing ...
                                </div>
                                <button
                                    class="btn small"
                                    type="submit"
                                    @click.prevent="updateProfile"
                                    v-show="edit"
                                >
                                    <i class="fas fa-save"></i>Save
                                </button>
                            </div>
                        </form>
                    </div>
                </Tab>

                <!-- Table of orders for each user -->
                <Tab title="Orders" iconClass="fas fa-box-open" v-if="role !== 'driver'">
                    <OrderTable :orders="orders" />
                </Tab>

                <!-- Driver navigation -->
                <!-- Assigned table orders -->
                <Tab title="Assign Order" iconClass="fas fa-plus-circle" v-else>
                    <DriverOrder :token="token" :profile="profile" />
                </Tab>
            </TabWrapper>
        </div>
    </div>
</template>

<script>
import { mapState, mapMutations } from "vuex";

import { RepositoryFactory } from "../../api/backend/Factory";
const AccountAPI = RepositoryFactory.get("account");
const OrderAPI = RepositoryFactory.get("order");

import TabWrapper from "@/components/profile/TabWrapper.vue";
import Tab from "@/components/profile/Tab.vue";
import OrderTable from "@/components/order/OrderTable.vue";
import DriverOrder from "@/components/order/DriverOrder.vue";
import CircleAnimation from "@/components/CircleAnimation.vue";

export default {
    name: "Profile",
    components: {
        CircleAnimation,
        OrderTable,
        DriverOrder,
        Tab,
        TabWrapper,
    },
    props: {
        email: String,
    },
    data() {
        return {
            profile: {
                fullName: null,
                email: "",
                dateOfBirth: "",
                phone: "",
                address: "",
                provinceId: null,
                districtId: null,
                wardId: null,
            },
            loadingData: false,
            edit: false,

            error: false,
            districts: [],
            wards: [],

            orders: [],
        };
    },
    computed: {
        ...mapState(["user", "token", "provinces"]),
        isCurrentUser() {
            return this.email === this.$store.getters.email;
        },
        tab() {
            let chosenTab = this.$route.query.tab;
            chosenTab = /^-?\d+$/.test(chosenTab) ? chosenTab : 0;

            return parseInt(chosenTab);
        },
        role() {
            if (this.profile.isAdmin) return "manager";
            if (this.profile.isStaff) return "driver";
            else return "customer";
        },
    },
    watch: {
        async "profile.districtId"(newVal, oldVal) {
            if (newVal) {
                this.loadingData = true;

                this.profile.wardId = oldVal ? null : this.profile.wardId;
                this.wards = await this.$province.getWardList(newVal);

                this.loadingData = false;
            }
        },
    },
    methods: {
        ...mapMutations(["logout", "updateProfile"]),
        async getProfile() {
            /*
                Get the user profile
                If it is the current user own profile, return the global user store
                else the user can only make API call to get other's profile only when he/she is the admin 
            */
            if (this.isCurrentUser) this.profile = this.user;
            else {
                if (!this.$store.getters.isAdmin)
                    return this.$router.push({ name: "Unauthorized" });

                try {
                    this.loadingData = true;
                    const { data } = await AccountAPI.get(this.email);
                    this.profile = data;
                } catch (e) {
                    if (e.response.status === 404) {
                        this.$router.push({ name: "NotFoundError" });
                    }
                }
            }

            if (this.role !== "driver") await this.getOrderList();
        },
        async getOrderList() {
            /* Call backend API to retrieve list of all orders */
            try {
                const { data } = await OrderAPI.getListAsAdmin({
                    profileId: this.profile.id,
                });

                this.orders = data;
            } catch (e) {
                console.log(e);
                if (e.response.status === 400) {
                    this.orders = [];
                    this.$toast.error(
                        "An error has occured while retriving orders! Please try again later!",
                        {
                            duration: 3000,
                        }
                    );
                }
            }
        },
        signOut() {
            this.logout();
            this.$router.push({ name: "Home" });
            this.$toast.info("You are just logged out of your account!", {
                duration: 2000,
            });
        },
        async updateProfile() {
            /* Make API call to update profile */
            try {
                this.loadingData = true;
                await AccountAPI.update(this.profile);
                this.edit = false;
                this.error = false;
                this.loadingData = false;
                this.$toast.success("Your profile has been updated!", {
                    duration: 2000,
                });
            } catch (e) {
                console.log(e);
            }
        },
    },
    async created() {
        this.loadingData = true;
        await this.getProfile();
        this.districts = this.provinces;

        if (this.profile.districtId) {
            this.wards = await this.$province.getWardList(this.profile.districtId);
        }

        this.loadingData = false;
    },
};
</script>

<style lang="scss" scoped>
.profile {
    &__header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 0.8rem;
        position: relative;

        button {
            background: rgb(223, 71, 71);
            font-weight: 600;
            position: absolute;
            right: 10px;
        }

        .title {
            font-size: 1.5rem;
            display: flex;
            align-items: center;
            gap: 3rem;
        }
    }

    &__content {
        width: 100%;
        margin-top: 2rem;
    }

    .form-container {
        padding: 0 2rem;
        padding-bottom: 1rem;
        display: flex;
        flex-direction: column;
        box-shadow: rgba(17, 17, 26, 0.05) 0px 1px 0px, rgba(17, 17, 26, 0.1) 0px 0px 8px;
        position: relative;

        .input {
            display: flex;
            align-items: center;

            label {
                margin-right: 2rem;
                width: 200px;
            }

            input {
                flex: 1 1 300px;
                max-width: 400px;
                line-height: 2;
                padding: 0 5px;
                margin-bottom: 1rem;
                font-size: 1rem;
                font-weight: 600;
                border: none;
                border-bottom: 1px solid black;

                &:focus {
                    outline: none;
                }

                &.active,
                &.active:focus {
                    border: none;
                    outline: 2px solid black;
                }

                &[type="password"] {
                    letter-spacing: 3px;
                    font-size: 1.2rem;
                }
            }

            .select {
                padding: 8px 5px;
                width: 100%;
                margin-bottom: 1rem;
                max-width: 400px;
                font-size: var(--input-font-size);
                font-weight: 600;
                line-height: 1.2rem;
                outline: none;
                border-bottom: 1px solid black !important;
                position: relative;

                &:focus {
                    border: 1px solid black !important;
                    outline: none;
                }

                i {
                    position: absolute;
                    cursor: pointer;
                    right: 10px;
                    top: 50%;
                    transform: translateY(-50%);
                    z-index: -1;
                    opacity: 0;
                }

                select {
                    cursor: initial;
                    width: 100%;
                    font-size: var(--input-font-size);
                    font-weight: 600;
                    line-height: 1.2rem;
                    background: transparent;

                    &:disabled {
                        opacity: 1;
                        color: black;
                    }
                }

                &.active {
                    border-bottom: none !important;
                    border: 2px solid black !important;

                    i {
                        opacity: 1;
                    }

                    select {
                        cursor: pointer;
                    }
                }
            }
        }

        .edit-buttons {
            position: absolute;
            top: 60px;
            right: 20px;
            display: flex;
            flex-direction: column;

            > * {
                margin: 0.5rem 0;
                font-weight: bold;

                &.editing {
                    background: rgb(51, 187, 51);
                    cursor: initial;
                }
            }
        }

        .animation {
            position: absolute;
            top: 15px;
            right: 30px;
        }

        .error {
            color: red;
            font-size: 12px;
            font-weight: 600;
            position: absolute;
            bottom: 15px;
            left: 30px;
        }
    }
}
</style>
