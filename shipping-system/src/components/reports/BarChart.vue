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
    max-width: 900px;

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
