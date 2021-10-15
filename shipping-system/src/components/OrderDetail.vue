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
                <!-- Consignor -->
                <div class="info">
                    <div class="info__title">Consignor Address</div>
                    <div class="info__detail">
                        <div class="name">{{ order.consignor.fullName }}</div>
                        <div class="phone">
                            <b>{{ order.consignor.phone }}</b>
                        </div>
                        <div class="address">
                            {{ order.consignor.address }}
                        </div>
                        <div class="address">
                            {{ consignorWard }},
                            {{
                                $store.getters.district(
                                    order.consignor.districtId
                                ).name
                            }}
                        </div>
                    </div>
                </div>
                <!-- Consignee -->
                <div class="info">
                    <div class="info__title">Consignee Address</div>
                    <div class="info__detail">
                        <div class="name">{{ order.consignee.fullName }}</div>
                        <div class="normal">
                            <b>{{ order.consignee.phone }}</b>
                        </div>
                        <div class="normal">
                            {{ order.consignee.address }}
                        </div>
                        <div class="normal">
                            {{ consigneeWard }},
                            {{
                                $store.getters.district(
                                    order.consignee.districtId
                                ).name
                            }}
                        </div>
                    </div>
                </div>
            </div>
            <!-- Other Information -->
            <div class="info">
                <div class="info__title">Other Information</div>
                <div class="info__detail">
                    <div class="normal">
                        Date Created: <b>{{ today }}</b>
                    </div>
                    <div class="normal">
                        Payment Method: <b>{{ payment }}</b>
                    </div>
                    <div class="normal" style="font-weight: bold">
                        {{ preview }}
                    </div>
                </div>
            </div>
            <!-- Package Information -->
            <div class="products-container">
                <div class="title">Products</div>
                <div class="products">
                    <div class="row">
                        <div class="header">Product Name</div>
                        <div class="header">Price</div>
                    </div>

                    <div
                        class="row"
                        v-for="(product, index) in order.products"
                        :key="index"
                    >
                        <div>{{ product.name }}</div>
                        <div>
                            {{ $func.formatMoneyToVND(product.price) }} VND
                        </div>
                    </div>
                </div>
            </div>
            <!-- Pricing Section -->
            <div class="pricing">
                <div class="title">Total Expense</div>
                <div class="pricing__details">
                    <p>
                        Packge's price:
                        <span class="money">
                            {{ this.$func.formatMoneyToVND(packagePrice) }} VND
                        </span>
                    </p>
                    <p>
                        Shipping price:
                        <span class="money">
                            {{
                                this.$func.formatMoneyToVND(order.shippingPrice)
                            }}
                            VND
                        </span>
                    </p>
                    <p class="total">
                        In total:
                        <span class="money total">
                            {{ this.$func.formatMoneyToVND(total) }}
                            VND
                        </span>
                    </p>
                </div>
            </div>
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
            consignorWard: null,
            consigneeWard: null,
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
            return this.paymentOptions[this.order.paymentMethod];
        },
        preview() {
            return this.previewOptions[this.order.productPreview];
        },
        shippingType() {
            return this.shippingOptions[this.order.shippingType];
        },
        packagePrice() {
            let total = 0;
            this.order.products.forEach(
                (item) => (total += parseFloat(item.price))
            );

            return total;
        },
        total() {
            return (
                parseFloat(this.order.shippingPrice) +
                parseFloat(this.packagePrice)
            );
        },
    },
    async created() {
        this.consignorWard = await this.$province.getWard(
            this.order.consignor.subDistrictId
        );
        this.consigneeWard = await this.$province.getWard(
            this.order.consignee.subDistrictId
        );

        this.consignorWard = this.consignorWard.name;
        this.consigneeWard = this.consigneeWard.name;
    },
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
            margin-bottom: 2rem;
            .title {
                margin-bottom: 5px;
                font-weight: 900;
                color: var(--primary-color);
            }

            .products {
                padding: 1rem;
                box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
                    rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;

                .row {
                    display: flex;
                    gap: 0.5rem;

                    .header {
                        font-size: 1rem;
                        font-weight: 900;
                        background: lightgray;
                        margin-bottom: 1rem;
                        border: none;
                    }

                    > * {
                        flex: 1;
                        font-weight: 500;
                        font-size: 1.1rem;
                        padding: 4px 10px;
                        margin-bottom: 0.5rem;
                        border-bottom: 1px solid black;
                    }
                }
            }
        }
        .pricing {
            .title {
                margin-bottom: 5px;
                font-weight: 900;
                color: var(--primary-color);
            }
            margin: 0rem 0.5rem;

            &__details {
                padding: 1rem 0;

                p {
                    font-size: 1.2rem;
                    margin-bottom: 6px;

                    .total,
                    &.total {
                        font-size: 1.3rem;
                        font-weight: 900;
                    }

                    .money {
                        margin: 0 1rem;
                        font-weight: 600;
                    }
                }
            }
        }
    }
}
</style>
