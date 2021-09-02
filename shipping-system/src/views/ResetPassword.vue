<template>
    <div class="form-wrap">
        <form class="login">
            <h2 class="test">Reset Password</h2>
            <p>Forgot your password? Enter your email to reset it</p>
            <div class="inputs">
                <div class="input">
                    <input type="text" placeholder="Email" v-model="email" />
                    <i class="far fa-envelope icon"></i>
                </div>
                <div v-show="error" class="error">{{ this.errorMsg }}</div>
            </div>
            <button class="register-btn" @click.prevent="resetPassword">
                Reset
            </button>
            <div class="angle"></div>
        </form>
        <div class="background"></div>
    </div>
</template>

<script>
export default {
    name: "ResetPassword",
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
        resetPassword() {
            console.log("Resetting password ...");
        },
    },
};
</script>

<style lang="scss" scoped>
h2 {
    margin: 0 !important;
}

p {
    margin-top: 1rem;
    margin-bottom: 2rem;
}

button {
    margin-top: 2rem;
}
</style>
