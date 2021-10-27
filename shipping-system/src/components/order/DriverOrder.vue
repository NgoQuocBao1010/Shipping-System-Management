<template>
    <div class="wrapper">
        <ul class="navigation">
            <li
                v-for="(tab, index) in tabs"
                :key="index"
                :class="{ active: index === selectedIndex }"
                @click="selectedIndex = index"
            >
                {{ tab }}
            </li>
        </ul>

        <OrderTable />
    </div>
</template>

<script>
import OrderTable from "./OrderTable.vue";

export default {
    name: "DriverOrder",
    components: {
        OrderTable,
    },
    data() {
        return {
            tabs: ["Assigned Order", "Status", "History"],
            selectedIndex: 0,
        };
    },
};
</script>

<style lang="scss" scoped>
.wrapper {
    .navigation {
        margin-bottom: 1rem;
        display: flex;
        gap: 2rem;

        li {
            list-style: none;
            padding: 5px 8px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;

            &.active {
                border-bottom: 2px solid var(--primary-color);
            }
        }
    }
}
</style>
