<template>
    <div class="wrapper">
        <template lang="html">
            <div class="tabs__container">
                <!-- Tab content -->
                <div class="slot__wrapper">
                    <slot></slot>
                </div>

                <!-- Tab navigation -->
                <ul class="tab-navigation">
                    <li
                        v-for="(tab, index) in tabs"
                        :key="tab.title"
                        @click="selectTab(index)"
                        :class="{ active: selectedIndex === index }"
                    >
                        <i :class="tab.iconClass"></i>
                        {{ tab.title }}
                    </li>
                </ul>
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
        // this.tabs = this.$refs.transition.$children;
        this.selectTab(0);
    },
};
</script>

<style lang="scss" scoped>
.wrapper {
    width: 100%;

    .tabs__container {
        width: 100%;
        display: flex;
        flex-wrap: nowrap;
        gap: 20px;

        .slot__wrapper {
            flex: 1 1 80%;
            max-width: 1440px;
            // box-shadow: rgba(14, 30, 37, 0.12) 0px 2px 4px 0px,
            //     rgba(14, 30, 37, 0.32) 0px 2px 16px 0px;
        }

        .tab-navigation {
            height: 150px;
            flex: 1 1 150px;
            background: var(--primary-color);
            color: #fff;
            padding: 1rem;
            border-radius: 15px;

            li {
                list-style: none;
                padding: 0.5rem 1rem;
                margin-bottom: 10px;
                font-weight: 600;
                transition: all 0.2s ease-in-out;
                cursor: pointer;
                border-radius: 500px;

                &:hover {
                    background: rgba(255, 255, 255, 0.4);
                }

                &.active {
                    background: #fff;
                    color: var(--primary-color);
                }

                i {
                    font-size: 1.2rem;
                    margin-right: 10px;
                }
            }
        }
    }
}
</style>
