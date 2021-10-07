<template>
    <div class="wrapper">
        <div class="title">Order Application</div>
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
                                v-model="test"
                                :values="provinces"
                            />
                        </div>
                        <div class="row">
                            <label for="district1">Sub District</label>
                        </div>
                    </div>
                </div>
                <div class="errors" v-show="consignor.error">
                    Please fill all the information
                    <i class="fas fa-exclamation-circle"></i>
                </div>
            </div>
            <div class="line"></div>
            <div class="order-form__section">
                <button type="submit">Submit</button>
            </div>
        </form>
        {{ test }}
    </div>
</template>

<script>
import { mapState } from "vuex";
import axios from "axios";

import Dropdown from "../components/DropdownInput.vue";

export default {
    name: "OrderCreate",
    components: {
        Dropdown,
    },
    data() {
        return {
            consignor: {
                fullName: "",
                phone: "",
                address: "",
                districtId: null,
                subDistrictId: null,
            },
            error: null,
            test: "",
        };
    },
    computed: {
        ...mapState(["user", "provinces"]),
    },
    watch: {},
    methods: {
        async submit() {},
    },
    created() {
        this.consignor = this.user;
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

            .errors {
                color: red;
                font-weight: bold;
                font-size: 0.75rem;
            }
        }
    }
}
</style>
