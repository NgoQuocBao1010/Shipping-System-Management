<template>
    <div class="orders">
        <div class="orders__header">
            <h1 class="title">Orders Management</h1>
            <div class="filters">
                <p class="filters__title">Filters</p>
                <div class="filters__inputs">
                    <!-- Select order's status -->
                    <div class="part">
                        <label for="status">Status</label>
                        <div class="select">
                            <select
                                name="status"
                                class="filters__status"
                                v-model="status"
                            >
                                <option value="all">All</option>
                                <option value="processing">Processing</option>
                                <option value="delivering">Delivering</option>
                                <option value="delivered">Delivered</option>
                                <option value="failed">Failed</option>
                            </select>
                        </div>
                    </div>
                    <!-- Select order's payment method -->
                    <div class="part">
                        <label for="payment">Payment Method</label>
                        <div class="select">
                            <select
                                name="payment"
                                class="filters__payment"
                                v-model="payment"
                            >
                                <option value="all">All</option>
                                <option value="processing">
                                    Payment by consignor
                                </option>
                                <option value="delivering">
                                    Payment by consignee
                                </option>
                            </select>
                        </div>
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

        <div class="orders__content"></div>
    </div>
</template>

<script>
import moment from "moment";

export default {
    name: "Orders",
    components: {},
    data() {
        return {
            status: "all",
            payment: "all",
            fromDate: null,
            toDate: null,
        };
    },
    watch: {
        status(newVal, oldVal) {
            console.log(newVal);
        },
    },
    methods: {
        getToday() {
            return moment().format("YYYY-MM-DD");
        },
    },
    created() {
        this.toDate = this.getToday();
        this.fromDate = moment().subtract("weeks", 1).format("YYYY-MM-DD");
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
            align-items: center;
            margin: 1rem 0;

            &__title {
                font-weight: bold;
                font-size: 1.2rem;
                margin-right: 2rem;
            }

            &__inputs {
                display: flex;
                align-items: center;
                gap: 1rem;

                @media only screen and (min-width: 1200px) {
                    gap: 3rem;
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
                        font-size: 10px;
                        font-weight: 600;

                        &::-ms-expand {
                            display: none;
                        }

                        @media only screen and (min-width: 1200px) {
                            font-size: 0.8rem;
                        }
                    }

                    .select {
                        position: relative;
                        display: flex;
                        width: 10rem;
                        height: 2em;
                        line-height: 2;
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

                        @media only screen and (min-width: 1200px) {
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
                                    width: 8rem;
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
    }
}
</style>
