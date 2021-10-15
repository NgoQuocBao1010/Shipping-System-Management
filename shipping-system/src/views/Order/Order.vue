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
    computed: {},
    methods: {
        async getOrder() {
            /* 
                Call backend API to retrieve order data that correspond to the query id
            */
            try {
                const url = `http://127.0.0.1:8000/order/${this.id}/`;
                const response = await axios.get(url);

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

        console.log(this.order);
    },
};
</script>

<style lang="scss" scoped>
.order-detail {
    @media only screen and (min-width: 1200px) {
        padding-left: 5rem;
        padding-right: 5rem;
    }

    &__header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 0.8rem;

        .title {
            font-size: 1.5rem;
            display: flex;
            align-items: center;
            gap: 5rem;

            .status {
                text-transform: capitalize;
                font-size: 12px;
            }
        }

        .date {
            font-weight: 600;
        }
    }

    &__content {
        padding: 2rem 0;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;

        .info {
            flex: 1 1 200px;
            max-width: 700px;

            margin: 2rem 0.5rem;

            font-weight: 500;

            &__title {
                margin-bottom: 1rem;
            }

            &__detail {
                min-height: 100%;
                padding: 0.4rem;
                box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
                    rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
                text-transform: capitalize;

                & > * {
                    margin-bottom: 0.4rem;
                }

                .name {
                    font-weight: 800;
                    font-size: 1.2rem;
                    margin-bottom: 0.5rem;
                }

                .price-tag {
                    margin-top: 2rem;
                    margin-bottom: 0;

                    .price {
                        font-weight: 800;
                        font-size: 1.2rem;
                        color: var(--primary-color);
                    }
                }
            }
        }
    }
}
</style>
