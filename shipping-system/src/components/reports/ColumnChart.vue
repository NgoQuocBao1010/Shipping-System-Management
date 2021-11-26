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
        data: Object,
    },
    data() {
        return {
            chartOptions: {
                chart: {
                    type: "bar",
                    stacked: true,
                    fontFamily: "Quicksand, sans-serif",
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
                    style: {
                        fontWeight: "bold",
                        cssClass: "apexcharts-xaxis-label",
                    },
                },
                tooltip: {
                    y: {
                        formatter: (count) => {
                            return `${count} orders`;
                        },
                        style: {
                            fontWeight: "bold",
                            cssClass: "apexcharts-xaxis-label",
                        },
                    },
                },
                colors: ["#8fd6e1", "#7dccff", "#90ee90", "#ee4e4e"],
                fill: {
                    opacity: 1,
                },
                legend: {
                    position: "right",
                    offsetX: 0,
                    offsetY: 50,
                    fontWeight: "700",
                },
            },
            series: this.data.series,
        };
    },
    watch: {
        data() {
            this.generateChart();
        },
    },
    methods: {
        generateChart() {
            this.chartOptions = {
                ...this.chartOptions,
                ...{
                    xaxis: {
                        categories: this.data.categories,
                        labels: {
                            style: {
                                fontWeight: 700,
                                cssClass: "apexcharts-xaxis-label",
                            },
                        },
                    },
                },
            };

            this.series = this.data.series;
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
