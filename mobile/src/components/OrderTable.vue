<template>
    <div class="table-wrapper">
        <table class="content-table">
            <!-- Header -->
            <thead>
                <tr>
                    <th class="id">ID</th>
                    <th class="infor">Consignee</th>
                    <th v-if="history" class="address">Status</th>
                    <th v-else class="address">Actions</th>
                </tr>
            </thead>

            <!-- Body -->
            <tbody class="empty" v-if="orders.length === 0">
                <div class="empty__info">There is no order yet</div>
            </tbody>

            <tbody v-else>
                <tr v-for="order in orders" :key="order.id">
                    <td>{{ order.id }}</td>
                    <td class="infor">
                        <p>{{ order.consignee.fullName }}</p>
                        <p>({{ order.consignee.phone }})</p>
                    </td>
                    <td v-if="history" class="status">{{ orderStatus[order.status] }}</td>
                    <td v-else class="action">
                        <div class="btn-small done" @click="finishOrder(order.id)">
                            Done
                        </div>
                        <div class="btn-small fail">Failed</div>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import axios from "axios";
import { mapState } from "vuex";

export default {
    name: "OrderTable",
    props: {
        orders: {
            type: Array,
            default: () => [],
            require: false,
        },
        history: {
            type: Boolean,
            default: true,
            require: false,
        },
    },
    data: () => ({
        orderStatus: {
            1: "processing",
            2: "delivering",
            3: "delivered",
            4: "failed",
        },
    }),
    computed: {
        ...mapState(["token"]),
    },
    methods: {
        async finishOrder(orderId) {
            /* Get list of order depends on chosen category */
            const url = `https://10.0.2.2:8000/order/finish/${orderId}/`;

            try {
                const { data } = await axios.post(
                    url,
                    { status: true },
                    {
                        headers: {
                            Authorization: `Token ${this.token}`,
                        },
                    }
                );

                this.$emit("done");

                this.$q.notify({
                    type: "positive",
                    message: `Your order has been updated`,
                    position: "bottom",
                    timeout: 1000,
                });
            } catch (e) {
                console.log(e);
            }
        },
    },
};
</script>

<style lang="scss" scoped>
.table-wrapper {
    width: 100%;

    .content-table {
        min-width: 100%;
        border-collapse: collapse;
        font-size: 0.9em;
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

            &.checkbox {
                display: flex;
                justify-content: center;
                align-items: center;
                cursor: pointer;
            }
        }

        tbody {
            &.empty {
                display: flex;
                justify-content: center;
                align-items: center;
                cursor: initial;
                padding-top: 3rem;
                font-weight: 900;

                .empty__info {
                    font-size: 12px;
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, 10%);
                }
            }

            tr {
                border-bottom: 1px solid #dddddd;
                font-size: 12px;
                font-weight: 600;
                cursor: pointer;

                td.infor {
                    p {
                        margin: 0;

                        &:last-child {
                            font-size: 10px;
                        }
                    }
                }

                td.status {
                    text-transform: capitalize;
                }

                td.action {
                    display: flex;
                    align-items: center;

                    .btn-small {
                        font-size: 10px;
                        padding: 2px 4px;
                        margin: 0 2px;
                        border-radius: 5px;

                        &.done {
                            background: limegreen;
                        }

                        &.fail {
                            background: rgb(241, 77, 77);
                        }
                    }
                }

                &.assign {
                    cursor: initial;
                }

                &:last-of-type {
                    border-bottom: 2px solid var(--primary-color);
                }
            }
        }
    }
}
</style>
