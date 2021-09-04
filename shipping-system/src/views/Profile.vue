<template>
    <div class="profile">
        <div class="profile__header">
            <h1 class="title">Profile Information</h1>
        </div>
        <form class="profile__content">
            <div class="input">
                <label for="name">Full Name: </label>
                <input
                    :class="{ active: edit }"
                    name="name"
                    type="text"
                    v-model="fullName"
                    :readonly="!edit"
                />
            </div>
            <div class="input">
                <label for="email">Email: </label>
                <input
                    :class="{ active: edit }"
                    name="email"
                    type="enail"
                    v-model="email"
                    :readonly="!edit"
                />
            </div>
            <div class="input">
                <label for="address">Address: </label>
                <input
                    :class="{ active: edit }"
                    name="address"
                    type="text"
                    v-model="address"
                    :readonly="!edit"
                />
            </div>
            <div class="input">
                <label for="dob">Date of birth: </label>
                <input
                    name="dob"
                    type="date"
                    v-model="date"
                    :readonly="!edit"
                    :class="{ active: edit }"
                />
            </div>
        </form>
    </div>
</template>

<script>
export default {
    name: "Profile",
    components: {},
    data() {
        return {
            fullName: "John Doe",
            address: "số 2, Phan Đình Phùng , Ninh Kiều, Cần Thơ",
            date: "2000-05-01",
            email: "jdoe@gmail.com",
            edit: true,
        };
    },
};
</script>

<style lang="scss" scoped>
.profile {
    &__header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 0.8rem;

        .title {
            font-size: 1.5rem;
        }
    }

    &__content {
        padding: 2rem;
        display: flex;
        flex-direction: column;
        box-shadow: rgba(17, 17, 26, 0.05) 0px 1px 0px,
            rgba(17, 17, 26, 0.1) 0px 0px 8px;

        .input {
            display: flex;
            align-items: center;

            label {
                margin-right: 2rem;
                width: 200px;
            }

            input {
                flex: 1 1 300px;
                max-width: 400px;
                line-height: 2;
                padding: 5px;
                margin-bottom: 1rem;
                font-size: 1rem;
                font-weight: 600;
                border: none;
                border-bottom: 1px solid black;

                &:focus {
                    outline: none;
                }

                &.active:focus {
                    border: none;
                    outline: 2px solid black;
                }

                &[type="password"] {
                    letter-spacing: 3px;
                    font-size: 1.2rem;
                }
            }
        }
    }
}
</style>
