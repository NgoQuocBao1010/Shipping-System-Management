<template>
    <div class="wrapper">
        <!-- Profile -->
        <div class="profile">
            <q-icon name="person"></q-icon>
            <div class="information">
                <p>Full name: {{ user.fullName }}</p>
                <p>Phone Number: {{ user.phone }}</p>
                <p>Driver License: {{ user.driverLicense }}</p>
                <p>Delivering Orders: {{ delveringOrders.length }}</p>
            </div>
        </div>

        <!-- Orders -->
        <div class="orders-container" v-if="orders">
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

                <span class="refresh" @click="getOrderList">
                    <q-icon name="refresh"></q-icon>
                </span>
            </ul>

            <OrderTable
                :orders="orders"
                :history="selectedIndex !== 0"
                @done="getOrderList"
            />

            <button
                v-if="orders.length > 0 && selectedIndex === 0"
                class="small"
                @click="confirmUpdateLocation"
            >
                Update Your Location
            </button>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import { mapState } from "vuex";

import OrderTable from "../components/OrderTable.vue";

export default {
    name: "PageIndex",
    components: {
        OrderTable,
    },
    data: () => ({
        orders: null,
        delveringOrders: 0,
        tabs: [
            {
                name: "Delivering",
                query: { status: 2 },
            },
            {
                name: "History",
                query: { status: 3 },
            },
        ],
        selectedIndex: 0,

        // location
        latitude: null,
        longitude: null,
        error: {
            message: null,
            code: null,
        },
    }),
    computed: {
        ...mapState(["user", "token"]),
    },
    watch: {
        async selectedIndex() {
            this.orders = [];
            await this.getOrderList();
        },
    },
    methods: {
        async getOrderList() {
            /* Get list of order depends on chosen category */
            const { status } = this.tabs[this.selectedIndex].query;
            const url = `https://10.0.2.2:8000/order/list/?status=${status}&shipper=${this.user.id}`;

            try {
                const { data } = await axios.get(url, {
                    headers: {
                        Authorization: `Token ${this.token}`,
                    },
                });
                this.orders = data;

                if (this.selectedIndex === 0) {
                    this.delveringOrders = this.orders.map((order) => order.id);
                }
            } catch (e) {
                console.log(e);
            }
        },
        confirmUpdateLocation() {
            this.$q.notify({
                message: "Are you sure to update your location?",
                color: "primary",
                actions: [
                    {
                        label: "Update",
                        color: "yellow",
                        handler: () => {
                            this.getCurrentPos();
                        },
                    },
                    {
                        label: "Dismiss",
                        color: "white",
                        handler: () => {
                            /* ... */
                        },
                    },
                ],
                timeout: 1500,
            });
        },
        getCurrentPos() {
            const result = navigator.geolocation.getCurrentPosition(
                (position) => {
                    const { latitude, longitude } = position.coords;
                    const data = JSON.stringify({
                        lat: latitude,
                        lon: longitude,
                    });

                    for (let i = 0; i < this.delveringOrders.length; i++) {
                        const orderId = this.delveringOrders[i];
                        this.updateLocation(orderId, data);
                    }
                },
                (error) => {
                    if (error) {
                        this.error = error;
                        console.log(error);
                        this.$q.notify({
                            type: "negative",
                            message: `An error has occured while trying to update your position`,
                            position: "bottom",
                            timeout: 1000,
                        });
                    }
                },
                {
                    enableHighAccuracy: true,
                    maximumAge: 3600000,
                }
            );
        },
        async updateLocation(orderId, data) {
            try {
                const url = `https://10.0.2.2:8000/order/location/${orderId}/`;

                const response = await axios.post(
                    url,
                    { location: data },
                    {
                        headers: {
                            Authorization: `Token ${this.token}`,
                        },
                    }
                );

                this.$q.notify({
                    type: "positive",
                    message: `Your location has been updated`,
                    position: "bottom",
                    timeout: 1000,
                });
            } catch (e) {
                console.log(e);
                this.$q.notify({
                    type: "negative",
                    message: `An error has occured while trying to update your position`,
                    position: "bottom",
                    timeout: 1000,
                });
            }
        },
    },
    async created() {
        await this.getOrderList();
    },
};
</script>

<style lang="scss" scoped>
p {
    margin: 0;
    padding: 0;
}

.profile {
    display: flex;
    justify-content: center;
    margin: 1rem;

    i {
        font-size: 3rem;
    }

    .information {
        margin: 0 1rem;

        p {
            margin-bottom: 1rem;
        }
    }
}

.orders-container {
    width: 90%;
    margin: 0 auto;
    margin-bottom: 2rem;

    .navigation {
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 2rem;
        position: relative;

        li {
            list-style: none;
            padding: 5px 8px;
            font-size: 12px;
            font-weight: 600;
            cursor: pointer;

            &.active {
                border-bottom: 2px solid var(--primary-color);
            }
        }

        .refresh {
            position: absolute;
            right: 0;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            background: var(--primary-color);
            color: #fff;
            font-weight: bold;
        }
    }

    button {
        display: block;
        margin: 0 auto;
        margin-top: 1rem;
    }
}
</style>
