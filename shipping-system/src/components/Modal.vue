<template>
    <transition name="modal-wrapper-animation">
        <div v-show="active" class="modal-wrapper" :class="size">
            <transition name="modal-animation">
                <div v-show="active" class="modal" :class="size">
                    <!-- Headers -->
                    <div class="header">
                        {{ header }}
                        <i
                            class="far fa-times-circle"
                            @click="$emit('toggle')"
                        ></i>
                    </div>

                    <!-- Content -->
                    <div class="content">
                        <slot>Content of modal</slot>
                    </div>

                    <!-- Footer -->
                    <div class="footer">
                        <button v-if="submit" @click="$emit('submit')">
                            {{ submit }}
                        </button>
                        <button class="close" @click="$emit('toggle')">
                            Close
                        </button>
                    </div>
                </div>
            </transition>
        </div>
    </transition>
</template>

<script>
export default {
    name: "Modal",
    props: {
        active: {
            type: Boolean,
            default: false,
        },
        header: {
            type: String,
            default: "Modal Header",
        },
        /* 
            If this modal is used to submit something, define a string for the submit button
            Also provide an method to handle the submit button
        */
        submit: {
            type: String,
            default: null,
        },
        size: {
            type: String,
            default: "",
        },
    },
};
</script>

<style lang="scss" scoped>
.modal-wrapper {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.3);
    z-index: 1000;
    padding-top: 2rem;
    overflow-y: scroll;
    display: flex;
    justify-content: center;

    &.small {
        align-items: center;
    }

    .modal {
        width: 70%;
        height: max-content;
        max-width: 1200px !important;
        padding: 1rem 2rem;
        border-radius: 10px;
        margin-bottom: 1rem;

        background: #fff;

        display: flex;
        flex-direction: column;
        justify-content: space-between;

        &.small {
            width: 50%;
        }

        > * {
            width: 100%;
        }

        .header {
            padding: 8px 16px;
            text-align: center;
            font-size: 1.5rem;
            font-weight: bold;
            position: relative;

            i {
                position: absolute;
                top: 0;
                right: 0;
                font-size: 1.5rem;
                cursor: pointer;
                color: rgb(223, 84, 84);
            }
        }

        .footer {
            display: flex;
            gap: 2rem;
        }
    }
}

.modal-wrapper-animation-enter-active,
.modal-wrapper-animation-leave-active {
    transition: all 0.3s ease-out;
}

.modal-wrapper-animation-enter,
.modal-wrapper-animation-leave-to {
    opacity: 0;
}

.modal-animation-enter-active,
.modal-animation-leave-active {
    transition: all 0.3s ease-out 0.15s;
}

.modal-animation-enter,
.modal-animation-leave-to {
    transform: scale(0.7);
    opacity: 0;
}

.modal-animation-enter-to {
    transform: scale(1);
}
</style>
