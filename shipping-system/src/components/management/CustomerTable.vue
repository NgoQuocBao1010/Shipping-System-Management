<template>
    <div class="wrapper">
        <table class="content-table">
            <!-- Header -->
            <thead>
                <tr>
                    <th>No.</th>
                    <th v-if="!isConsigneeList">Account</th>
                    <th v-else>Order ID</th>
                    <th>Name</th>
                    <th>Phone number</th>
                </tr>
            </thead>

            <!-- Body when empty -->
            <tbody class="empty" v-if="profileList.length === 0">
                <div class="empty__info">No customer yet.</div>
            </tbody>

            <tbody v-else>
                <tr
                    v-for="(profile, index) in profileList"
                    :key="index"
                    @click="redirect(profile)"
                >
                    <td>{{ index + 1 }}</td>
                    <td v-if="!isConsigneeList">{{ profile.email }}</td>
                    <td v-else>{{ profile.orderId }}</td>
                    <td>{{ profile.fullName }}</td>
                    <td>{{ profile.phone }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    name: "CustomerTable",
    props: {
        profileList: {
            type: Array,
            default: () => [],
        },
    },
    computed: {
        isConsigneeList() {
            return this.profileList.some((profile) => profile.consignee);
        },
    },
    methods: {
        redirect(profile) {
            /* Redirect to other page accoring to the type of profile */
            return this.isConsigneeList
                ? this.goToOrderDetail(profile)
                : this.goToProfile(profile);
        },
        goToOrderDetail(profile) {
            this.$router.push({ name: "OrderDetail", params: { id: profile.orderId } });
        },
        goToProfile(profile) {
            this.$router.push({ name: "Profile", params: { email: profile.email } });
        },
    },
};
</script>

<style lang="scss" scoped>
.wrapper {
    width: 100%;
    .content-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 0.9em;
        min-width: 400px;
        border-radius: 5px 5px 0 0;
        overflow: hidden;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
        position: relative;

        thead tr {
            background-color: var(--primary-color);
            color: #ffffff;
            text-align: left;
            font-weight: bold;
        }

        th,
        td {
            padding: 12px 15px;

            &.checkbox {
                display: flex;
                justify-content: center;
                align-items: center;
                cursor: pointer;
            }
        }

        tbody {
            &.empty {
                display: flex;
                justify-content: center;
                align-items: center;
                cursor: initial;
                padding: 2rem;
                font-weight: 900;

                .empty__info {
                    font-size: 1.2rem;
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, 10%);
                }
            }

            tr {
                border-bottom: 1px solid #dddddd;
                font-size: 1rem;
                font-weight: 600;
                cursor: pointer;

                &.assign {
                    cursor: initial;
                }

                &:hover {
                    color: var(--primary-color);
                    background-color: #f3f3f3;
                }

                &:last-of-type {
                    border-bottom: 2px solid var(--primary-color);
                }
            }
        }
    }
}
</style>
