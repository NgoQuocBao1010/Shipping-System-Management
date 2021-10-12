<template>
    <transition name="modal-wrapper-animation">
        <div v-show="active" class="modal-wrapper">
            <transition name="modal-animation">
                <div v-show="active" class="modal">
                    <div class="header">
                        {{ header }}
                        <i
                            class="far fa-times-circle"
                            @click="$emit('toggle')"
                        ></i>
                    </div>

                    <div class="content">
                        <slot>Content of modal</slot>
                    </div>

                    <div class="footer">
                        <button class="small">Close</button>
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
    }
}
</style>
