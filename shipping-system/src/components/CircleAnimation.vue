<template>
    <div class="wrapper">
        <div class="loading2" :class="[size]"></div>
    </div>
</template>

<script>
export default {
    name: "CircleAnimation",
    props: {
        size: {
            type: String,
            default: "small",
        },
    },
};
</script>

<style lang="scss" scoped>
.wrapper {
    max-width: 100px;
    min-height: 20px;

    .small {
        width: 30px;
        border-width: 4px !important;
        aspect-ratio: 1 / 1;
    }

    .large {
        width: 100px;
        border-width: 8px !important;
        aspect-ratio: 1 / 1;
    }

    .loading1 {
        border-radius: 50%;
        border: 8px solid;
        border-color: var(--primary-color) transparent transparent;
        // border-color: var(--primary-color) rgba(255, 255, 255, 0.1)
        //     rgba(255, 255, 255, 0.1);
        animation: spin 1s ease infinite;
    }

    .loading2 {
        border-radius: 50%;
        border-top: 8px solid;
        border-right: 8px solid;
        border-color: var(--primary-color) transparent;
        animation: spin 1s linear infinite;
    }

    .loading3 {
        border-radius: 50%;
        border: 8px solid;
        border-color: var(--primary-color) transparent var(--primary-color);
        animation: spin 1s ease-in-out infinite;
    }
}

@keyframes spin {
    0% {
        transform: rotate(0deg);
    }

    100% {
        transform: rotate(359deg);
    }
}
</style>
