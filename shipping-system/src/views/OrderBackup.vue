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
                                v-model="consignorName"
                            />
                        </div>
                        <div class="row">
                            <label for="phone1">Phone number</label>
                            <input
                                type="tel"
                                inputmode="numeric"
                                name="phone1"
                                placeholder="Enter phone number"
                                v-model="consignorNumber"
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
                                v-model="address1"
                            />
                        </div>
                        <div class="row">
                            <label for="city1">District - Province</label>
                            <div class="select">
                                <i class="fas fa-chevron-down"></i>
                                <select name="city1" v-model="district1">
                                    <option
                                        v-for="district in districts"
                                        :key="district.disCode"
                                        :value="district.disCode"
                                    >
                                        {{ district.name }}
                                    </option>
                                </select>
                            </div>
                        </div>
                        <div class="row">
                            <label for="district1">Sub District</label>
                            <div class="select">
                                <i class="fas fa-chevron-down"></i>
                                <select name="district1" v-model="subDis1">
                                    <option
                                        v-for="subDistrict in subDistricts1"
                                        :key="subDistrict.code"
                                        :value="subDistrict.code"
                                    >
                                        {{ subDistrict.name }}
                                    </option>
                                </select>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="errors" v-show="error1">
                    Please fill all the information
                    <i class="fas fa-exclamation-circle"></i>
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
                                v-model="consigneeName"
                            />
                        </div>
                        <div class="row">
                            <label for="phone1">Phone number</label>
                            <input
                                type="tel"
                                inputmode="numeric"
                                name="phone1"
                                placeholder="Enter phone number"
                                v-model="consigneeNumber"
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
                                v-model="address2"
                            />
                        </div>
                        <div class="row">
                            <label for="city1">District - Province</label>
                            <div class="select">
                                <i class="fas fa-chevron-down"></i>
                                <select name="city1" v-model="district2">
                                    <option
                                        v-for="district in districts"
                                        :key="district.disCode"
                                        :value="district.disCode"
                                    >
                                        {{ district.name }}
                                    </option>
                                </select>
                            </div>
                        </div>
                        <div class="row">
                            <label for="district1">Sub District</label>
                            <div class="select">
                                <i class="fas fa-chevron-down"></i>
                                <select name="district1" v-model="subDis2">
                                    <option
                                        v-for="subDistrict in subDistricts2"
                                        :key="subDistrict.code"
                                        :value="subDistrict.code"
                                    >
                                        {{ subDistrict.name }}
                                    </option>
                                </select>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="errors" v-show="error2">
                    Please fill all the information
                    <i class="fas fa-exclamation-circle"></i>
                </div>
            </div>
            <div class="line"></div>

            <!-- Package's Info -->
            <div class="order-form__section">
                <div class="title">
                    Package Information - {{ products.length }} Products
                    <span class="btn small" @click="addProduct">
                        <i class="fas fa-plus-circle"></i>Add product
                    </span>
                </div>
                <div class="inputs one-row">
                    <div
                        class="column"
                        v-for="(product, index) in products"
                        :key="index"
                    >
                        <div class="row">
                            <label for="name1">Product Name</label>
                            <input
                                type="text"
                                name="name1"
                                v-model="product.name"
                            />
                        </div>
                        <div class="row">
                            <label for="price">
                                Product Price (Thousand Vietnam Dong)
                            </label>
                            <input
                                type="number"
                                name="price"
                                v-model="product.price"
                            />
                        </div>

                        <i
                            class="fas fa-trash"
                            @click="products.splice(index, 1)"
                            v-show="products.length > 1"
                        ></i>
                    </div>
                </div>
                <div class="errors" v-show="error3">
                    Please fill out all the information, value of the product
                    should be bigger than 10.000 VND
                    <i class="fas fa-exclamation-circle"></i>
                </div>
            </div>
            <div class="line"></div>

            <!-- Shipping's Info -->
            <div class="order-form__section">
                <div class="title">Shipping Information</div>
                <div class="inputs">
                    <div class="column">
                        <!-- Payment method -->
                        <div class="row">
                            <label for="payment-method">Payment Method</label>
                            <div class="select">
                                <i class="fas fa-chevron-down"></i>
                                <select name="payment-method" v-model="payment">
                                    <option value="0">Pay by consignor</option>
                                    <option value="1">Pay by consignee</option>
                                </select>
                            </div>
                        </div>
                        <!-- Customer preview -->
                        <div class="row">
                            <label for="preview">
                                Product Preview when Deliver
                            </label>
                            <div class="select">
                                <i class="fas fa-chevron-down"></i>
                                <select name="preview" v-model="preview">
                                    <option value="0">
                                        Customer allows to observe but not to
                                        try the product
                                    </option>
                                    <option value="1">
                                        Customer not allows to observe product
                                    </option>
                                    <option value="2">
                                        Customer allows to try product
                                    </option>
                                </select>
                            </div>
                        </div>
                        <!-- Shipping Type -->
                        <div class="row">
                            <label for="type">Shipping Type</label>
                            <div class="select">
                                <i class="fas fa-chevron-down"></i>
                                <select name="type" v-model="shippingType">
                                    <option value="0">Standard</option>
                                    <option value="1">Advance</option>
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
                                v-model="note"
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
import { mapState } from "vuex";
import axios from "axios";

