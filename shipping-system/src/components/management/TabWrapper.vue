<template>
    <div class="wrapper">
        <template lang="html">
            <div>
                <!-- Tab title -->
                <ul class="tabs__header">
                    <li
                        v-for="(tab, index) in tabs"
                        :key="tab.title"
                        @click="selectTab(index)"
                        :class="{ active: selectedIndex === index }"
                    >
                        {{ tab.title }}
                    </li>
                </ul>

                <!-- Tab content -->
                <div class="slot__wrapper">
                    <slot></slot>
                </div>
            </div>
        </template>
    </div>
</template>

<script>
export default {
    name: "TabWrapper",
    data() {
        return {
            selectedIndex: 0,
            tabs: [],
        };
    },
    methods: {
        selectTab(index) {
            this.selectedIndex = index;

            this.tabs.forEach((tab, i) => {
                tab.isActive = i === this.selectedIndex;
            });
        },
    },
    created() {
        this.tabs = this.$children;
    },
    mounted() {
        this.selectTab(0);
    },
};
</script>

<style lang="scss" scoped>
.wrapper {
    width: 100%;

    .tabs__header {
        display: flex;
        gap: 2rem;

        li {
            display: inline-block;
            padding: 10px 20px;
            list-style: none;
            font-weight: 500;
            cursor: pointer;

            &.active {
                border-bottom: 2px solid var(--primary-color);
            }
        }
    }

    .slot__wrapper {
        margin-top: 1.5rem;
        padding: 10px 20px;
        border-radius: 15px;
        box-shadow: rgba(14, 30, 37, 0.12) 0px 2px 4px 0px,
            rgba(14, 30, 37, 0.32) 0px 2px 16px 0px;
    }
}
</style>
