<template>
    <div class="wrapper">
        <p class="status" v-if="ordersInDeliver">
            Delivering <span>{{ ordersInDeliver }}</span> orders
        </p>
        <p class="status" v-else>No orders are delivering at the moment</p>

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
            :remove="selectedIndex === 0"
        />
    </div>
</template>

<script>
import axios from "axios";

import { RepositoryFactory } from "@/api/backend/Factory";
const OrderAPI = RepositoryFactory.get("order");

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
                    name: "Order Delivering",
                    query: { status: 2, shipper: this.profile.id },
                },
                {
                    name: "Processing Order",
                    query: { status: 1 },
                },
                {
                    name: "History",
                    query: { status: 3, shipper: this.profile.id },
                },
            ],
            selectedIndex: 0,

            orders: [],
            ordersInDeliver: 0,
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
                const { data } = await OrderAPI.getListAsAdmin(query);
                this.orders = data;

                if (this.selectedIndex === 0)
                    this.ordersInDeliver = data.length;
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

                await OrderAPI.assignOrders(data);

                this.$toast.success("Assign Completed!!!");
                this.selectedIndex = 0;
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

                await OrderAPI.unassignOrders(data);

                this.$toast.success("Unassign Completed!!!");
                this.selectedIndex = 1;
                this.ordersInDeliver =
                    this.ordersInDeliver - chosenOrders.length;
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
    .status {
        font-size: 1.4rem;
        font-weight: 600;
        margin-bottom: 2rem;

        span {
            color: var(--primary-color);
            font-weight: bold;
        }
    }

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
