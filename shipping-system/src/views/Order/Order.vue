<template>
    <div class="order-detail">
        <h1 v-if="error">{{ error }}</h1>
        <OrderDetail v-if="order" :order="order" />
    </div>
</template>

<script>
import axios from "axios";
import { mapState } from "vuex";

import OrderDetail from "@/components/OrderDetail.vue";

export default {
    name: "Order",
    components: {
        OrderDetail,
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
                const url = `http://127.0.0.1:8000/order/detail/${this.id}/`;
                const response = await axios.get(url, {
                    headers: {
                        Authorization: `Token ${this.token}`,
                    },
                });

                this.order = response.data;
            } catch (e) {
                if (e.response.status === 404) {
                    this.error = "Not found";
                }
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
    @media only screen and (min-width: 1200px) {
        padding-left: 5rem;
        padding-right: 5rem;
    }
}
</style>
