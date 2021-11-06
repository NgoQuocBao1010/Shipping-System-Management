<template>
    <div class="order-detail">
        <h1 v-if="error">{{ error }}</h1>
        <OrderDetail v-if="order" :order="order" />

        <div class="map-container" v-if="order && order.status === 2">
            <Map :order="order" />
        </div>
    </div>
</template>

<script>
import { mapState } from "vuex";

import { RepositoryFactory } from "@/api/backend/Factory";
const OrderAPI = RepositoryFactory.get("order");

import OrderDetail from "@/components/order/OrderDetail.vue";
import Map from "@/components/Leaflet.vue";

export default {
    name: "Order",
    components: {
        OrderDetail,
        Map,
    },
    data() {
        return {
            order: null,
            error: null,
        };
    },
    props: {
        id: String | Number,
    },
    computed: {
        ...mapState(["token"]),
    },
    methods: {
        async getOrder() {
            /* 
                Call backend API to retrieve order data that correspond to the query id
            */
            try {
                const { data } = await OrderAPI.get(this.id);
                this.order = data;
            } catch (e) {
                if (e.response.status === 404) {
                    this.error = "Not found";
                } else if (e.response.status === 401) {
                    this.$router.push({ name: "Unauthorized" });
                } else if (e.response.status === 500) {
                    this.$router.push({ name: "InternalError" });
                }

                console.log(e.response);
            }
        },
    },
    async created() {
        await this.getOrder();
    },
};
</script>

<style lang="scss" scoped>
.order-detail {
    @media only screen and (min-width: 1400px) {
        padding-left: 5rem;
        padding-right: 5rem;
    }

    .map-container {
        margin: 2rem 0;
    }
}
</style>
