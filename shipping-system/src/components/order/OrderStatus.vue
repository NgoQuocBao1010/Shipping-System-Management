<template>
    <div class="wrapper">
        <ol class="steps" v-if="status !== 4">
            <li
                class="step"
                :class="status > 1 ? 'is-complete' : 'is-active'"
                data-step="1"
            >
                Processing
            </li>
            <li class="step" :class="deliveringClass" data-step="2">
                Delivering
            </li>
            <li class="step" :class="deliveredClass" data-step="3">
                Delivered
            </li>
        </ol>

        <ol class="steps fail" v-else>
            <li class="step is-complete">Processing</li>
            <li class="step is-complete" data-step="2">Delivering</li>
            <li class="step is-complete fail" data-step="3">
                <b>Failed to Delivered</b>
            </li>
        </ol>
    </div>
</template>

<script>
export default {
    name: "OrderStatus",
    props: {
        status: {
            type: Number,
            default: 1,
        },
    },
    computed: {
        deliveringClass() {
            if (this.status === 1) return "";
            else if (this.status === 2) return "is-active";
            else return "is-complete";
        },
        deliveredClass() {
            if (this.status < 3) return "";
            else if (this.status === 3) return "is-complete";
        },
    },
};
</script>

<style lang="scss" scoped>
.wrapper {
    margin-top: 3rem;
    width: 100%;

    $active: var(--primary-color);
    $activeBackground: var(--secondary-color);
    $completeBackground: #bee4f3;
    $mute: #e6e6e6;

    .steps {
        list-style: none;
        margin: 0;
        padding: 0;
        display: table;
        table-layout: fixed;
        width: 100%;
        color: darken($mute, 33%);
        height: 4rem;

        > .step {
            position: relative;
            display: table-cell;
            text-align: center;
            font-size: 1rem;
            font-weight: 900;
            color: #6d6875;

            &:before {
                content: attr(data-step);
                display: block;
                margin: 0 auto;
                background: #ffffff;
                border: 2px solid $mute;
                color: $mute;
                width: 2rem;
                height: 2rem;
                text-align: center;
                margin-bottom: -4.2rem;
                line-height: 1.9rem;
                border-radius: 100%;
                position: relative;
                z-index: 1;
                font-weight: 700;
                font-size: 1rem;
            }
            &:after {
                content: "";
                position: absolute;
                display: block;
                background: $mute;
                width: 100%;
                height: 0.125rem;
                top: 1rem;
                left: 50%;
            }
            &:last-child:after {
                display: none;
            }
            &.is-complete {
                color: black;

                &:before {
                    content: "\2713";
                    color: $active;
                    background: $completeBackground;
                    border: 2px solid $active;
                }
                &:after {
                    background: $active;
                }
            }
            &.is-active {
                font-size: 1.5rem;

                &:before {
                    color: #fff;
                    border: 2px solid $active;
                    background: $activeBackground;
                    margin-bottom: -4.9rem;
                }
            }
        }

        // Fail style
        &.fail {
            > .step {
                &.is-complete {
                    color: #6d6875;

                    &:before {
                        content: "\2713";
                        color: rgb(253, 52, 52);
                        background: #fdd1d4;
                        border: 2px solid rgb(253, 52, 52);
                    }
                    &:after {
                        background: rgb(253, 52, 52);
                    }
                }

                &.fail {
                    &.is-complete {
                        &:before {
                            content: "\00d7";
                            font-size: 2rem;
                        }
                    }
                }
            }
        }
    }
}
</style>
