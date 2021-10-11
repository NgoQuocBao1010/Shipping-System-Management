<template>
    <div class="form-wrap">
        <form @submit.prevent="signIn" class="login">
            <p class="login-register" v-show="!newUserCreated">
                Don't have an account?
                <router-link class="router-link" :to="{ name: 'Register' }">
                    Register
                </router-link>
            </p>
            <p class="account-created" v-show="newUserCreated">
                Account Created Successfully
            </p>
            <h2>Login to Kaz Shipping System</h2>
            <div class="inputs">
                <div class="input">
                    <input
                        type="text"
                        required
                        placeholder="Email"
                        v-model="email"
                    />
                    <i class="far fa-envelope icon"></i>
                </div>
                <div class="input">
                    <input
                        type="password"
                        required
                        placeholder="Password"
                        v-model="password"
                    />
                    <i class="fas fa-lock icon"></i>
                </div>
                <div v-show="error" class="error">{{ this.errorMsg }}</div>
            </div>
            <router-link
                class="forgot-password"
                :to="{ name: 'ResetPassword' }"
            >
                Forgot your password?
            </router-link>
            <button type="submit">Sign In</button>
            <div class="angle"></div>
        </form>
        <div class="background"></div>
    </div>
</template>

<script>
import { mapActions } from "vuex";
import axios from "axios";

export default {
    name: "Login",
    props: {
        newUserCreated: Boolean,
    },
    data() {
        return {
            error: null,
            errorMsg: "",
            email: "",
            password: "",
        };
    },
    methods: {
        ...mapActions(["login"]),
        async signIn() {
            try {
                const formInfo = {
                    email: this.email,
                    password: this.password,
                };

                const url = `http://127.0.0.1:8000/account/login`;
                const response = await axios.post(url, formInfo);
                const authToken = response.data.auth_token;

                await this.login(authToken);

                this.$router.push({ name: "Reports" });
            } catch (e) {
                console.log("Error loggin in", e);
                this.error = true;
                this.errorMsg = e.response.data.message;
            }
        },
    },
};
</script>

<style lang="scss">
.form-wrap {
    overflow: hidden;
    display: flex;
    height: 100vh;
    justify-content: center;
    align-self: center;
    margin: 0 auto;
    width: 90%;

    @media (min-width: 900px) {
        width: 100%;
    }
    .login-register {
        margin-bottom: 32px;
        .router-link {
            color: #000;
        }
    }
    .account-created {
        margin-bottom: 32px;
        font-weight: bold;
        color: var(--primary-color);
    }
    form {
        padding: 0 10px;
        position: relative;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        flex: 1;
        @media (min-width: 900px) {
            padding: 0 50px;
        }
        h2 {
            text-align: center;
            font-size: 32px;
            color: #303030;
            margin-bottom: 40px;
            @media (min-width: 900px) {
                font-size: 40px;
            }
        }
        .inputs {
            width: 100%;
            max-width: 350px;
            .input {
                position: relative;
                display: flex;
                justify-content: center;
                align-items: center;
                margin-bottom: 8px;
                input {
                    font-size: 16px;
                    width: 100%;
                    border: none;
                    background-color: #f2f7f6;
                    padding: 4px 4px 4px 30px;
                    height: 50px;
                    &:focus {
                        outline: none;
                    }
                }
                .icon {
                    width: 12px;
                    position: absolute;
                    left: 6px;
                }
            }
            .error {
                font-size: 12px;
                font-weight: 500;
                color: red;
                text-align: center;
            }
        }
        .forgot-password {
            text-decoration: none;
            color: #000;
            cursor: pointer;
            font-size: 14px;
            margin: 16px 0 32px;
            border-bottom: 1px solid transparent;
            transition: 0.5s ease all;
            &:hover {
                border-color: #303030;
            }
        }
        .angle {
            display: none;
            position: absolute;
            background-color: #fff;
            transform: rotateZ(3deg);
            width: 60px;
            right: -30px;
            height: 101%;
            @media (min-width: 900px) {
                display: initial;
            }
        }
    }
    .background {
        display: none;
        flex: 2;
        background-size: cover;
        background-image: url("../../assets/background.jpg");
        width: 100%;
        height: 100%;
        @media (min-width: 900px) {
            display: initial;
        }
    }
}
</style>
