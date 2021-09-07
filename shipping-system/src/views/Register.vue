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
                    <input type="text" placeholder="Email" v-model="email" />
                    <i class="far fa-envelope icon"></i>
                    <!-- <email class="icon" /> -->
                </div>
                <div class="input">
                    <input
                        type="password"
                        placeholder="Password"
                        v-model="password"
                    />
                    <i class="fas fa-lock icon"></i>
                    <!-- <password class="icon" /> -->
                </div>
                <div class="input">
                    <input
                        type="password"
                        placeholder="Confirm password"
                        v-model="password2"
                    />
                    <i class="fas fa-lock icon"></i>
                    <!-- <password class="icon" /> -->
                </div>
                <div v-show="error" class="error">{{ this.errorMsg }}</div>
            </div>
            <button class="register-btn" @click.prevent="register">
                Register
            </button>
            <div class="angle"></div>
        </form>
        <div class="background"></div>
    </div>
</template>

<script>
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
        register() {
            console.log("Registering ...");
        },
        passwordValidation(password) {
            return /\d/.test(password) && password.length >= 5 ? true : false;
        },
    },
};
</script>

<style lang="scss" scoped>
.register-btn {
    margin: 2rem 0;
}
</style>
