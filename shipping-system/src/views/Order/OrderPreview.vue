<template>
    <div class="wrapper">
        <h2>Order #{{ id }}</h2>
        <div class="preview">
            <p class="message">{{ statusMessage }}</p>
            <div class="message" v-if="order && order.shipperInfo">
                Shipper Informtion:
                <b>
                    {{ order.shipperInfo.fullName }} ({{
                        order.shipperInfo.email
                    }}) - {{ order.shipperInfo.phone }}
                </b>
            </div>
        </div>
        <!-- Order status -->
        <OrderStatus v-if="order" :status="order.status" />

        <div class="map-container" v-if="order && order.status === 2">
            <Map :order="order" />
        </div>
    </div>
</template>

<script>
import { RepositoryFactory } from "../../api/backend/Factory";
const OrderAPI = RepositoryFactory.get("order");

import Map from "@/components/Leaflet.vue";
import OrderStatus from "@/components/order/OrderStatus.vue";

const statusMessages = {
    1: "This order is processing! We will deliver soon!",
    2: "This order is delivering, check the map below for more information",
    3: "This order is already delivered",
    4: "This order is failed to delivered",
};

export default {
    name: "OrderPreview",
    components: {
        Map,
        OrderStatus,
    },
    data() {
        return {
            order: null,
        };
    },
    computed: {
        statusMessage() {
            return statusMessages[this.order?.status];
        },
    },
    props: {
        id: Number | String,
    },
    async created() {
        try {
            const { data } = await OrderAPI.getPreview(this.id);

            if (this.$store.getters.isAuthenticated) {
                this.$router.push({
                    name: "OrderDetail",
                    params: { id: this.id },
                });
            }

            this.order = data;
        } catch (e) {
            console.log(e);
            if (e.response?.status === 404) {
                this.$router.push({ name: "NotFoundError" });
            }
        }
    },
};
</script>

<style lang="scss" scoped>
.wrapper {
    .preview {
        .message {
            font-weight: 600;
            margin: 1rem 0;
        }
    }
    .map-container {
        margin: 2rem 0;
    }
}
</style>
