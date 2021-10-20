<template>
    <div class="card">
        <div class="card__profile">
            <img src="../../assets/test/user-icon.jpg" alt="" />
        </div>
        <div class="card__info">
            <div class="ribbons color" :class="role">{{ role }}</div>
            <div class="header">
                <p class="header__name">
                    {{ profile.fullName || "No information" }}
                </p>
                <div class="role color" v-if="!profile.consignee" :class="role">
                    {{ profile.email }}
                </div>
                <div class="role color" v-else>
                    Consignee of
                    <router-link
                        class="normal-link"
                        :to="{
                            name: 'OrderDetail',
                            params: { id: profile.orderId },
                        }"
                        >Order {{ profile.orderId }}</router-link
                    >
                </div>
            </div>
            <div class="content">
                <div class="content__btn" v-if="!profile.consignee">
                    <router-link
                        to="#"
                        class="btn small"
                        v-if="profile.isAdmin"
                    >
                        <i class="fas fa-plus-circle"></i>Add Task
                    </router-link>
                    <router-link to="#" class="btn small" v-else>
                        <i class="fas fa-box-open"></i>Orders
                    </router-link>
                    <router-link to="#" class="btn small">
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
            return this.profile.isAdmin ? "manager" : "customer";
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
            box-shadow: rgba(0, 0, 0, 0.19) 0px 10px 20px,
                rgba(0, 0, 0, 0.23) 0px 6px 6px;
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
