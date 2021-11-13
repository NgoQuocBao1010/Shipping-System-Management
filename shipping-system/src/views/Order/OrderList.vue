<template>
    <div class="orders">
        <div class="orders__header">
            <h1 class="title">Orders Management</h1>
            <div class="filters">
                <div class="filters__inputs">
                    <!-- Select order's status -->
                    <div class="part">
                        <Dropdown
                            v-model="status"
                            :options="statusOptions"
                            placeholder="All"
                            label="Status"
                            :noSearch="true"
                            :all="true"
                        />
                    </div>

                    <!-- Select order's payment method -->
                    <div class="part">
                        <Dropdown
                            v-model="payment"
                            :options="paymentOptions"
                            placeholder="All"
                            label="Payment Methods"
                            :noSearch="true"
                            :all="true"
                        />
                    </div>

                    <!-- Order Timeline -->
                    <div class="part">
                        <div class="timeline">
                            <p>Order created date</p>
                            <div class="timeline__inputs">
                                <div class="input">
                                    <label for="from">From</label>
                                    <input
                                        type="date"
                                        name="from"
                                        v-model="fromDate"
                                        :max="getToday()"
                                    />
                                </div>
                                <div class="input">
                                    <label for="to">To</label>
                                    <input
                                        type="date"
                                        name="to"
                                        v-model="toDate"
                                        :max="getToday()"
                                    />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="orders__content">
            <Table :orders="orders" v-if="orders" />
            <LoadingAnimation v-else />
        </div>
    </div>
</template>

<script>
import moment from "moment";
import { mapState } from "vuex";

import { RepositoryFactory } from "@/api/backend/Factory";
const OrderAPI = RepositoryFactory.get("order");

import { statusOptions, paymentOptions } from "../../globalVariables";

import Dropdown from "@/components/DropdownInput.vue";
import Table from "@/components/order/OrderTable.vue";
import LoadingAnimation from "@/components/CircleAnimation.vue";

export default {
    name: "Orders",
    components: {
        Table,
        Dropdown,
        LoadingAnimation,
    },
    data() {
        return {
            orders: null,

            // status
            statusOptions,
            status: null,
            // Payment Information
            paymentOptions,
            payment: null,

            fromDate: null,
            toDate: null,
            loading: false,
        };
    },
    computed: {
        ...mapState(["token"]),
    },
    watch: {
        async status(newVal) {
            const data = JSON.parse(JSON.stringify(this.$route.query)); // ??
            data["status"] = newVal;

            this.$router
                .replace({
                    name: "Orders",
                    query: data,
                })
                .catch(() => {});

            this.orders = null;
            await this.getOrderList();
        },
        async payment(newVal) {
            const data = JSON.parse(JSON.stringify(this.$route.query)); // ??
            data["payment"] = newVal;

            this.$router
                .replace({
                    name: "Orders",
                    query: data,
                })
                .catch(() => {});

            this.orders = null;
            await this.getOrderList();
        },
        async toDate(newVal, oldVal) {
            if (oldVal) {
                await this.getOrderList();
            }
        },
        async fromDate(newVal, oldVal) {
            if (oldVal) {
                await this.getOrderList();
            }
        },
    },
    methods: {
        getToday() {
            /*  Get current day */
            return moment().format("YYYY-MM-DD");
        },
        async getOrderList() {
            /* Call backend API to retrieve list of all orders */
            try {
                const { data } = await OrderAPI.getList({
                    status: this.status,
                    payment: this.payment,
                    startDate: this.fromDate,
                    endDate: this.toDate,
                });
                this.orders = data;
            } catch (e) {
                this.$func.handleError(e);
            }
        },
    },
    created() {
        const { status, payment } = this.$route.query;

        this.status = status ? parseInt(status) : null;
        this.payment = payment ? parseInt(payment) : null;
    },
    async mounted() {
        this.toDate = this.getToday();
        this.fromDate = moment().subtract(1, "years").format("YYYY-MM-DD");

        await this.getOrderList();
    },
};
</script>

<style lang="scss" scoped>
.orders {
    &__header {
        margin-bottom: 0.8rem;

        .title {
            font-size: 1.5rem;
        }

        .filters {
            display: flex;
            margin: 1rem 0;

            &__title {
                font-weight: bold;
                font-size: 1.2rem;
                margin-right: 2rem;
            }

            &__inputs {
                display: flex;
                min-width: 80%;
                align-items: center;
                gap: 1rem;

                @media only screen and (min-width: 1440px) {
                    gap: 2rem;
                }

                .part {
                    p,
                    label {
                        font-size: 12px;
                        font-weight: 500;
                    }

                    select {
                        -webkit-appearance: none;
                        -moz-appearance: none;
                        -ms-appearance: none;
                        appearance: none;
                        outline: 0;
                        box-shadow: none;
                        border: 0 !important;
                        background: transparent;
                        background-image: none;
                        flex: 1;
                        padding: 0 0.5em;
                        color: black;
                        cursor: pointer;
                        font-size: 16px;
                        font-weight: 600;

                        &::-ms-expand {
                            display: none;
                        }

                        @media only screen and (min-width: 1440px) {
                            font-size: 0.8rem;
                        }
                    }

                    .select {
                        position: relative;
                        display: flex;
                        width: 12rem;
                        height: 1.5em;
                        line-height: 1.5;
                        background: transparent;
                        overflow: hidden;
                        border: 1px solid var(--primary-color);
                        border-radius: 10px;

                        &::after {
                            content: "\25BC";
                            position: absolute;
                            top: 0;
                            right: 0;
                            padding: 0 1em;
                            background: var(--primary-color);
                            color: white;
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            cursor: pointer;
                            pointer-events: none;
                            transition: 0.25s all ease;
                        }

                        @media only screen and (min-width: 1440px) {
                            width: 15rem;
                        }
                    }

                    .timeline {
                        display: flex;
                        flex-direction: column;

                        &__inputs {
                            display: flex;

                            .input {
                                > * {
                                    margin-right: 1rem;
                                }

                                input {
                                    height: 2em;
                                    line-height: 2;
                                    width: 10rem;
                                    font-size: 16px;
                                    font-weight: 600;
                                    padding: 0 2px;
                                    color: var(--primary-color);

                                    @media only screen and (min-width: 1440px) {
                                        font-size: 1rem;
                                        width: 12rem;
                                        padding: 0 0.5rem;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    &__content {
        padding: 2rem 0;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 1.5rem;

        .filter-var {
            width: 100%;
            background: lightblue;
        }
    }
}
</style>
