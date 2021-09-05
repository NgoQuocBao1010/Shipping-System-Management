<template>
    <div class="wrapper">
        <div class="title">Order Application</div>
        <div class="line"></div>
        <form class="order-form" @submit.prevent="submit">
            <!-- Consignor's Info -->
            <div class="order-form__section">
                <div class="title">Consignor Information</div>
                <div class="inputs">
                    <div class="column">
                        <div class="row">
                            <label for="name1">Consignor's Name</label>
                            <input
                                type="text"
                                name="name1"
                                placeholder="Enter full name"
                            />
                        </div>
                        <div class="row">
                            <label for="phone1">Phone number</label>
                            <input
                                type="tel"
                                inputmode="numeric"
                                name="phone1"
                                placeholder="Enter phone number"
                            />
                        </div>
                    </div>
                    <div class="column">
                        <div class="row">
                            <label for="address1">Address</label>
                            <input
                                type="text"
                                name="address1"
                                placeholder="Enter address"
                            />
                        </div>
                        <div class="row">
                            <label for="city1">Province/City</label>
                            <div class="select">
                                <i class="fas fa-chevron-down"></i>
                                <select name="city1">
                                    <option value="all">TP Cần Thơ</option>
                                    <option value="processing">
                                        TP Hồ Chí Minh
                                    </option>
                                    <option value="delivering">
                                        TP Hà Nội
                                    </option>
                                </select>
                            </div>
                        </div>
                        <div class="row">
                            <label for="district1">District</label>
                            <div class="select">
                                <i class="fas fa-chevron-down"></i>
                                <select name="district1">
                                    <option value="all">Cái Răng</option>
                                    <option value="processing">
                                        Ninh Kiều
                                    </option>
                                </select>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="line"></div>

            <!-- Consignee's Info -->
            <div class="order-form__section">
                <div class="title">Consignee Information</div>
                <div class="inputs">
                    <div class="column">
                        <div class="row">
                            <label for="name1">Consignee's Name</label>
                            <input
                                type="text"
                                name="name1"
                                placeholder="Enter full name"
                            />
                        </div>
                        <div class="row">
                            <label for="phone1">Phone number</label>
                            <input
                                type="tel"
                                inputmode="numeric"
                                name="phone1"
                                placeholder="Enter phone number"
                            />
                        </div>
                    </div>
                    <div class="column">
                        <div class="row">
                            <label for="address1">Address</label>
                            <input
                                type="text"
                                name="address1"
                                placeholder="Enter address"
                            />
                        </div>
                        <div class="row">
                            <label for="city1">Province/City</label>
                            <div class="select">
                                <i class="fas fa-chevron-down"></i>
                                <select name="city1">
                                    <option value="all">TP Cần Thơ</option>
                                    <option value="processing">
                                        TP Hồ Chí Minh
                                    </option>
                                    <option value="delivering">
                                        TP Hà Nội
                                    </option>
                                </select>
                            </div>
                        </div>
                        <div class="row">
                            <label for="district1">District</label>
                            <div class="select">
                                <i class="fas fa-chevron-down"></i>
                                <select name="district1">
                                    <option value="all">Cái Răng</option>
                                    <option value="processing">
                                        Ninh Kiều
                                    </option>
                                </select>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="line"></div>

            <!-- Package's Info -->
            <div class="order-form__section">
                <div class="title">
                    Package Information - {{ products }} Products
                    <span class="btn small" @click="products++">
                        <i class="fas fa-plus-circle"></i>Add product
                    </span>
                </div>
                <div class="inputs one-row">
                    <div class="column" v-for="index in products" :key="index">
                        <div class="row">
                            <label for="name1">Product Name</label>
                            <input type="text" name="name1" />
                        </div>
                        <div class="row">
                            <label for="price">Product Price</label>
                            <input type="number" name="price" />
                        </div>

                        <i
                            class="fas fa-trash"
                            @click="products--"
                            v-show="products > 1"
                        ></i>
                    </div>
                </div>
            </div>
            <div class="line"></div>

            <!-- Shipping's Info -->
            <div class="order-form__section">
                <div class="title">Shipping Information</div>
                <div class="inputs">
                    <div class="column">
                        <div class="row">
                            <label for="warning">Shipping Warning</label>
                            <div class="select">
                                <i class="fas fa-chevron-down"></i>
                                <select name="warning">
                                    <option value="all">
                                        Customer allows to observe but not to
                                        try the product
                                    </option>
                                    <option value="processing">
                                        Customer not allows to observe product
                                    </option>
                                    <option value="delivering">
                                        Customer allows to try product
                                    </option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <div class="column">
                        <div class="row">
                            <label for="note">Other Note</label>
                            <textarea
                                name="note"
                                placeholder="Other note"
                            ></textarea>
                        </div>
                    </div>
                </div>
            </div>
            <div class="line"></div>

            <div class="order-form__section">
                <button type="submit">Submit</button>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    name: "OrderCreate",
    data() {
        return {
            consignorName: "",
            consignorNumber: "",
            products: 1,
        };
    },
    methods: {
        submit() {
            console.log("Submitting...");
        },
    },
};
</script>

