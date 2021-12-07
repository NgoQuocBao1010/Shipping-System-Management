<template>
    <div class="order-container">
        <!-- Order Id -->
        <div class="order-container__header">
            <h1 class="title" v-if="order.id">
                Order <span class="order-id">#{{ order.id }}</span>
                <i class="far fa-copy" @click="generatePreviewLink"></i>
                <span class="status" :class="'order-' + statusCodes[order.status]">
                    {{ statusCodes[order.status] }}
                </span>
            </h1>

            <!-- Edit Button -->
            <router-link
                v-if="$store.getters.isAdmin && order.id"
                :to="{
                    name: 'OrderEdit',
                    params: { id: order.id, orderInstance: order },
                }"
                class="btn small"
            >
                <i class="fas fa-edit"></i>Edit
            </router-link>
        </div>

        <!-- Order Information -->
        <div class="order-container__content">
            <!-- Customer Section -->
            <div class="customer">
                <!-- Consignor -->
                <div class="customer__info">
                    <div class="info__title">Consignor Address</div>
                    <div class="info__detail">
                        <div class="name">
                            {{ order.consignor.fullName }}
                        </div>
                        <div class="phone">
                            <b>{{ order.consignor.phone }}</b>
                        </div>
                        <div class="address">
                            {{ order.consignor.address }}
                        </div>
                        <div class="address">
                            {{ consignorWard }},
                            {{ $store.getters.district(order.consignor.districtId).name }}
                        </div>
                    </div>
                </div>

                <!-- Consignee -->
                <div class="customer__info">
                    <div class="info__title">Consignee Address</div>
                    <div class="info__detail">
                        <div class="name">{{ order.consignee.fullName }}</div>
                        <div class="normal">
                            <b>{{ order.consignee.phone }}</b>
                        </div>
                        <div class="address">
                            {{ order.consignee.address }}
                        </div>
                        <div class="address">
                            {{ consigneeWard }},
                            {{ $store.getters.district(order.consignee.districtId).name }}
                        </div>
                    </div>
                </div>
            </div>

            <!-- Order status -->
            <OrderStatus v-if="order.id" :status="order.status" />

            <!-- Other Information -->
            <div class="info">
                <div class="info__title">Other Information</div>
                <div class="info__detail">
                    <!-- Status -->
                    <div class="normal" v-if="order.id">
                        Status: <b>{{ statusCodes[order.status] }}</b>
                    </div>

                    <!-- Status -->
                    <div class="normal">
                        Note: <b>{{ order.note || "No note" }}</b>
                    </div>

                    <!-- Distance -->
                    <div class="normal" v-if="order.id">
                        Estimate distance:
                        <b>{{ displayDistance(order.estimateDistance) }}</b>
                    </div>

                    <div class="normal" v-if="!order.id && distance">
                        Estimate distance: <b>{{ displayDistance(distance) }}</b>
                    </div>

                    <!-- Delivery time -->
                    <div class="normal" v-if="order.id && order.status === 2">
                        Estimate Deliver time: <b>Around {{ estimatedTime }}</b>
                    </div>

                    <!-- Date created -->
                    <div class="normal" v-if="order.id">
                        Date Created: <b>{{ order.dateCreated }}</b>
                    </div>
                    <div class="normal" v-else>
                        Date Created: <b>{{ today }}</b>
                    </div>

                    <!-- Payment method -->
                    <div class="normal">
                        Payment Method: <b>{{ payment }}</b>
                    </div>

                    <!-- Shipper information -->
                    <div
                        class="normal"
                        v-if="order.shipperInfo"
                        style="text-transform: initial"
                    >
                        Shipper Informtion:
                        <b>
                            {{ order.shipperInfo.fullName }} ({{
                                order.shipperInfo.email
                            }}) - {{ order.shipperInfo.phone }}
                        </b>
                    </div>

                    <!-- Preview -->
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
                        <div>{{ $func.formatMoneyToVND(product.price) }} VND</div>
                    </div>
                </div>
            </div>

            <!-- Pricing Section -->
            <div class="pricing">
                <div class="title">Total Expense</div>
                <div class="pricing__details">
                    <p>
                        Package's price:
                        <span class="money">
                            {{ this.$func.formatMoneyToVND(packagePrice) }} VND
                        </span>
                    </p>
                    <p>
                        Shipping price:
                        <span class="money">
                            {{ this.$func.formatMoneyToVND(order.shippingPrice) }}
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

