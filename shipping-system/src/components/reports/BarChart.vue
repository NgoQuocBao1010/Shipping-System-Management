<template>
    <div class="wrapper">
        <apexcharts
            class="chart"
            type="bar"
            :options="options"
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
            options: {
                chart: {
                    type: "bar",
                    height: 50,
                    fontFamily: "Quicksand, sans-serif",
                },
                plotOptions: {
                    bar: {
                        borderRadius: 4,
                        horizontal: true,
                        distributed: true,
                    },
                },
                dataLabels: {
                    enabled: true,
                    distributed: true,
                    style: {
                        colors: ["#222"],
                        fontWeight: 700,
                    },
                },
                colors: ["#8fd6e1", "#7dccff", "#90ee90", "#ee4e4e"],
                xaxis: {
                    categories: ["Processing", "Delivering", "Delivered", "Failed"],
                    labels: {
                        style: {
                            fontWeight: 700,
                            fontSize: "13px",
                        },
                    },
                },
                yaxis: {
                    labels: {
                        style: {
                            fontWeight: 700,
                            fontSize: "13px",
                        },
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
                legend: {
                    position: "right",
                    offsetX: 0,
                    offsetY: 50,
                    fontWeight: "700",
                },
            },
            series: [{ name: "Orders", data: [] }],
        };
    },
    watch: {},
    methods: {},
    created() {
        const { processing, delivering, delivered, failed } = this.data;
        this.series[0].data = [processing, delivering, delivered, failed];
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
