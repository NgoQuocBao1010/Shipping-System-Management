<template>
    <div class="wrapper">
        <table class="content-table">
            <thead>
                <tr>
                    <th class="id">ID</th>
                    <th class="date">Date created</th>
                    <th class="username">From Account</th>
                    <th class="address">Place of delivery</th>
                    <th class="account">Shipper</th>
                    <th class="status">Status</th>
                </tr>
            </thead>
            <tbody class="empty" v-if="orders.length === 0">
                <div class="empty__info">There is no order yet</div>
            </tbody>
            <tbody v-else>
                <tr
                    v-for="order in orders"
                    :key="order.id"
                    @click="goToDetail(order.id)"
                >
                    <td>{{ order.id }}</td>
                    <td>{{ order.dateCreated }}</td>
                    <td>{{ order.consignor.email }}</td>
                    <td>
                        {{ order.consignee.address }},
                        {{
                            $store.getters.district(order.consignee.districtId)
                                .name
                        }}
                    </td>
                    <td>Unassigned</td>
                    <td>
                        <div :class="'order-' + statusCodes[order.status]">
                            {{ statusCodes[order.status] }}
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    name: "Table",
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
        orders: {
            type: Array,
            default: () => [],
        },
    },
    methods: {
        goToDetail(id) {
            /* Redirect to order detail page */
            this.$router.push({ name: "OrderDetail", params: { id: id } });
        },
    },
};
</script>

<style lang="scss" scoped>
.wrapper {
    width: 100%;

    .content-table {
        width: 100%;
        border-collapse: collapse;
        margin: 25px 0;
        font-size: 0.9em;
        min-width: 400px;
        border-radius: 5px 5px 0 0;
        overflow: hidden;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
        position: relative;

        thead tr {
            background-color: var(--primary-color);
            color: #ffffff;
            text-align: left;
            font-weight: bold;
        }

        th,
        td {
            padding: 12px 15px;
        }

        tbody {
            &.empty {
                display: flex;
                justify-content: center;
                align-items: center;
                cursor: initial;
                padding: 2rem;
                font-weight: 900;

                .empty__info {
                    font-size: 1.2rem;
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, 10%);
                }
            }

            tr {
                border-bottom: 1px solid #dddddd;
                font-size: 1rem;
                font-weight: 600;
                cursor: pointer;

                &:hover {
                    color: var(--primary-color);
                    background-color: #f3f3f3;
                }

                &:last-of-type {
                    border-bottom: 2px solid var(--primary-color);
                }
            }
        }
    }
}
</style>