import OrderStatus from "@/components/order/OrderStatus.vue";

export default {
    name: "OrderDetail",
    components: {
        OrderStatus,
    },
    data() {
        return {
            statusCodes: {
                1: "processing",
                2: "delivering",
                3: "delivered",
                4: "failed",
            },
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
        distance: {
            required: false,
            default: null,
        },
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
            this.order.products.forEach((item) => (total += parseFloat(item.price)));

            return total;
        },
        total() {
            return parseFloat(this.order.shippingPrice) + parseFloat(this.packagePrice);
        },
        estimatedTime() {
            let timeUnit = "days";
            let time = Math.floor((this.order.deliverTime / 3600) * 24);

            if (this.order.deliverTime < 3600) {
                timeUnit = "minutes";
                time = Math.floor(this.order.deliverTime / 60);
            } else if (
                this.order.deliverTime > 3600 &&
                this.order.deliverTime < 3600 * 24
            ) {
                timeUnit = "hours";
                time = Math.floor(this.order.deliverTime / 3600);
            }

            return `${time} ${timeUnit}`;
        },
    },
    methods: {
        generatePreviewLink() {
            const orderPreviewLink = document.createElement("a");
            orderPreviewLink.href = this.$router.resolve({
                name: "OrderPreview",
                params: { id: this.order.id },
            }).href;

            navigator.clipboard.writeText(orderPreviewLink.href);

            this.$toast.info("Copy to clipboard");
        },
        displayDistance(distance) {
            if (distance < 1000) return `${distance} m`;
            else {
                let newDistance = Math.floor(distance / 1000);

                return `Around ${newDistance} km`;
            }
        },
    },
    async created() {
        const wardObj = await this.$province.getWard(this.order.consignor.wardId);
        const wardObj2 = await this.$province.getWard(this.order.consignee.wardId);
        this.consignorWard = wardObj.name;
        this.consigneeWard = wardObj2.name;
    },
};
</script>

<style lang="scss" scoped>
.order-container {
    &__header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 2rem;

        .title {
            font-size: 2rem;
            display: flex;
            align-items: center;

            .order-id {
                color: var(--primary-color);
                margin: 0 10px;
            }

            i {
                font-size: 1.2rem;
                padding: 1rem;
                color: rgb(109, 106, 106);
                cursor: pointer;
            }

            .status {
                text-transform: capitalize;
                font-size: 12px;
            }
        }

        a {
            padding: 0.5rem 1rem;
            font-size: 1rem;

            i {
                font-size: 1rem;
            }
        }
    }

    &__content {
        display: flex;
        flex-direction: column;
        margin-bottom: 2rem;

        .customer {
            display: flex;
            justify-content: space-between;
            gap: 20px;
            width: 100%;
            margin-bottom: 2.5rem;

            > * {
                flex: 1 1 40%;
            }

            .address {
                font-weight: 600;
            }
        }

        .info {
            margin: 1rem 0;
            font-weight: 500;

            &__title {
                margin-bottom: 5px;
                font-weight: 900;
                color: var(--primary-color);
            }

            &__detail {
                height: 100%;
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
                    margin-bottom: 0.8rem;
                }
            }
        }

        .products-container {
            margin-bottom: 1rem;
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
                        color: white;
                        background: var(--secondary-color);
                        margin-bottom: 1rem;
                        border: none;
                    }

                    > * {
                        flex: 1;
                        font-weight: 600;
                        font-size: 1.2rem;
                        padding: 4px 10px;
                        margin-bottom: 0.5rem;
                        border-bottom: 1px solid black;
                    }
                }
            }
        }

        .pricing {
            display: flex;

            > * {
                flex: 1 1 50%;
            }
            .title {
                margin-bottom: 5px;
                font-weight: 900;
                font-size: 1.5rem;
                color: var(--primary-color);
            }

            &__details {
                padding: 0.5rem 0;
                text-align: right;

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
