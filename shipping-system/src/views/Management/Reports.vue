<template>
    <div class="report">
        <div class="loading" v-if="!dataLoaded">
            <loading-animation />
        </div>
        <div class="report__content" v-else>
            <!-- Daily Reports -->
            <div class="daily">
                <div class="title">Reports Today orders</div>

                <div class="information">
                    <div class="category processing">
                        <p class="name">Processing</p>
                        <router-link to="#">
                            <h2>{{ daily.processing }} Orders</h2>
                        </router-link>
                    </div>

                    <div class="category delivering">
                        <p class="name">Delivering</p>
                        <router-link to="#">
                            <h2>{{ daily.delivering }} Orders</h2>
                        </router-link>
                    </div>

                    <div class="category delivered">
                        <p class="name">Delivered</p>
                        <router-link to="#">
                            <h2>{{ daily.delivered }} Orders</h2>
                        </router-link>
                    </div>

                    <div class="category failed">
                        <p class="name">Failed</p>
                        <router-link to="#">
                            <h2>{{ daily.failed }} Orders</h2>
                        </router-link>
                    </div>
                </div>
            </div>

            <!-- Chart of orders -->
            <div class="chart-wrapper">
                <div class="select">
                    <i class="fas fa-caret-down"></i>
                    <select name="rangeOption" v-model="rangeOption">
                        <option value="week">Number of Orders this week</option>
                        <option value="year">Number of Orders this year</option>
                    </select>
                </div>
                <BarChart :data="charts.last7Days" />
            </div>
        </div>
    </div>
</template>

<script>
import moment from "moment";

import { RepositoryFactory } from "../../api/backend/Factory";
const OrderAPI = RepositoryFactory.get("order");

import BarChart from "../../components/BarChartReport.vue";
import LoadingAnimation from "../../components/CircleAnimation.vue";

export default {
    name: "Reports",
    components: {
        LoadingAnimation,
        BarChart,
    },
    data() {
        return {
            dataLoaded: false,

            rangeOption: "week",
            daily: null,
            charts: {
                last7Days: null,
                allTime: null,
            },
        };
    },
    computed: {
        today() {
            return moment().format("YYYY-MM-DD");
        },
    },
    methods: {},
    async created() {
        const { data } = await OrderAPI.getReport();
        this.dataLoaded = true;

        const { daily, last7Days } = data;
        this.daily = daily;
        this.charts.last7Days = last7Days;
    },
};
</script>

<style lang="scss" scoped>
.report {
    &__content {
        padding: 2rem 0;
        display: flex;
        flex-direction: column;

        .daily {
            padding: 1rem 2rem;
            margin-bottom: 4rem;

            .title {
                font-size: 1.2rem;
                font-weight: 900;
                text-align: center;
                margin-bottom: 2rem;
            }

            .information {
                width: 100%;
                display: flex;
                align-items: center;
                justify-content: space-around;

                .category {
                    padding: 1rem 3rem;
                    text-align: center;
                    border-radius: 1rem;

                    &.processing {
                        background: #8fd6e1;
                    }
                    &.delivering {
                        background: var(--secondary-color);
                    }
                    &.delivered {
                        background: lightgreen;
                    }
                    &.failed {
                        background: rgb(238, 78, 78);
                    }

                    p {
                        font-weight: bold;
                        margin-bottom: 1rem;
                    }

                    a {
                        text-decoration: none;
                        color: #fff;
                    }
                }
            }
        }

        .chart-wrapper {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;

            .select {
                position: relative;
                cursor: pointer;

                select {
                    padding: 1rem 2rem;
                    font-size: 1.2rem;
                    font-weight: 900;
                    width: max-content;
                    cursor: pointer;
                    border-radius: 10000px;
                    background: transparent;
                }

                i {
                    position: absolute;
                    right: 10px;
                    top: 50%;
                    transform: translateY(-50%);
                    font-size: 1.5rem;
                    z-index: -1;
                }
            }
        }
    }
}
</style>
