<template>
    <div class="wrapper">
        <img src="../assets/Color logo - no background.png" alt="" class="logo" />
        <form action="" @submit.prevent="login">
            <div class="input">
                <q-icon name="account_circle"></q-icon>
                <input
                    v-model="user.email"
                    type="text"
                    placeholder="Enter your driver account"
                />
            </div>
            <div class="input">
                <q-icon name="vpn_key"></q-icon>
                <input
                    v-model="user.password"
                    type="password"
                    placeholder="Enter your password"
                />
            </div>

            <button class="btn">Login</button>
        </form>

        {{ token }}
    </div>
</template>
<script>
import axios from "axios";

export default {
    name: "Login",
    data: () => ({
        user: {
            email: "",
            password: "",
        },
        token: "",
    }),
    methods: {
        async login() {
            try {
                const url = `http://10.0.2.2:8000/account/login`;
                const response = await axios.post(url, this.user);
                this.token = response.data.auth_token;

                this.$q.notify({
                    type: "positive",
                    message: `Login successfully`,
                    position: "top",
                    timeout: 1000,
                });
            } catch (e) {
                console.log(e);
            }
        },
    },
};
</script>
<style lang="scss" scoped>
.wrapper {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    .logo {
        max-width: 40%;
    }

    form {
        margin: 1rem 0;
        width: 70%;
        display: flex;
        flex-direction: column;

        .input {
            width: 100%;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            position: relative;

            i {
                font-size: 2rem;
                position: absolute;
                left: 2px;
                color: var(--primary-color);
            }

            input {
                font-size: 1rem;
                flex: 1;
                padding: 10px 0;
                padding-left: 2.5rem;
                border-radius: 5px;
                border: 1px solid var(--primary-color);

                &:focus {
                    outline: none;
                    border: 2px solid var(--primary-color);
                }
            }
        }

        button {
            margin: 1rem 0;
        }
    }
}
</style>
