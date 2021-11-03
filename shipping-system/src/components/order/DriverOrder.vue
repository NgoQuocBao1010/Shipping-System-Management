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
        <component
            :is="table"
            :orders="orders"
            @assign="assignOrder"
            @remove="unassignOrder"
            :remove="selectedIndex === 1"
        />
    </div>
</template>

<script>
import axios from "axios";

import OrderTable from "./OrderTable.vue";
import SelectTable from "./SelectTable.vue";

export default {
    name: "DriverOrder",
    components: {
        SelectTable,
        OrderTable,
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
        };
    },
    computed: {
        table() {
            return this.selectedIndex === 2 ? "OrderTable" : "SelectTable";
        },
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

                if (response.status === 200) {
                    this.$toast.success("Completed!!!");
                    this.selectedIndex = 1;
                }
            } catch (e) {
                console.log(e);
            }
        },
        async unassignOrder(chosenOrders) {
            /* Unassigned certain orders from driver */
            try {
                const data = {
                    orders: chosenOrders,
                };

                const url = `http://127.0.0.1:8000/order/edit/`;
                const response = await axios.post(url, data, {
                    headers: {
                        Authorization: `Token ${this.token}`,
                    },
                });

                if (response.status === 200) {
                    this.$toast.success("Completed!!!");
                    this.selectedIndex = 0;
                }
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