export default {
    name: "OrderCreate",
    data() {
        return {
            // Api districts value
            districts: [],
            subDistricts1: [],
            subDistricts2: [],

            // consignor information
            consignorName: "",
            consignorNumber: "",
            address1: "",
            district1: "",
            subDis1: "default",
            error1: false,

            // consignee information
            consigneeName: "",
            consigneeNumber: "",
            address2: "",
            district2: "",
            subDis2: "default",
            error2: false,

            // package information
            products: [{ price: 0, name: "" }],
            error3: false,

            // shipping information
            payment: 0,
            preview: 0,
            shippingType: 0,
            note: "",
        };
    },
    computed: {
        ...mapState(["token"]),
    },
    watch: {
        district1(newVal, oldVal) {
            if (newVal) {
                this.subDis1 = "";

                this.getSubDistricts(newVal)
                    .then((response) => {
                        this.subDistricts1 = response.data.wards;
                    })
                    .catch((error) => console.log(error));
            }
        },
        district2(newVal, oldVal) {
            if (newVal) {
                this.subDis2 = "";

                this.getSubDistricts(newVal)
                    .then((response) => {
                        this.subDistricts2 = response.data.wards;
                    })
                    .catch((error) => console.log(error));
            }
        },
    },
    methods: {
        getAllProvinces() {
            const url = `https://provinces.open-api.vn/api/?depth=2`;
            axios
                .get(url)
                .then((response) => {
                    const provinces = response.data;

                    // Get info from api then rearrange them to get the info for Can Tho city to the front
                    let results = [];
                    let ctInfo = [];

                    for (let province of provinces) {
                        for (let district of province.districts) {
                            const disObj = {
                                proCode: province.code,
                                disCode: district.code,
                                name: `${district.name} - ${province.name}`,
                            };
                            if (province.code === 92) ctInfo.push(disObj);
                            else results.push(disObj);
                        }
                    }
                    this.districts = [...ctInfo, ...results];
                })
                .catch((error) => console.log(error));
        },
        getSubDistricts(districtCode) {
            const url = `https://provinces.open-api.vn/api/d/${districtCode}/?depth=2`;

            return axios.get(url);
        },
        addProduct() {
            this.products.push({
                name: "",
                price: 0,
            });
        },
        async submit() {
            let consignor = null;
            let consignee = null;

            // Validate consignor info
            if (
                this.consignorName &&
                this.consignorNumber &&
                this.address1 &&
                this.district1 &&
                this.subDis1
            ) {
                let province1 = this.districts.find(
                    (info) => info.disCode === this.district1
                ).proCode;

                consignor = {
                    name: this.consignorName,
                    phone: this.consignorNumber,
                    address: this.address1,
                    provinceId: province1,
                    districtId: this.district1,
                    subDistrictId: this.subDis1,
                };

                this.error1 = false;
            } else {
                this.error1 = true;
            }

            // Validate consignee info
            if (
                this.consigneeName &&
                this.consigneeNumber &&
                this.address2 &&
                this.district2 &&
                this.subDis2
            ) {
                let province2 = this.districts.find(
                    (info) => info.disCode === this.district2
                ).proCode;
                consignee = {
                    name: this.consigneeName,
                    phone: this.consigneeNumber,
                    address: this.address2,
                    provinceId: province2,
                    districtId: this.district2,
                    subDistrictId: this.subDis2,
                };

                this.error2 = false;
            } else {
                this.error2 = true;
            }

            // Package information
            for (let product of this.products) {
                if (product.name === "" || product.price <= 0) {
                    this.error3 = true;
                    return;
                }
            }

            this.error3 = false;
            if (!this.error1 && !this.error2 && !this.error3) {
                const order = {
                    consignor,
                    consignee,
                    products: this.products,
                    info: {
                        paymentMethod: this.payment,
                        productPreview: this.preview,
                        shippingType: this.shippingType,
                        note: this.note,
                    },
                };

                try {
                    const url = "http://127.0.0.1:8000/order/create/";
                    const response = await axios.post(url, order, {
                        headers: {
                            Authorization: `Token ${this.token}`,
                        },
                    });
                } catch (err) {
                    console.log(err);
                }
            }
        },
    },
    mounted() {
        this.getAllProvinces();
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

            .errors {
                color: red;
                font-weight: bold;
                font-size: 0.75rem;
            }
        }
    }
}
</style>
