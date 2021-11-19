<template>
    <div class="wrapper">
        <!-- Profile -->
        <div class="profile">
            <q-icon name="person"></q-icon>
            <div class="information">
                <p>Full name: {{ user.fullName }}</p>
                <p>Phone Number: {{ user.phone }}</p>
                <p>Driver License: {{ user.driverLicense }}</p>
                <p>Delivering Orders: {{ delveringOrders }}</p>
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
            </ul>

            <OrderTable :orders="orders" />

            <button class="small" @click="updateLocation">Update Your Location</button>
        </div>

        {{ latitude }} {{ longitude }}
        {{ error.message }}
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
                name: "Processing",
                query: { status: 1 },
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

                if (this.selectedIndex === 0) this.delveringOrders = data.length;
            } catch (e) {
                console.log(e);
            }
        },
        updateLocation() {
            var options = {
                enableHighAccuracy: true,
                maximumAge: 3600000,
            };
            const result = navigator.geolocation.getCurrentPosition(
                (position) => {
                    this.latitude = position.coords.latitude;
                    this.longitude = position.coords.longitude;
                },
                (error) => {
                    if (error) {
                        this.error = error;
                        console.log(error);
                    }
                },
                options
            );
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
        gap: 2rem;

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
    }

    button {
        display: block;
        margin: 0 auto;
        margin-top: 1rem;
    }
}
</style>
