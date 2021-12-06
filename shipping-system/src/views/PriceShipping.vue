<template>
    <div class="wrapper">
        <div class="header" id="contact">
            <span>Kaz Shipping System</span>
            <p>
                Address: 100C, B20 street, Hưng Phú Residental Area, Cái Răng district,
                Cần Thơ city, Việt Nam
            </p>
            <p>Contact: baoB1809677@student.ctu.edu.vn</p>
        </div>

        <div class="map-container">
            <CompanyMap />
        </div>

        <!-- Header -->
        <div class="header">
            <span>Kaz Shipping System</span>
            <i class="fas fa-shipping-fast icon"></i> price list

            <button v-if="$store.getters.isAdmin" class="small" @click="editPriceObj(-1)">
                <i class="fas fa-plus-circle"></i>Add Price
            </button>
        </div>

        <!-- Main content -->
        <div class="content" id="price">
            <!-- Table of pricing list -->
            <table>
                <thead>
                    <tr>
                        <th>Distance</th>
                        <th>Price</th>
                        <th v-if="$store.getters.isAdmin">Edit / Delete</th>
                    </tr>
                </thead>

                <tbody>
                    <tr v-for="(price, index) in prices" :key="price.id">
                        <td v-if="price.lowerLimit === 0">
                            In {{ price.upperLimit }} kilometer range
                        </td>
                        <td v-else>
                            {{ price.lowerLimit }} - {{ price.upperLimit }} kilometer
                        </td>
                        <td>{{ $func.formatMoneyToVND(price.price) }} VND</td>
                        <td v-if="$store.getters.isAdmin">
                            <i class="fas fa-edit" @click="editPriceObj(index)"></i>
                            <i
                                class="fas fa-minus-circle"
                                @click="deletePrice(index)"
                            ></i>
                        </td>
                    </tr>
                </tbody>
            </table>

            <!-- Form edit -->
            <div class="form-container" v-if="$store.getters.isAdmin">
                <form v-show="edit">
                    <div class="inputs">
                        <label for="lower">Lower Limit (km)</label>
                        <input type="number" v-model="editPrice.lowerLimit" />
                    </div>

                    <div class="inputs">
                        <label for="upper">Upper Limit (km)</label>
                        <input type="number" v-model="editPrice.upperLimit" />
                    </div>

                    <div class="inputs">
                        <label for="price">Price Limit (VND)</label>
                        <input type="number" v-model="editPrice.price" />
                    </div>

                    <p v-show="error" class="error">
                        <i class="fas fa-exclamation-circle"></i>{{ error }}
                    </p>

                    <div class="buttons-container">
                        <button type="submit" class="small" @click.prevent="submit">
                            Save
                        </button>

                        <button class="small close" @click.prevent="edit = false">
                            Close
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import { required, minLength } from "vuelidate/lib/validators";

import { RepositoryFactory } from "../api/backend/Factory";
const OrderAPI = RepositoryFactory.get("order");

import CompanyMap from "../components/CompanyMap.vue";

export default {
    components: {
        CompanyMap,
    },
    data() {
        return {
            prices: null,
            edit: false,
            editPrice: {
                lowerLimit: null,
                upperLimit: null,
                price: null,
            },

            // form error
            error: null,
        };
    },
    computed: {
        submitMsg() {
            return false;
        },
    },
    methods: {
        async getPrices() {
            /* Get all prices */
            const { data } = await OrderAPI.getAllPrices();
            this.prices = data;
        },
        editPriceObj(index) {
            this.edit = true;
            if (index !== -1) {
                this.editPrice = this.prices[index];
            } else {
                this.editPrice = {
                    lowerLimit: null,
                    upperLimit: null,
                    price: null,
                };
            }
        },
        async deletePrice(index) {
            const userConfirm = confirm(`Are you sure to delete this price?`);

            if (userConfirm) {
                try {
                    const priceId = this.prices[index].id;
                    await OrderAPI.deletePrice(priceId);

                    this.$toast.success("Delete successfully");
                    await this.getPrices();
                } catch (e) {
                    console.log(e);
                }
            }
        },
        async submit() {
            /* Submit handler */

            this.$v.$touch();
            if (this.$v.$error) {
                this.error =
                    "Please fill out all the field and make sure the price is at least 10.000 VND";

                return;
            }

            this.error = null;

            try {
                this.edit = false;
                await OrderAPI.editShippingPrice(this.editPrice);

                this.$toast.success("Update successfully");
                await this.getPrices();
            } catch (e) {
                console.log(e.response);
            }
        },
    },
    validations: {
        editPrice: {
            lowerLimit: { required },
            upperLimit: { required },
            price: { required, minLength: minLength(5) },
        },
    },
    async mounted() {
        await this.getPrices();
    },
};
</script>

<style lang="scss" scoped>
.wrapper {
    .map-container {
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 100px;
    }

    .header {
        font-size: 2rem;
        font-weight: bold;
        position: relative;

        span {
            color: var(--primary-color);
        }

        p {
            font-size: 1.2rem;
            margin: 10px 0;
        }

        .icon {
            color: var(--primary-color);
            margin: 0 1rem;
        }

        button {
            position: absolute;
            right: 0;
        }
    }

    table {
        width: 100%;
        border-collapse: collapse;
        font-size: 1.2em;
        text-align: center;
        min-width: 400px;
        margin: 2rem 0;
        border-radius: 5px 5px 0 0;
        overflow: hidden;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
        position: relative;

        thead tr {
            background-color: var(--primary-color);
            color: #ffffff;
            text-align: left;
            font-weight: bold;
            text-align: center;
        }

        th,
        td {
            padding: 12px 15px;
        }

        tbody {
            tr {
                border-bottom: 1px solid #dddddd;
                font-weight: 600;

                &:hover {
                    color: var(--primary-color);
                    background-color: #f3f3f3;
                }

                &:last-of-type {
                    border-bottom: 2px solid var(--primary-color);
                }

                i {
                    padding: 5px;
                    font-size: 1.3rem;
                    cursor: pointer;
                    margin-right: 10px;
                    color: var(--secondary-color);

                    transition: 0.2s ease all;

                    &.fa-minus-circle {
                        color: rgb(247, 63, 63);
                    }

                    &:hover {
                        color: var(--primary-color);
                    }
                }
            }
        }
    }

    form {
        margin: 1rem 0;
        padding: 1rem;
        border-bottom: 3px solid var(--primary-color);

        .inputs {
            display: flex;
            gap: 2rem;
            align-items: center;
            font-size: 1.2rem;
            margin: 1rem 0;

            label {
                font-weight: 500;
            }

            input {
                padding: 4px 12px;
                font-size: 1.2rem;
                font-weight: 600;
                line-height: 1.2rem;
                outline: none;
                border: 2px solid var(--secondary-color) !important;

                &:focus {
                    border: 2px solid var(--primary-color) !important;
                    outline: none;
                }
            }
        }

        .error {
            color: red;
            font-weight: 600;
            font-style: italic;

            i {
                margin-right: 5px;
                margin-bottom: 10px;
            }
        }

        .buttons-container {
            display: flex;
            gap: 2rem;

            .close {
                background: rgb(248, 62, 62);
            }
        }
    }
}
</style>
