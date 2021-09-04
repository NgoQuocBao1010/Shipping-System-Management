<template>
    <div class="order-detail">
        <div class="order-detail__header">
            <h1 class="title">
                Order #{{ id }}
                <span
                    class="status"
                    :class="'order-' + statusCodes[order.status]"
                    >{{ statusCodes[order.status] }}</span
                >
            </h1>
            <div class="date">Order Date: {{ order.date }}</div>
        </div>
        <div class="order-detail__content">
            <div class="info">
                <div class="info__title">Consignor Address</div>
                <div class="info__detail">
                    <div class="name">{{ order.consignor }}</div>
                    <div class="address">
                        Address: {{ order.placeOfReceipt }}
                    </div>
                    <div class="phone">
                        Phone Number: {{ order.consignorPhone }}
                    </div>
                </div>
            </div>
            <div class="info">
                <div class="info__title">Consignee Address</div>
                <div class="info__detail">
                    <div class="name">{{ order.consignee }}</div>
                    <div class="normal">
                        Address: {{ order.placeOfDelivery }}
                    </div>
                    <div class="normal">
                        Phone Number: {{ order.consigneePhone }}
                    </div>
                </div>
            </div>
            <div class="info">
                <div class="info__title">Other Information</div>
                <div class="info__detail">
                    <div class="normal">
                        Payment Method: {{ order.paymentMethod }}
                    </div>
                    <div class="normal">Shipper: {{ order.shipper }}</div>
                    <div class="normal">Shipping Method: Ordinary</div>
                    <div class="price-tag">
                        Price: <span class="price">5.000.000 VND</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapState } from "vuex";

export default {
    name: "OrderDetail",
    data() {
        return {
            order: null,
            statusCodes: {
                0: "failed",
                1: "delivered",
                2: "delivering",
                3: "processing",
            },
        };
    },
    props: {
        id: String | Number,
    },
    computed: {
        ...mapState(["orders"]),
    },
    method: {},
    created() {
        this.order = this.orders.find(
            (order) => order.id === Number.parseInt(this.id)
        );
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
