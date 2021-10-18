<template>
    <div v-show="isActive">
        <slot></slot>
    </div>
</template>

<script>
export default {
    name: "Tab",
    props: {
        title: {
            type: String,
            default: "Tab",
        },
    },
    data() {
        return {
            isActive: true,
        };
    },
};
</script>

<style lang="scss" scoped></style>
