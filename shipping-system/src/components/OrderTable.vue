<template>
    <div class="wrapper">
        <!-- Header -->
        <div class="header">
            <div class="column">Order ID</div>
            <div class="column">Order Date</div>
            <div class="column">User</div>
            <div class="column">Place of Delivery</div>
            <div class="column">Payment Method</div>
            <div class="column">Shipper</div>
            <div class="column">Status</div>
        </div>

        <!-- Contents -->
        <div class="content">
            <!-- No content -->
            <div v-if="orders.length === 0" class="row empty">
                There is no order yet
            </div>

            <!-- Main contents -->
            <div
                v-else
                class="row"
                v-for="order in orders"
                :key="order.id"
                @click="goToDetail(order.id)"
            >
                <div class="column">{{ order.id }}</div>
                <div class="column">{{ order.dateCreated }}</div>
                <div class="column">{{ order.consignor.email }}</div>
                <div class="column">
                    {{ order.consignee.address }},
                    {{
                        $store.getters.district(order.consignee.districtId).name
                    }}
                </div>
                <div class="column">
                    {{ paymentMethods[order.paymentMethod] }}
                </div>
                <div class="column">
                    {{ order.shipper || "No information" }}
                </div>
                <div class="column status">
                    <div :class="'order-' + statusCodes[order.status]">
                        {{ statusCodes[order.status] }}
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "OrderTable",
    data() {
        return {
            statusCodes: {
                0: "failed",
                1: "processing",
                2: "delivering",
                3: "delivered",
            },
            paymentMethods: {
                1: "Pay by consignor",
                2: "Pay by consignee",
            },
        };
    },
    props: {
        orders: Array,
    },
    methods: {
        goToDetail(id) {
            /* Redirect to order detail page */
            this.$router.push({ name: "OrderDetail", params: { id: id } });
        },
    },
    created() {
        console.log(this.orders);
    },
};
</script>

<style lang="scss" scoped>
.wrapper {
    width: 100%;

    .header,
    .row {
        width: 100%;
        max-width: 1440px;
        margin: 0 auto;
        display: flex;

        &.empty {
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: initial;
            padding: 1rem;
            font-weight: 900;
        }

        .column:first-child {
            max-width: 100px;
        }

        .column:last-child,
        .column:nth-child(2) {
            max-width: 120px;
        }
    }

    .header {
        .column {
            background: var(--primary-color);
            color: #fff;
            font-size: 1rem;
            font-weight: bold;
        }
    }

    .column {
        flex: 1;
        padding: 1rem;
        color: black;
        font-weight: 600;
    }

    .row {
        background-color: rgb(241, 236, 236);
        cursor: pointer;

        transition: all 0.2s ease;

        &:hover {
            background: lightgrey;
        }
    }
}
</style>
