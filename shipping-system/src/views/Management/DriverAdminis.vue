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
                        v-model="driver.name"
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
            <div class="content">
                <form>
                    <div class="inputs">
                        <label for="password">Confirm your password</label>
                        <input
                            type="password"
                            autocomplete="new-password"
                            v-model="confirmPassword"
                        />
                    </div>
                </form>

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
import { required, numeric, minLength } from "vuelidate/lib/validators";

export default {
    name: "Driver",
    components: {
        Modal: () => ({
            component: import("../../components/Modal.vue"),
            delay: 5000,
        }),
    },
    data() {
        return {
            driver: {
                name: "",
                license: "",
            },
            error: null,

            userConfirmation: false,
            confirmPassword: "",
        };
    },
    validations: {
        driver: {
            name: { required },
            license: { required, minLength: minLength(5) },
        },
    },
    methods: {
        submit() {
            this.$v.$touch();

            if (this.$v.$error) {
                this.error = true;
                return;
            }

            this.userConfirmation = true;
            this.error = null;
        },
        createAccount() {
            console.log("Confirmed");
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

                .error {
                    width: max-content;
                    color: red;
                    font-weight: 600;
                    position: absolute;
                    right: 0;
                    top: 0;
                    transform: translate(120%, 40%);
                    cursor: initial;
                }
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

                @media only screen and (min-width: 1700px) {
                    max-width: 500px;
                }

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

    .content {
        width: 100%;
        margin: 2rem 0;

        p {
            font-style: italic;
        }
    }
}
</style>
