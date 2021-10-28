<template>
    <div class="wrapper">
        <!-- Tab navigation -->
        <ul class="navigation">
            <li
                v-for="(tab, index) in tabs"
                :key="index"
                :class="{ active: index === selectedIndex }"
                @click="selectedIndex = index"
            >
                {{ tab.name }}
            </li>
        </ul>

        <!-- Order table -->
        <SelectTable
            :orders="orders"
            @assign="assignOrder"
            :remove="selectedIndex === 1"
        />

        <!-- Confirm password modal -->
        <Modal
            header="User Confirmation"
            size="small"
            :active="userConfirmation"
            @toggle="userConfirmation = false"
            submit="Confirm"
            @submit.prevent=""
        >
            <!-- Modal content -->
            <div class="content">
                <!-- Verify password form -->
                <form @submit.prevent="">
                    <div class="inputs">
                        <label for="password">
                            Enter your password for
                            <b>{{ $store.getters.email }}</b>
                        </label>
                        <input type="password" v-model="confirmPassword" />
                    </div>

                    <p class="error" v-show="passwordError">
                        {{ passwordError }}
                    </p>
                </form>

                <!-- Instruction -->
                <p>
                    *** Please enter your password to confirm this action. ***
                </p>
            </div>
        </Modal>
    </div>
</template>

<script>
import axios from "axios";

import SelectTable from "./SelectTable.vue";
import Modal from "../Modal.vue";

export default {
    name: "DriverOrder",
    components: {
        SelectTable,
        Modal,
    },
    props: {
        token: String,
        profile: Object,
    },
    data() {
        return {
            tabs: [
                {
                    name: "Assigned Order",
                    query: "status=1",
                },
                {
                    name: "Status",
                    query: `status=2&shipper=${this.profile.id}`,
                },
                {
                    name: "History",
                    query: `status=3&shipper=${this.profile.id}`,
                },
            ],
            selectedIndex: 0,

            orders: [],
            assignedOrder: null,

            // Modal
            userConfirmation: false,
            confirmPassword: "",
            passwordError: null,
            verifyToken: null,
        };
    },
    watch: {
        async selectedIndex() {
            await this.getOrderList();
        },
    },
    methods: {
        async getOrderList() {
            /* Get list of order depends on chosen category */
            const query = this.tabs[this.selectedIndex].query;

            try {
                const url = `http://127.0.0.1:8000/order/list/?${query}`;
                const response = await axios.get(url, {
                    headers: {
                        Authorization: `Token ${this.token}`,
                    },
                });

                // console.log(response.data);
                this.orders = response.data;
            } catch (e) {
                console.log(e);
            }
        },
        async assignOrder(chosenOrders) {
            /* Assign chosen order to driver */
            try {
                const data = {
                    driverId: this.profile.id,
                    orders: chosenOrders,
                };

                const url = `http://127.0.0.1:8000/order/assign/`;
                const response = await axios.post(url, data, {
                    headers: {
                        Authorization: `Token ${this.token}`,
                    },
                });

                console.log(response.data);
            } catch (e) {
                console.log(e);
            }
        },
    },
    async created() {
        await this.getOrderList();
    },
};
</script>

<style lang="scss" scoped>
.wrapper {
    .navigation {
        margin-bottom: 1rem;
        display: flex;
        gap: 2rem;

        li {
            list-style: none;
            padding: 5px 8px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;

            &.active {
                border-bottom: 2px solid var(--primary-color);
            }
        }
    }

    .inputs {
        width: 100%;
        display: flex;
        flex-direction: column;
        margin: 1rem 0;

        label {
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 5px;
            color: var(--primary-color);
        }

        input {
            font-size: 1.4rem;
            font-weight: 500;
            padding: 8px 12px;
            border: 2px solid rgb(138, 135, 135);

            &:focus {
                border: none;
                outline: none;
                border: 2px solid var(--primary-color);
            }
        }
    }

    .error {
        width: max-content;
        color: red;
        font-weight: 600;
        font-style: normal;
        cursor: initial;
    }

    .content {
        width: 100%;
        margin: 2rem 0;

        p {
            font-style: italic;
        }
    }
}
</style>
