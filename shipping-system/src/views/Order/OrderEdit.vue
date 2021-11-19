<template>
    <div class="wrapper">
        <h1 class="header">
            <span style="color: var(--primary-color)">Editting Mode</span> for Order
            {{ id }}

            <button class="small" @click="deleteOrder">
                <i class="fas fa-trash"></i>Delete
            </button>
        </h1>

        <!-- Information Section -->
        <section v-if="order && drivers">
            <!-- Customer Section -->
            <div class="customer">
                <!-- Consignor -->
                <div class="customer__info">
                    <div class="title">Consignor Information</div>
                    <div class="detail">
                        <div>
                            {{ order.consignor.fullName }}
                        </div>
                        <div>
                            {{ order.consignor.phone }}
                        </div>
                        <div>
                            {{ order.consignor.address }}
                        </div>
                        <div>
                            {{ $store.getters.district(order.consignor.districtId).name }}
                        </div>
                    </div>
                </div>

                <!-- Consignee -->
                <div class="customer__info">
                    <div class="title">Consignee Information</div>
                    <div class="detail">
                        <div>{{ order.consignee.fullName }}</div>
                        <div>
                            {{ order.consignee.phone }}
                        </div>
                        <div>
                            {{ order.consignee.address }}
                        </div>
                        <div>
                            {{ $store.getters.district(order.consignee.districtId).name }}
                        </div>
                    </div>
                </div>
            </div>

            <h2>Edit Field <Loading v-show="loading" class="loading" /></h2>
            <!-- Field edit -->
            <form class="edit-form">
                <!-- Status -->
                <Dropdown
                    v-model="order.status"
                    :options="statusOptions"
                    placeholder="All"
                    label="Status"
                    :noSearch="true"
                />

                <!-- Payment -->
                <Dropdown
                    v-model="order.paymentMethod"
                    :options="paymentOptions"
                    placeholder="All"
                    label="Payment Methods"
                    :noSearch="true"
                />

                <!-- Driver -->
                <Dropdown
                    v-model="order.shipperInfo.id"
                    :options="drivers"
                    placeholder="No driver assigned"
                    label="Driver"
                    :noSearch="true"
                />
            </form>
        </section>
    </div>
</template>

<script>
import { RepositoryFactory } from "../../api/backend/Factory";
const OrderAPI = RepositoryFactory.get("order");
const AccountAPI = RepositoryFactory.get("account");

import { statusOptions, paymentOptions } from "../../globalVariables";

import Dropdown from "@/components/DropdownInput.vue";
import Loading from "@/components/CircleAnimation.vue";

export default {
    name: "OrderEdit",
    components: {
        Dropdown,
        Loading,
    },
    props: {
        id: Number | String,
        orderInstance: {
            required: false,
        },
    },
    data() {
        return {
            order: null,
            drivers: null,
            statusOptions,
            paymentOptions,

            loading: false,
        };
    },
    watch: {
        async "order.status"(newVal, oldVal) {
            if (oldVal) {
                await this.editOrder({ status: newVal });
                this.$toast.success("Order updated!", {
                    duration: 2000,
                });
            }
        },
        "order.paymentMethod"(newVal, oldVal) {
            if (oldVal) {
                this.editOrder({ paymentMethod: newVal });
                this.$toast.success("Order updated!", {
                    duration: 2000,
                });
            }
        },
        "order.shipperInfo.id"(newVal, oldVal) {
            if (newVal) {
                this.editOrder({ driverId: newVal });
                // this.$toast.success("Order updated!", {
                //     duration: 2000,
                // });
            }
        },
    },
    methods: {
        async deleteOrder() {
            /* Delete order */
            const userConfirm = confirm("Are you sure to delete this order?");

            if (userConfirm) {
                try {
                    this.loading = true;
                    const { status } = await OrderAPI.delete(this.id);
                    this.loading = false;

                    if (status === 200) {
                        this.$router.replace({ name: "Orders" });
                        this.$toast.warning(`Order #${this.id} has been deleted`);
                    }
                } catch (e) {
                    console.log(e);
                }
            }
        },
        async editOrder(data) {
            /* Edit order */
            try {
                this.loading = true;
                const { status } = await OrderAPI.edit({
                    orderId: this.id,
                    data,
                });
                this.loading = false;
            } catch (e) {
                console.log(e);
            }
        },
    },
    async created() {
        // Gather order information
        if (!this.orderInstance) {
            const { data } = await OrderAPI.get(this.id);
            this.order = data;
        } else this.order = this.orderInstance;

        if (!this.order.shipperInfo) this.order.shipperInfo = { id: null };

        // Gather drivers information
        const { data } = await AccountAPI.queryProfile({ role: "Employee" });
        this.drivers = data.filter((employee) => !employee.isAdmin);
        this.drivers = this.drivers.map((driver) => {
            return {
                id: driver.id,
                name: driver.fullName,
            };
        });
    },
};
</script>

<style lang="scss" scoped>
.wrapper {
    .header {
        position: relative;

        button {
            position: absolute;
            right: 0;
            font-size: 1rem;
            background: rgb(253, 61, 61);
        }
    }

    section {
        .customer {
            display: flex;
            justify-content: space-between;
            gap: 20px;
            width: 100%;
            margin: 2.5rem 0;

            &__info {
                flex: 1 1 40%;
                padding: 1rem 2rem;
                border-radius: 10px;
                box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px;

                .title {
                    font-size: 1.2rem;
                    font-weight: bold;
                    margin-bottom: 1rem;
                }

                .detail {
                    font-size: 1.2rem;
                    font-weight: 500;
                    & > * {
                        padding: 10px 0;
                    }
                }
            }
        }

        h2 {
            position: relative;

            .loading {
                position: absolute;
                top: 0;
                right: 0;
            }
        }
        .edit-form {
            display: flex;
            margin: 1rem 0;
            gap: 2rem;

            & > * {
                flex: 1 1 40%;
            }
        }
    }
}
</style>
