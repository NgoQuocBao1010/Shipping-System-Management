<template>
    <div class="select-container">
        <label for="city1">District - Province</label>
        <div class="search-options">
            <i class="fas fa-chevron-down" @click="closeDropdown"></i>
            <input
                type="text"
                placeholder="Enter your province ..."
                autocomplete="nope"
                v-model="value"
                @focus="showOptions = true"
                @input="updateOptions"
            />

            <div class="options" v-show="showOptions" ref="options">
                <div class="no-info" v-show="filterArr.length === 0">
                    There is no result
                </div>
                <div
                    class="option"
                    v-for="(val, index) in filterArr"
                    :key="index"
                    @click="updateValue(val, index)"
                    :class="{ active: val === value }"
                >
                    {{ val.name }}
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "Dropdown",
    model: {
        prop: "title",
        event: "change",
    },
    props: {
        title: String,
        values: Array,
    },
    data() {
        return {
            showOptions: false,
            arr: [
                "Cái Răng - Cần Thơ",
                "Ninh Kiều - Cần Thơ",
                "Quận 1 - TP Hồ Chí Minh",
                "Quận 2 - TP Hồ Chí Minh",
                "Quận 3 - TP Hồ Chí Minh",
                "Hạ Long - Hà Nội",
                "Phước Vinh - Hà Nội",
            ],
            filterArr: [],
            value: "",
            selectVal: "",
        };
    },
    watch: {
        selectVal(newVal, oldVal) {
            this.$emit("change", newVal);
        },
    },
    methods: {
        updateOptions(e) {
            const newVal = e.target.value;

            this.filterArr = this.arr.filter((val) => {
                return val.trim().toLowerCase().includes(newVal.toLowerCase());
            });
        },
        closeDropdown() {
            // Detect if option is choosen before close
            this.value = this.selectVal;
            this.showOptions = false;
        },
        updateValue(value, index) {
            // Update the value that the user choose
            this.selectVal = value;
            this.closeDropdown();

            this.filterArr = this.arr.filter((val) => val !== value);
            this.filterArr = [value, ...this.filterArr];

            this.$refs.options.scrollTop = 0;
        },
    },
    created() {
        this.filterArr = this.values;
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
            position: absolute;
            cursor: pointer;
            right: 10px;
            top: 50%;
            transform: translateY(-50%);
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
    }
}
</style>
