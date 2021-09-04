<template>
    <div class="wrapper">
        <apexcharts
            class="chart"
            type="bar"
            :options="chartOptions"
            :series="series"
        ></apexcharts>
    </div>
</template>

<script>
import VueApexCharts from "vue-apexcharts";

export default {
    name: "BarChart",
    components: {
        apexcharts: VueApexCharts,
    },
    props: {
        rangeOption: String,
    },
    data() {
        return {
            chartOptions: {
                chart: {
                    type: "bar",
                    stacked: true,
                    // stackType: "100%",
                },
                responsive: [
                    {
                        breakpoint: 480,
                        options: {
                            legend: {
                                position: "bottom",
                                offsetX: -10,
                                offsetY: 0,
                            },
                        },
                    },
                ],
                xaxis: {
                    categories: null,
                },
                colors: ["#1190CB", "#FF2626"],
                fill: {
                    opacity: 1,
                },
                legend: {
                    position: "right",
                    offsetX: 0,
                    offsetY: 50,
                },
            },
            series: null,
            categories: null,
        };
    },
    watch: {
        rangeOption(newVal, oldVal) {
            this.generateChart();
        },
    },
    methods: {
        getRandomInt(min, max) {
            min = Math.ceil(min);
            max = Math.floor(max);
            return Math.floor(Math.random() * (max - min + 1)) + min;
        },
        generateRandomIntArr(length, minLimit, maxLimit) {
            let arr = [];

            for (let i = 0; i < length; i++) {
                arr.push(this.getRandomInt(minLimit, maxLimit));
            }

            return arr;
        },
        generateChart() {
            const rangeCategories = {
                year: [
                    "January",
                    "February",
                    "March",
                    "April",
                    "May",
                    "June",
                    "July",
                    "August",
                    "September",
                    "October",
                    "November",
                    "December",
                ],
                week: [
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday",
                    "Sunday",
                ],
            };

            this.categories = rangeCategories[this.rangeOption];

            this.chartOptions = {
                ...this.chartOptions,
                ...{
                    xaxis: {
                        categories: this.categories,
                    },
                },
            };

            this.series = [
                {
                    name: "Delivered",
                    data: this.generateRandomIntArr(
                        this.categories.length,
                        5,
                        20
                    ),
                },
                {
                    name: "Failed",
                    data: this.generateRandomIntArr(
                        this.categories.length,
                        1,
                        10
                    ),
                },
            ];
        },
    },
    created() {
        this.generateChart();
    },
};
</script>
<style lang="scss" scoped>
.wrapper {
    width: 100%;
    min-width: 500px;
    max-width: 700px;

    .title {
        background: lightcoral;
    }

    button {
        background: #26e6a4;
        border: 0;
        font-size: 16px;
        color: "#fff";
        padding: 10px;
        margin-left: 28px;
    }
}
</style>
