<template>
    <div class="wrapper">
        <div class="header">
            <span>Kaz Shipping System</span>
            <i class="fas fa-shipping-fast icon"></i> price list
        </div>
        <div class="content">
            <!-- Table of pricing list -->
            <table>
                <thead>
                    <tr>
                        <th>Distance</th>
                        <th>Price</th>
                        <th>Estimated Time to Shipped</th>
                        <th v-if="$store.getters.isAdmin">Edit</th>
                    </tr>
                </thead>

                <tbody>
                    <tr v-for="(price, index) in prices" :key="price.id">
                        <td v-if="price.lowerLimit === 0">
                            In {{ price.upperLimit }} kilometer range
                        </td>
                        <td v-else>
                            {{ price.lowerLimit }} -
                            {{ price.upperLimit }} kilometer
                        </td>
                        <td>{{ $func.formatMoneyToVND(price.price) }} VND</td>
                        <td>Less than 1 day</td>
                        <td
                            v-if="$store.getters.isAdmin"
                            @click="editObj(index)"
                        >
                            <i class="fas fa-edit"></i>
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

                    <button type="submit" class="small" @click.prevent="submit">
                        Save
                    </button>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import { RepositoryFactory } from "../api/backend/Factory";
const OrderAPI = RepositoryFactory.get("order");

export default {
    data() {
        return {
            prices: null,

            edit: false,
            editPrice: {
                lowerLimit: null,
                upperLimit: null,
                price: null,
            },
        };
    },
    methods: {
        editObj(index) {
            this.edit = true;
            this.editPrice = this.prices[index];
        },
        async submit() {
            this.edit = false;
            console.log(this.editPrice);

            await OrderAPI.editShippingPrice(this.editPrice);
        },
    },
    async mounted() {
        const { data } = await OrderAPI.getAllPrices();
        this.prices = data;
    },
};
</script>

<style lang="scss" scoped>
.wrapper {
    .header {
        font-size: 2rem;
        font-weight: bold;
        position: relative;

        span {
            color: var(--primary-color);
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
                }
            }
        }
    }

    form {
        margin: 1rem 0;

        .inputs {
            display: flex;
            gap: 2rem;
            align-items: center;
            font-size: 1.2rem;
            margin: 1rem 0;

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
    }
}
</style>
