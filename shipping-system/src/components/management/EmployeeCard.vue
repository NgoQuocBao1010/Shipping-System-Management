<template>
    <div class="card">
        <div class="card__profile">
            <img src="../../assets/test/user-icon.jpg" alt="" />
        </div>
        <div class="card__info">
            <div class="ribbons color" :class="role">{{ role }}</div>
            <!-- Card information -->
            <div class="header">
                <!-- Staff member -->
                <p class="header__name">
                    {{ profile.fullName || "No information" }}
                </p>

                <!-- Cosnsignor -->
                <div class="role color" v-if="!profile.consignee" :class="role">
                    {{ profile.email }}
                </div>

                <!-- Consignee -->
                <div class="role color" v-else>
                    Consignee of
                    <router-link
                        class="normal-link"
                        :to="{
                            name: 'OrderDetail',
                            params: { id: profile.orderId },
                        }"
                    >
                        Order {{ profile.orderId }}
                    </router-link>
                </div>
            </div>

            <!-- Function button -->
            <div class="content">
                <!-- Consignee -->
                <div class="content__btn" v-if="profile.consignee">
                    <router-link
                        :to="{
                            name: 'OrderDetail',
                            params: { id: profile.orderId },
                        }"
                        class="btn small"
                    >
                        <i class="fas fa-box-open"></i>Orders
                        {{ profile.orderId }}
                    </router-link>
                </div>

                <!-- Staff member -->
                <div class="content__btn" v-else>
                    <router-link
                        :to="{
                            name: 'Profile',
                            params: { email: profile.email },
                            query: { tab: 1 },
                        }"
                        class="btn small"
                        v-if="profile.isStaff & !profile.isAdmin"
                    >
                        <i class="fas fa-plus-circle"></i>Orders
                    </router-link>

                    <router-link
                        :to="{
                            name: 'Profile',
                            params: { email: profile.email },
                        }"
                        class="btn small"
                    >
                        <i class="fas fa-user-circle"></i>Profile
                    </router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "EmployeeCard",
    props: {
        profile: {
            type: Object,
            default() {
                return {
                    fullName: "John Doe",
                    email: "jhdoe@gmail.com",
                };
            },
        },
    },
    computed: {
        role() {
            if (this.profile.isAdmin) return "manager";
            if (this.profile.isStaff) return "driver";
            else return "customer";
        },
    },
};
</script>

<style lang="scss" scoped>
.card {
    min-width: 250px;
    width: 250px;
    aspect-ratio: 6 / 7;
    padding: 1rem;
    border-radius: 10px;
    box-shadow: rgba(0, 0, 0, 0.12) 0px 1px 3px, rgba(0, 0, 0, 0.24) 0px 1px 2px;
    display: flex;
    flex-direction: column;
    position: relative;

    &__profile {
        display: flex;
        justify-content: center;
        align-items: center;

        img {
            width: 60%;
            max-width: 120px;
            aspect-ratio: 1 / 1;
            border-radius: 50%;
        }
    }

    &__info {
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-evenly;

        .ribbons {
            position: absolute;
            top: 20px;
            right: 0;
            font-size: 12px;
            font-weight: 600;
            text-transform: capitalize;
            padding: 2px 6px;
            border-top-left-radius: 25px;
            border-bottom-left-radius: 25px;
            box-shadow: rgba(0, 0, 0, 0.19) 0px 10px 20px, rgba(0, 0, 0, 0.23) 0px 6px 6px;
        }

        .header {
            display: flex;
            flex-direction: column;
            align-items: center;

            &__name {
                font-weight: 600;
            }
        }

        .content {
            .btn {
                margin: 0 5px;
            }
        }
    }
}
</style>
