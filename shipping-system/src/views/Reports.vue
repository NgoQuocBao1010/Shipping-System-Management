<template>
    <div class="orders">
        <div class="orders__header">
            <div class="title">Report Pagte</div>
        </div>

        <div class="orders__content">
            <BarChart />
        </div>
    </div>
</template>

<script>
import BarChart from "../components/BarChartReport.vue";

export default {
    name: "Reports",
    components: {
        BarChart,
    },
    data() {
        return {};
    },
    computed: {},
    methods: {},
};
</script>

<style lang="scss" scoped>
.orders {
    &__header {
        margin-bottom: 0.8rem;

        .title {
            font-size: 1.5rem;
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
