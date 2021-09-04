<template>
    <div class="report">
        <div class="report__content">
            <div class="daily"></div>
            <div class="range">
                <div class="select">
                    <i class="fas fa-caret-down"></i>
                    <select name="rangeOption" v-model="rangeOption">
                        <option value="year">Number of Orders this year</option>
                        <option value="week">Number of Orders this week</option>
                    </select>
                </div>
                <BarChart :rangeOption="rangeOption" />
            </div>
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
        return {
            rangeOption: "year",
        };
    },
    computed: {},
    methods: {},
    created() {},
};
</script>

<style lang="scss" scoped>
.report {
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

        .range {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            flex: 1 1 300px;

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
        .daily {
            background: lightblue;
            flex: 1 1 300px;
        }
    }
}
</style>
