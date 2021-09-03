<template>
    <div class="wrapper">
        <apexcharts
            class="chart"
            type="bar"
            :options="chartOptions"
            :series="series"
        ></apexcharts>
        <div>
            <button @click="updateChart">Update!</button>
        </div>
    </div>
</template>

<script>
import VueApexCharts from "vue-apexcharts";

export default {
    name: "BarChart",
    components: {
        apexcharts: VueApexCharts,
    },
    data: function () {
        return {
            chartOptions: {
                chart: {
                    type: "bar",
                    stacked: true,
                    stackType: "100%",
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
                    categories: [
                        "2011 Q1",
                        "2011 Q2",
                        "2011 Q3",
                        "2011 Q4",
                        "2012 Q1",
                        "2012 Q2",
                        "2012 Q3",
                        "2012 Q4",
                    ],
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
            series: [
                {
                    name: "Delivered",
                    data: [44, 55, 41, 67, 22, 43, 21, 49],
                },
                {
                    name: "Failed",
                    data: [13, 23, 20, 8, 13, 27, 33, 12],
                },
            ],
        };
    },
    methods: {
        updateChart() {
            const max = 90;
            const min = 20;
            const newData = this.series[0].data.map(() => {
                return Math.floor(Math.random() * (max - min + 1)) + min;
            });
            // In the same way, update the series option
            this.series = [
                {
                    data: newData,
                },
            ];
        },
    },
};
</script>
<style lang="scss" scoped>
.wrapper {
    width: 100%;
    max-width: 700px;
    .chart {
        width: 100%;
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
