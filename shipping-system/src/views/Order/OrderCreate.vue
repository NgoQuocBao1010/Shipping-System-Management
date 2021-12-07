<template>
    <div class="wrapper">
        <div class="title">Order Application</div>

        <!-- Order's Form Application -->
        <form class="order-form" @submit.prevent="submit">
            <!-- Consignor Info -->
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
                                v-model="consignor.fullName"
                            />
                        </div>
                        <div class="row">
                            <label for="phone1">Phone number</label>
                            <input
                                type="tel"
                                inputmode="numeric"
                                name="phone1"
                                placeholder="Enter phone number"
                                v-model="consignor.phone"
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
                                v-model="consignor.address"
                            />
                        </div>
                        <div class="row">
                            <Dropdown
                                v-if="provinces"
                                v-model="consignor.districtId"
                                :options="provinces"
                                label="District - Province"
                                placeholder="Enter your province"
                            />
                        </div>
                        <div class="row">
                            <label v-show="!subDistrict1" for="district1">
                                Sub District
                            </label>
                            <input
                                type="text"
                                placeholder="Please pick your province first"
                                disabled
                                v-show="!subDistrict1"
                            />
                            <Dropdown
                                v-if="subDistrict1"
                                v-model="consignor.wardId"
                                :options.sync="subDistrict1"
                                label="Subdistrict"
                                placeholder="Enter your ward name ..."
                            />
                        </div>
                    </div>
                </div>
                <div class="errors" v-show="error.consignor">
                    {{ error.consignor }}
                    <i class="fas fa-exclamation-circle"></i>
                </div>
            </div>

            <!-- Consignee Info -->
            <div class="order-form__section">
                <div class="title">Consignee Information</div>
                <div class="inputs">
                    <div class="column">
                        <div class="row">
                            <label for="name1">Consignee's Name</label>
                            <input
                                type="text"
                                name="name2"
                                placeholder="Enter full name"
                                v-model="consignee.fullName"
                            />
                        </div>
                        <div class="row">
                            <label for="phone2">Phone number</label>
                            <input
                                type="tel"
                                inputmode="numeric"
                                name="phone2"
                                placeholder="Enter phone number"
                                v-model="consignee.phone"
                            />
                        </div>
                    </div>
                    <div class="column">
                        <div class="row">
                            <label for="address2">Address</label>
                            <input
                                type="text"
                                name="address2"
                                placeholder="Enter address"
                                v-model="consignee.address"
                            />
                        </div>
                        <div class="row">
                            <Dropdown
                                v-if="provinces"
                                v-model="consignee.districtId"
                                :options="provinces"
                                label="District - Province"
                                placeholder="Enter your province"
                            />
                        </div>
                        <div class="row">
                            <label v-show="!subDistrict2" for="district1">
                                Sub District
                            </label>
                            <input
                                type="text"
                                placeholder="Please pick your province first"
                                disabled
                                v-show="!subDistrict2"
                            />
                            <Dropdown
                                v-if="subDistrict2"
                                v-model="consignee.wardId"
                                :options.sync="subDistrict2"
                                label="Subdistrict"
                                placeholder="Enter your ward name ..."
                            />
                        </div>
                    </div>
                </div>
                <div class="errors" v-show="error.consignee">
                    {{ error.consignee }}
                    <i class="fas fa-exclamation-circle"></i>
                </div>
            </div>

            <!-- Package's Info -->
            <div class="order-form__section">
                <div class="title">
                    Package Information - {{ products.length }}
                    <span v-if="products.length == 1">Product</span>
                    <span v-else>Products</span>
                    <span class="btn small" @click="addProduct">
                        <i class="fas fa-plus-circle"></i>Add product
                    </span>
                </div>
                <div class="inputs one-row">
                    <div class="column" v-for="(product, index) in products" :key="index">
                        <!-- Product Name -->
                        <div class="row">
                            <label>Product Name</label>
                            <input
                                type="text"
                                v-model="product.name"
                                autocomplete="nope"
                            />
                        </div>

                        <!-- Product Price -->
                        <div class="row">
                            <label for="price">
                                Product Price <b>(Viet Nam Dong - VND)</b>
                            </label>
                            <input
                                type="text"
                                name="price"
                                autocomplete="nope"
                                placeholder="100.000"
                                v-model="product.price"
                                @input="formatPrice($event, index)"
                            />
                        </div>

                        <i
                            class="fas fa-trash"
                            @click="products.splice(index, 1)"
                            v-show="products.length > 1"
                        ></i>
                    </div>
                </div>
                <div class="errors" v-show="error.products">
                    Please fill out all the information, value of each product should be
                    bigger than 10.000 VND
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
                            <Dropdown
                                v-model="payment"
                                :options="paymentOptions"
                                :noSearch="true"
                                label="Payment methods"
                            />
                        </div>
                        <!-- Customer preview -->
                        <div class="row">
                            <Dropdown
                                v-model="preview"
                                :options="previewOptions"
                                label="Customer Preview"
                                :noSearch="true"
                            />
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

            <!-- Submit -->
            <div class="order-form__submit">
                <button type="submit">Submit</button>
                <div class="errors">
                    <i
                        class="fas fa-exclamation-circle"
                        v-show="error.consignor || error.consignee || error.products"
                    ></i>
                </div>
                <Loading v-show="loading" />
            </div>
        </form>

        <!-- Order Confirmation Modal -->
        <Modal
            header="Order Confirmation"
            :active="modal"
            submit="Place Order"
            @submit="placeOrder"
            @toggle="modal = !modal"
        >
            <OrderDetail v-if="order" :order="order" :distance="distance" />
        </Modal>
    </div>
