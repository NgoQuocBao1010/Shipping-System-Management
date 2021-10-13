<template>
    <div class="order-detail">
        <div class="order-detail__header">
            <h1 class="title" v-if="order.id">
                Order #{{ id }}
                <span
                    class="status"
                    :class="'order-' + statusCodes[order.status]"
                >
                    {{ statusCodes[order.status] }}
                </span>
            </h1>
        </div>
        <div class="order-detail__content">
            <div class="customer">
                <div class="info">
                    <div class="info__title">Consignor Address</div>
                    <div class="info__detail">
                        <div class="name">{{ order.consignor.fullName }}</div>
                        <div class="phone">
                            Phone Number: {{ order.consignor.phone }}
                        </div>
                        <div class="address">
                            Address: {{ order.consignor.address }}
                        </div>
                    </div>
                </div>
                <div class="info">
                    <div class="info__title">Consignee Address</div>
                    <div class="info__detail">
                        <div class="name">{{ order.consignee.fullName }}</div>
                        <div class="normal">
                            Address: {{ order.consignee.address }}
                        </div>
                        <div class="normal">
                            Phone Number: {{ order.consignee.phone }}
                        </div>
                    </div>
                </div>
            </div>

            <div class="info">
                <div class="info__title">Other Information</div>
                <div class="info__detail">
                    <div class="normal">Date Created: {{ today }}</div>
                    <div class="normal">Shipping Type: {{ shippingType }}</div>
                    <div class="normal">Payment Method: {{ payment }}</div>
                    <div class="normal">{{ preview }}</div>
                </div>
            </div>

            <div class="products-container">
                <div class="title">Products</div>
                <div class="products">
                    <ul>
                        <li
                            v-for="(product, index) in order.products"
                            :key="index"
                        >
                            {{ product.name }}, {{ product.price }} VND
                        </li>
                    </ul>
                </div>
            </div>

            {{ order.price }}
        </div>
    </div>
</template>

<script>
import { mapState } from "vuex";
import moment from "moment";

export default {
    name: "OrderDetail",
    data() {
        return {
            statusCodes: {
                0: "failed",
                1: "delivered",
                2: "delivering",
                3: "processing",
            },
            paymentOptions: [
                {
                    id: 1,
                    name: "Pay by consignor",
                },
                {
                    id: 2,
                    name: "Pay by consignee",
                },
            ],
            paymentOptions: {
                1: "Pay by consignor",
                2: "Pay by consignee",
            },
            previewOptions: {
                1: "Customer does not allow to observe products",
                2: "Customer allows to oberseve products but not to try",
                3: "Customer allows to try products",
            },
            shippingOptions: {
                1: "Standard",
                2: "Advance",
            },
        };
    },
    props: {
        order: Object,
    },
    computed: {
        ...mapState(["orders"]),
        today() {
            return moment().format("DD-MM-YYYY");
        },
        payment() {
            return this.paymentOptions[this.order.info.paymentMethod];
        },
        preview() {
            return this.previewOptions[this.order.info.productPreview];
        },
        shippingType() {
            return this.shippingOptions[this.order.info.shippingType];
        },
    },
    method: {},
    created() {},
};
</script>

<style lang="scss" scoped>
.order-detail {
    &__header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 0.8rem;
        background: lightblue;

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
        display: flex;
        flex-direction: column;
        margin-bottom: 2rem;

        .customer {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            width: 100%;
            margin-bottom: 1rem;
        }
        .info {
            flex: 1 1 200px;
            margin: 1rem 0.5rem;

            font-weight: 500;

            &__title {
                margin-bottom: 5px;
                font-weight: 900;
                color: var(--primary-color);
            }

            &__detail {
                padding: 1rem;
                box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
                    rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
                text-transform: capitalize;

                .name {
                    font-weight: 800;
                    font-size: 1.2rem;
                    margin-bottom: 0.8rem;
                }
                > * {
                    margin-bottom: 0.5rem;
                }
            }
        }
        .products-container {
            margin: 0rem 0.5rem;
            .title {
                margin-bottom: 5px;
                font-weight: 900;
                color: var(--primary-color);
            }

            ul {
                padding: 1rem;
                box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
                    rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
                li {
                    list-style: none;
                }
            }
        }
    }
}
</style>
