<template>
    <div class="wrapper">
        <div class="header">
            <div class="column">Order ID</div>
            <div class="column">Order Date</div>
            <div class="column">Place of Receipt</div>
            <div class="column">Place of Delivery</div>
            <div class="column">Payment Method</div>
            <div class="column">Shipper</div>
            <div class="column">Status</div>
        </div>
        <div class="content">
            <div
                class="row"
                v-for="order in orders"
                :key="order.id"
                @click="goToDetail(order.id)"
            >
                <div class="column">{{ order.id }}</div>
                <div class="column">{{ order.date }}</div>
                <div class="column">{{ order.placeOfReceipt }}</div>
                <div class="column">{{ order.placeOfDelivery }}</div>
                <div class="column">{{ order.paymentMethod }}</div>
                <div class="column">{{ order.shipper }}</div>
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
                1: "delivered",
                2: "delivering",
                3: "processing",
            },
        };
    },
    props: {
        orders: Array,
    },
    methods: {
        goToDetail(id) {
            this.$router.push({ name: "OrderDetail", params: { id: id } });
        },
    },
};
</script>

<style lang="scss" scoped>
.wrapper {
    width: 100%;

    .header,
    .row {
        width: 100%;
        max-width: 1000px;
        margin: 0 auto;
        display: flex;

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
