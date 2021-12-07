<template>
    <div class="select-container">
        <label for="city1">{{ label }}</label>
        <div class="search-options">
            <!-- Icon sections -->
            <transition name="fade">
                <i
                    class="fas fa-times"
                    @click="showOptions = false"
                    v-show="showOptions"
                ></i>
            </transition>
            <transition name="fade">
                <i
                    class="fas fa-caret-down"
                    @click="showOptions = true"
                    v-show="!showOptions"
                ></i>
            </transition>

            <!-- Search options -->
            <input
                type="text"
                :placeholder="placeholder"
                autocomplete="nope"
                v-model="displayValue"
                @focus="showOptions = true"
                @input="updateOptions"
                :disabled="noSearch"
            />
            <div
                v-if="noSearch"
                @click="showOptions = !showOptions"
                class="pseudo-select"
            ></div>

            <!-- Options -->
            <transition name="dropdown">
                <div class="options" v-show="showOptions" ref="options">
                    <div class="no-info" v-show="filterArr.length === 0">
                        There is no result
                    </div>
                    <div
                        class="option"
                        v-for="(obj, index) in filterArr"
                        :key="index"
                        @click="updateValue(obj, index)"
                        :class="{ active: obj.id === value }"
                    >
                        {{ obj.name }}
                    </div>
                </div>
            </transition>
        </div>
    </div>
</template>

<script>
export default {
    name: "Dropdown",
    model: {
        prop: "value",
        event: "change",
    },
    props: {
        value: Number, // v-model value
        options: Array, // all the options value for the models {id, name}
        label: {
            // label for the input
            type: String,
            default: "Dropdown label",
        },
        placeholder: {
            // place holder for the input
            type: String,
            default: "Enter your value to filter",
        },
        noSearch: {
            type: Boolean,
            default: false,
        }, // no filter options needed
        all: {
            type: Boolean,
            default: false,
        }, // return null to v-model
    },
    data() {
        return {
            showOptions: false,
            filterArr: [],
            displayValue: "",
            selectVal: null,
        };
    },
    watch: {
        selectVal(newVal, oldVal) {
            this.$emit("change", newVal);
            this.displayValue = this.options.find((obj) => obj.id === newVal).name;
        },
        value(newVal, oldVal) {
            if (!newVal) {
                this.displayValue = null;
            }
        },
        options(newVal, oldVal) {
            this.filterArr = newVal;
        },
    },
    methods: {
        updateOptions(e) {
            // Filter options base on search input
            const newVal = e.target.value;

            this.filterArr = this.options.filter((obj) => {
                return obj.name.trim().toLowerCase().includes(newVal.toLowerCase());
            });
        },
        updateValue(value, index) {
            // Update the value that the user choose
            this.selectVal = value.id;
            this.showOptions = false;

            this.filterArr = this.options.filter((obj) => obj !== value);
            this.filterArr = [value, ...this.filterArr];

            if (this.all) {
                this.filterArr.push({
                    id: null,
                    name: "All",
                });
            }

            this.$refs.options.scrollTop = 0;
        },
    },
    created() {
        this.filterArr = this.options.slice(0);

        if (this.all) {
            this.filterArr.push({
                id: null,
                name: "All",
            });
        }

        if (this.value) {
            this.filterArr.forEach((obj, index) => {
                if (obj.id === this.value) {
                    this.displayValue = obj.name;
                }
            });
        }
    },
};
</script>

<style lang="scss" scoped>
.select-container {
    --input-font-size: 0.8rem;
    display: flex;

    @media only screen and (min-width: 1200px) {
        --input-font-size: 1rem;
    }

    display: flex;
    flex-direction: column;
    gap: 0.5rem;

    label {
        font-size: 0.8rem;
        font-weight: 600;
    }

    .search-options {
        width: 100%;
        position: relative;

        i {
            font-size: 1.2rem;
            position: absolute;
            cursor: pointer;
            right: 10px;
            top: 50%;
            transform: translateY(-50%);
            z-index: 2;
        }

        input {
            width: 100%;
            padding: 8px 15px;
            font-size: var(--input-font-size);
            font-weight: 600;
            line-height: 1.2rem;
            border-radius: 50px;
            outline: none;
            border: 2px solid var(--secondary-color) !important;

            &:focus {
                border: 2px solid var(--primary-color) !important;
                outline: none;
            }

            &:disabled {
                color: black;
                background: transparent;
            }
        }

        .pseudo-select {
            width: 100%;
            height: 100%;
            background-color: transparent;
            position: absolute;
            inset: 0;
            cursor: pointer;
            border-radius: 50px;
            z-index: 1;
        }

        .options {
            position: absolute;
            width: 90%;
            bottom: 0;
            left: 50%;
            transform: translate(-50%, 100%);
            max-height: 150px;
            overflow-y: scroll;
            box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px;
            background: #fff;
            z-index: 999;

            .option {
                padding: 6px 12px;
                background: #fff;
                cursor: pointer;
                transition: 0.3s all ease;

                &.active,
                &:hover {
                    color: #fff;
                    background: var(--secondary-color);
                }

                &.active {
                    background: var(--primary-color);
                }
            }

            .no-info {
                padding: 10px 16px;
                background: #fff;
                text-align: center;
                font-weight: 900;
            }
        }

        // Transition style
        .fade-enter-active,
        .fade-leave-active {
            transition: all 0.3s ease;
        }
        .fade-enter,
        .fade-leave-to {
            opacity: 0;
        }

        .dropdown-enter-active,
        .dropdown-leave-active {
            transform: translate(-50%, 100%);
            transition: all 0.2s ease;
        }
        .dropdown-enter,
        .dropdown-leave-to {
            transform: translate(-50%, 90%);
            opacity: 0;
        }
    }
}
</style>