</template>

<script>
import { mapState } from "vuex";
import { required, numeric, minLength } from "vuelidate/lib/validators";

import { RepositoryFactory } from "../../api/backend/Factory";
const OrderRepo = RepositoryFactory.get("order");
import LocationAPI from "../../api/routing/location";

import Dropdown from "@/components/DropdownInput.vue";
import Loading from "@/components/CircleAnimation.vue";

export default {
    name: "OrderCreate",
    components: {
        Dropdown,
        Loading,
        Modal: () => import("@/components/Modal.vue"),
        OrderDetail: () => import("@/components/order/OrderDetail.vue"),
    },
    data() {
        return {
            consignor: {
                fullName: "",
                phone: "",
                address: "",
                districtId: null,
                wardId: null,
            },
            consignee: {
                fullName: "",
                phone: "",
                address: "",
                districtId: null,
                wardId: null,
                fullAddress: "",
            },
            // Dynamic var contains wards of a district
            subDistrict1: null,
            subDistrict2: null,
            // Products info
            products: [
                {
                    name: "Chair",
                    price: 150000,
                },
            ],
            // Payment Information
            paymentOptions: [
                {
                    id: 1,
                    name: "Pay by consignor",
                },
                {
                    id: 2,
                    name: "Pay by consignee",
                },
            ],
            payment: 1,
            // Customer Preview Information
            previewOptions: [
                {
                    id: 1,
                    name: "Customer does not allow to observe products",
                },
                {
                    id: 2,
                    name: "Customer allows to oberseve products but not to try",
                },
                {
                    id: 3,
                    name: "Customer allows to try products",
                },
            ],
            preview: 2,
            // Shipping Information
            shippingOptions: [
                {
                    id: 1,
                    name: "Standard",
                },
                {
                    id: 2,
                    name: "Advance",
                },
            ],
            shipping: 1,
            // Note for the order
            note: null,
            // Order
            order: null,
            // Error handler
            error: {
                consignor: null,
                consignee: null,
                products: null,
            },
            // Modal active
            modal: false,
            // Loading Animation
            loading: false,

            distance: null,
        };
    },
    computed: {
        ...mapState(["user", "provinces", "token", "currentLocation"]),
    },
    watch: {
        async "consignor.districtId"(newVal, oldVal) {
            if (newVal) {
                if (oldVal) this.consignor.wardId = null; // Reset subdistrict dropdown if district is changed

                this.subDistrict1 = await this.$province.getWardList(newVal);
            }
        },
        async "consignee.districtId"(newVal, oldVal) {
            if (newVal) {
                if (oldVal) this.consignee.wardId = null; // Reset subdistrict dropdown if district is changed

                this.subDistrict2 = await this.$province.getWardList(newVal);
            }
        },
        async "consignee.wardId"(newVal, oldVal) {
            if (newVal) {
                const districtName = this.$store.getters.district(
                    this.consignee.districtId
                ).name;

                const ward = await this.$province.getWard(newVal);

                this.consignee.fullAddress = `${ward.name}, ${districtName}`
                    .replace("Thành phố", "")
                    .replace("Quận", "")
                    .replace("Phường", "")
                    .replace("Xã", "")
                    .trim();
            }
        },
    },
    validations: {
        consignor: {
            fullName: { required },
            phone: { required, numeric },
            address: { required },
            districtId: { required, numeric },
            wardId: { required, numeric },
        },
        consignee: {
            fullName: { required },
            phone: { required, numeric },
            address: { required },
            districtId: { required, numeric },
            wardId: { required, numeric },
        },
        products: {
            $each: {
                name: { required },
                price: { required, minLength: minLength(5) },
            },
        },
    },
    methods: {
        async submit() {
            /* Form submit handler */

            // Handle input errors
            this.$v.$touch(); // validate input data
            if (this.$v.$error) {
                console.log("Order Application/OrderCreate: Invalid input");
                this.error.consignor = this.$v.consignor.$error
                    ? "Please fill out all information"
                    : null;

                this.error.consignee = this.$v.consignee.$error
                    ? "Please fill out all information"
                    : null;

                this.error.products = this.$v.products.$error ? true : null;

                return;
            }
            Object.keys(this.error).forEach((field) => (this.error[field] = null)); // Set all error to null

            this.loading = true; // Trigger loading animation

            // Get consignee location and estimate the shipping distance
            const location = await LocationAPI.search(this.consignee.fullAddress);
            console.log("Done getting location", location);
            const routing = location
                ? await LocationAPI.estimateDistance(this.currentLocation, location)
                : null;
            console.log("Done routing", routing);
            const estimatedPrice = routing
                ? await this.estimatePrice(routing.distance)
                : null;
            console.log("Done get the price", estimatedPrice);

            this.distance = routing.distance;

            this.order = {
                consignor: this.consignor,
                consignee: this.consignee,
                products: this.products,

                paymentMethod: this.payment,
                productPreview: this.preview,
                note: this.note,
                estimateDistance: routing ? routing.distance : null,
                deliverTime: routing ? routing.duration : null,
                shippingPrice: estimatedPrice ? estimatedPrice : null,
            };

            this.loading = false;
            this.modal = true;
        },
        async placeOrder() {
            /* Call backend API to place an order after customer confirmation */
            try {
                const { status } = await OrderRepo.create(this.order);

                if (status === 200) {
                    this.$router.push({ name: "Orders" });
                    this.$toast.success("Your order has been placed!");
                }
            } catch (e) {
                console.log(e.response);

                if (e.response.status === 500) {
                    this.$toast.error(
                        "There is an problem occured in our server, plese try again later!",
                        {
                            duration: 4000,
                        }
                    );
                }
            }
        },
        async estimatePrice(distance) {
            /* Call backend API to estimate the shipping money */

            try {
                const { data } = await OrderRepo.getPrice(distance);

                if (data.length > 0) {
                    return data[0].price;
                }

                console.log("Error retriving price info");
                return null;
            } catch (e) {
                console.log("Error retriving price info", e);
            }
        },
        addProduct() {
            /* Add 1 more product input to the form */
            this.products.push({
                name: "",
                price: "",
            });
        },
        formatPrice(e, index) {
            /* Format the price as user typing */
            const value = e.target.value;

            if (value) this.products[index].price = /^\d+$/.test(value) ? value : 0;

            // this.products[index].price = this.$func.formatMoneyToVND(
            //     this.products[index].price
            // );
        },
    },
    created() {
        const { fullName, phone, address, districtId, wardId, ...rest } = this.user;

        this.consignor = {
            fullName,
            phone,
            address,
            districtId,
            wardId,
        };
    },
};
</script>

<style lang="scss" scoped>
.wrapper {
    width: 100%;
    display: flex;
    align-items: center;
    flex-direction: column;

    .errors {
        color: red;
        font-weight: bold;
        font-size: 0.75rem;
    }

    .title {
        font-weight: 900;
        font-size: 2rem;
        position: relative;

        &::after {
            content: "";
            position: absolute;
            left: 0;
            bottom: -12px;
            width: 100%;
            height: 1px;
            background: black;
            transform: scaleX(400%);
        }
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
                padding-left: 20px;
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
                }
            }
        }

        &__submit {
            margin: 0.5rem 0;
            padding: 1rem 0;
            display: flex;
        }
    }
}
</style>
