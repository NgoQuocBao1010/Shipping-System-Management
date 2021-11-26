<template>
    <div class="report">
        <div class="loading" v-if="!dataLoaded">
            <loading-animation />
        </div>
        <div class="report__content" v-else>
            <!-- Daily Reports -->
            <div class="daily">
                <div class="header">Today Reports</div>
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

                    <div class="category revenue">
                        <p class="name">Revenue</p>
                        <router-link to="#">
                            <h2>{{ $func.formatMoneyToVND(daily.revenue) }} VND</h2>
                        </router-link>
                    </div>
                </div>
            </div>

            <!-- Chart of orders -->
            <div class="chart-wrapper">
                <div class="headers">
                    Orders Reports

                    <ul class="ranges">
                        <li
                            :class="{ active: rangeOption === 'week' }"
                            @click="rangeOption = 'week'"
                        >
                            This week
                        </li>
                        <li
                            :class="{ active: rangeOption === 'month' }"
                            @click="rangeOption = 'month'"
                        >
                            This month
                        </li>
                        <li
                            :class="{ active: rangeOption === 'allTime' }"
                            @click="rangeOption = 'allTime'"
                        >
                            All time
                        </li>
                    </ul>
                </div>

                <div class="information">
                    <component :is="chartComp" :data="chartData"></component>

                    <p>
                        Total Revenue
                        <span>{{ $func.formatMoneyToVND(chartData.revenue) }} VND</span>
                    </p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import moment from "moment";

import { RepositoryFactory } from "../../api/backend/Factory";
const OrderAPI = RepositoryFactory.get("order");

import ColumnChart from "../../components/reports/ColumnChart.vue";
import BarChart from "../../components/reports/BarChart.vue";
import LoadingAnimation from "../../components/CircleAnimation.vue";

export default {
    name: "Reports",
    components: {
        LoadingAnimation,
        ColumnChart,
        BarChart,
    },
    data() {
        return {
            dataLoaded: false,

            rangeOption: "week",
            daily: null,
            charts: {
                last7Days: null,
                thisMonth: null,
                allTime: null,
            },
        };
    },
    computed: {
        today() {
            return moment().format("YYYY-MM-DD");
        },
        chartData() {
            return this.rangeOption === "week"
                ? this.charts.last7Days
                : this.rangeOption === "month"
                ? this.charts.thisMonth
                : this.charts.allTime;
        },
        chartComp() {
            return this.rangeOption !== "allTime" ? "ColumnChart" : "BarChart";
        },
    },
    methods: {},
    async created() {
        const { data } = await OrderAPI.getReport();
        this.dataLoaded = true;

        const { daily, last7Days, thisMonth, allTime } = data;
        this.daily = daily;

        this.charts = {
            last7Days,
            thisMonth,
            allTime,
        };
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
            width: 100%;
            border-radius: 5px;
            margin-bottom: 3em;

            .header {
                padding: 0.5em;
                font-size: 1.2rem;
                font-weight: bold;
                border-bottom: 2px solid var(--primary-color);
                margin-bottom: 0.5em;
            }

            .information {
                width: 100%;
                display: flex;
                align-items: center;
                gap: 1rem;

                .category {
                    flex: 1;
                    padding: 1rem 3rem;
                    border-radius: 1rem;

                    &.processing {
                        background: #8fd6e1;
                    }
                    &.delivering {
                        background: var(--secondary-color);
                    }
                    &.delivered {
                        background: rgb(69, 182, 69);
                    }
                    &.failed {
                        background: rgb(238, 78, 78);
                    }
                    &.revenue {
                        background: rgb(226, 226, 53);
                    }

                    p {
                        font-weight: bold;
                        margin-bottom: 1rem;
                    }

                    h2 {
                        font-size: 1.2rem;
                    }

                    a {
                        text-decoration: none;
                        color: #fff;
                    }
                }
            }
        }

        .chart-wrapper {
            width: 100%;
            margin: 2rem auto;
            padding: 1rem;
            border-radius: 1rem;
            box-shadow: rgba(0, 0, 0, 0.02) 0px 1px 3px 0px,
                rgba(27, 31, 35, 0.15) 0px 0px 0px 1px;

            .headers {
                display: flex;
                align-items: center;
                font-size: 1.4rem;
                font-weight: bold;
                color: var(--primary-color);
                margin-bottom: 2rem;
                border-bottom: 3px solid var(--primary-color);

                .ranges {
                    height: 30px;
                    margin-left: auto;
                    display: flex;
                    gap: 2rem;
                    cursor: pointer;

                    li {
                        list-style: none;
                        font-size: 1rem;
                        padding: 0.3em 1em;
                        border-top-right-radius: 15px;
                        border-top-left-radius: 15px;
                        transition: all 0.3s ease;

                        &.active {
                            background: var(--primary-color);
                            color: #fff;
                        }
                    }
                }
            }

            .information {
                display: flex;
                justify-content: space-around;

                p {
                    width: 250px;
                    font-weight: bold;
                    font-size: 1.3rem;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;

                    span {
                        color: var(--primary-color);
                        font-size: 1.4rem;
                    }
                }
            }
        }
    }
}
</style>
