<template>
    <div class="form-wrap">
        <form class="login">
            <p class="login-register">
                Already have an account?
                <router-link class="router-link" :to="{ name: 'Login' }">
                    Login
                </router-link>
            </p>
            <h2>Register to Kaz Shipping System</h2>
            <div class="inputs">
                <div class="input">
                    <input
                        type="email"
                        autocomplete="nope"
                        placeholder="Email"
                        v-model="email"
                    />
                    <i class="far fa-envelope icon"></i>
                </div>
                <div class="input">
                    <input
                        type="password"
                        placeholder="Password"
                        autocomplete="new-password"
                        v-model="password"
                        required
                    />
                    <i class="fas fa-lock icon"></i>
                </div>
                <div class="input">
                    <input
                        type="password"
                        placeholder="Confirm password"
                        v-model="password2"
                    />
                    <i class="fas fa-lock icon"></i>
                </div>
                <div v-show="error" class="error">{{ this.errorMsg }}</div>
            </div>
            <button class="register-btn" @click.prevent="register">Register</button>
            <div class="angle"></div>
        </form>
        <div class="background"></div>
    </div>
</template>

<script>
import axios from "axios";
export default {
    name: "Register",
    data() {
        return {
            error: null,
            errorMsg: "",
            email: "",
            password: "",
            password2: "",
        };
    },
    methods: {
        async register() {
            if (!this.validateEmail(this.email)) {
                this.error = true;
                this.errorMsg = "Please provide a valid email";
                return;
            }

            if (!this.passwordValidation(this.password)) {
                this.error = true;
                this.errorMsg =
                    "Password needs to be at least 5 letter long and contains numeric values";
                return;
            }

            if (this.password !== this.password2) {
                this.error = true;
                this.errorMsg = "Password fields don't match!";
                return;
            }

            this.error = false;
            this.errorMsg = "";

            const registerInfo = {
                email: this.email,
                password: this.password,
            };

            try {
                const url = "https://127.0.0.1:8000/account/register";
                const response = await axios.post(url, registerInfo);

                if (response.status === 200) {
                    this.$router.replace({
                        name: "Login",
                        params: { newUserCreated: true, newEmail: this.email },
                    });

                    this.$toast.success("Your accout is successfully created!", {
                        duration: 4000,
                    });
                }
            } catch (e) {
                if (e.response.status === 400) {
                    this.error = true;
                    this.errorMsg = `${e.response.data.errors.email[0]}, please try another email`;
                }
            }
        },
        // Validation input
        passwordValidation(password) {
            return /\d/.test(password) && password.length >= 5 ? true : false;
        },
        validateEmail(email) {
            const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            return re.test(String(email).toLowerCase());
        },
    },
};
</script>

<style lang="scss" scoped>
.register-btn {
    margin: 2rem 0;
}
</style>