<style lang="scss" scoped>
.wrapper {
    width: 100%;
    display: flex;
    align-items: center;
    flex-direction: column;

    .title {
        font-weight: bold;
        font-size: 1.2rem;
    }

    .line {
        width: 100%;
        height: 1px;
        background-color: lightgrey;
    }

    .order-form {
        width: 100%;
        min-width: 700px;
        max-width: 1200px;
        margin: 2rem 0;

        &__section {
            margin: 0.5rem 0;
            padding: 1rem 0;

            .title {
                color: var(--primary-color);
                margin-bottom: 0.5rem;
                padding-left: 10px;
                font-size: 1rem;
                position: relative;

                &::after {
                    content: "";
                    position: absolute;
                    top: 0;
                    left: 0;
                    background: var(--primary-color);
                    width: 5px;
                    height: 100%;
                }

                span.btn {
                    position: absolute;
                    right: 10px;
                }
            }

            .inputs {
                --input-font-size: 0.8rem;
                display: flex;

                @media only screen and (min-width: 1200px) {
                    --input-font-size: 1rem;
                }

                .column {
                    flex: 1 1 400px;
                }

                &.one-row {
                    display: flex;
                    flex-direction: column;

                    .column {
                        flex: initial;
                        display: flex;
                        position: relative;

                        .row {
                            flex: 1 1 400px;
                        }

                        i {
                            position: absolute;
                            top: 10px;
                            right: 20px;
                            cursor: pointer;
                            color: lightgrey;
                        }
                    }
                }

                .row {
                    padding: 0.5rem 1rem;
                    display: flex;
                    flex-direction: column;
                    gap: 0.5rem;

                    label {
                        font-size: 0.8rem;
                        font-weight: 600;
                    }

                    .select,
                    input {
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

                    textarea {
                        padding: 8px 15px;
                        font-size: var(--input-font-size);
                        font-weight: 600;
                        min-height: 200px;
                        max-width: 1000px !important;
                        border: 2px solid var(--secondary-color) !important;
                        border-radius: 10px;

                        &:focus {
                            border: 2px solid var(--primary-color) !important;
                            outline: none;
                        }
                    }

                    .select {
                        position: relative;

                        i {
                            position: absolute;
                            cursor: pointer;
                            right: 10px;
                            top: 50%;
                            transform: translateY(-50%);
                            z-index: -1;
                        }

                        select {
                            cursor: pointer;
                            width: 100%;
                            font-size: var(--input-font-size);
                            font-weight: 600;
                            line-height: 1.2rem;
                            background: transparent;
                        }
                    }
                }
            }
        }
    }
}
</style>
