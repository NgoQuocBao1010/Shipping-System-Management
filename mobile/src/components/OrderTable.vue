<template>
    <div class="table-wrapper">
        <table class="content-table">
            <!-- Header -->
            <thead>
                <tr>
                    <th class="id">ID</th>
                    <th class="infor">Consignee</th>
                    <th class="address">Status</th>
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
                    <td class="status">{{ orderStatus[order.status] }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    name: "OrderTable",
    props: {
        orders: {
            type: Array,
            default: () => [],
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
    created() {
        console.log(this.orders);
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

                &.assign {
                    cursor: initial;
                }

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
