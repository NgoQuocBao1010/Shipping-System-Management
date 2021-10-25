<template>
    <div class="driver">
        <h1>Create an account for your drivers</h1>

        <!-- Main content -->
        <div class="driver__content">
            <!-- Driver form -->
            <form class="driver__form">
                <div class="inputs">
                    <label for="driver-name">Driver Name</label>
                    <input
                        name="driver-name"
                        v-model="driver.fullName"
                        type="text"
                    />
                </div>

                <div class="inputs">
                    <label for="driver-license">Driver License</label>
                    <input
                        name="driver-license"
                        v-model="driver.license"
                        type="text"
                    />
                </div>

                <button type="submit" @click.prevent="submit">
                    Create
                    <p v-show="error" class="error">
                        <i class="fas fa-exclamation-circle"></i>
                        Please fill all of your information
                    </p>
                </button>
            </form>

            <div class="hero-image">
                <img src="../../assets/driver.jpg" alt="" />
            </div>
        </div>

        <!-- Modal section -->
        <Modal
            header="User Confirmation"
            size="small"
            :active="userConfirmation"
            @toggle="userConfirmation = false"
            submit="Confirm"
            @submit="createAccount"
        >
            <!-- Modal content -->
            <div class="content">
                <!-- Verify password form -->
                <form @submit.prevent="createAccount">
                    <div class="inputs">
                        <label for="password">
                            Enter your password for <b>{{ email }}</b>
                        </label>
                        <input type="password" v-model="confirmPassword" />
                    </div>

                    <p class="error" v-show="passwordError">
                        {{ passwordError }}
                    </p>
                </form>

                <!-- Instruction -->
                <p>
                    *** This action will create an account that could
                    potentially has access to your important data. Please
                    confirm your password to confirm your action. ***
                </p>
            </div>
        </Modal>
    </div>
</template>

<script>
import { required, minLength } from "vuelidate/lib/validators";
import axios from "axios";

export default {
    name: "Driver",
    components: {
        Modal: () => import("../../components/Modal.vue"),
        LoadingAnimation: () => import("../../components/CircleAnimation.vue"),
    },
    data() {
        return {
            driver: {
                fullName: "",
                license: "",
            },
            error: null,

            userConfirmation: false,
            confirmPassword: "",
            passwordError: null,

            verifyToken: null,
        };
    },
    computed: {
        email() {
            return this.$store.getters.email;
        },
    },
    validations: {
        driver: {
            fullName: { required },
            license: { required, minLength: minLength(5) },
        },
    },
    methods: {
        submit() {
            /* Validation create driver form */
            this.$v.$touch();

            if (this.$v.$error) {
                this.error = true;
                return;
            }

            this.userConfirmation = true;
            this.error = null;
        },
        async createAccount() {
            /* Make an API call to verify passoword */
            if (!this.confirmPassword) {
                this.passwordError = "Please input your password!";

                return;
            }

            try {
                const formInfo = {
                    email: this.email,
                    password: this.confirmPassword,
                };

                const url = `http://127.0.0.1:8000/account/login`;
                const response = await axios.post(url, formInfo);

                this.verifyToken = response.data.auth_token;
                await this.createDriver();
                this.passwordError = null;
            } catch (e) {
                console.log(e.response);

                if (e.response.status === 400)
                    this.passwordError = "Your password is incorrent";
            }
        },
        async createDriver() {
            /* Make API call to create driver */
            try {
                const url = "http://127.0.0.1:8000/account/driver/add";
                const response = await axios.post(url, this.driver, {
                    headers: {
                        Authorization: `Token ${this.verifyToken}`,
                    },
                });

                if (response.status === 200) {
                    this.$toast.success(
                        `Successfully created an account for ${this.driver.fullName}`
                    );
                    this.$router.push({ name: "Management" });
                }
            } catch (e) {
                console.log(e.response);
            }
        },
    },
};
</script>

<style lang="scss" scoped>
.driver {
    &__content {
        margin: 1rem 0;
        display: flex;
        gap: 2rem;

        form {
            padding: 1rem 2rem;
            flex: 1 1 800px;
            max-width: 800px;
            border-radius: 20px;
            box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px,
                rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;

            button {
                margin-top: 2rem;
                position: relative;
            }

            .error {
                position: absolute;
                right: 0;
                top: 0;
                transform: translate(120%, 40%);
            }
        }

        .hero-image {
            flex: 1 1 500px;
            height: 100%;
            padding: 1rem 0;

            display: flex;
            justify-content: center;
            align-items: center;

            img {
                width: 100%;
                max-width: 300px;

                border-radius: 20px;
            }
        }
    }

    .inputs {
        width: 100%;
        display: flex;
        flex-direction: column;
        margin: 1rem 0;

        label {
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 5px;
            color: var(--primary-color);
        }

        input {
            font-size: 1.4rem;
            font-weight: 500;
            padding: 8px 12px;
            border: 2px solid rgb(138, 135, 135);

            &:focus {
                border: none;
                outline: none;
                border: 2px solid var(--primary-color);
            }
        }
    }

    .error {
        width: max-content;
        color: red;
        font-weight: 600;
        font-style: normal;
        cursor: initial;
    }

    .content {
        width: 100%;
        margin: 2rem 0;

        p {
            font-style: italic;
        }
    }
}
</style>
