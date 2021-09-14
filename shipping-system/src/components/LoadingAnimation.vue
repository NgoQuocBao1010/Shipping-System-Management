<template>
    <div class="load-wrapp">
        <div class="load-3">
            <div class="line"></div>
            <div class="line"></div>
            <div class="line"></div>
        </div>
    </div>
</template>

<script>
export default {
    name: "LoadingAnimation",
};
</script>

<style lang="scss">
.load-wrapp {
    min-width: max-content;

    p {
        padding: 0 0 20px;
    }

    &:last-child {
        margin-right: 0;
    }

    .line {
        display: inline-block;
        width: 10px;
        height: 10px;
        border-radius: 15px;
        margin: 0 2px;
        background-color: #4b9cdb;
    }

    .load-3 .line:nth-last-child(1) {
        animation: loadingC 0.6s 0.1s linear infinite;
    }
    .load-3 .line:nth-last-child(2) {
        animation: loadingC 0.6s 0.2s linear infinite;
    }
    .load-3 .line:nth-last-child(3) {
        animation: loadingC 0.6s 0.3s linear infinite;
    }

    @keyframes loadingC {
        0% {
            transform: translate(0, 0);
        }
        50% {
            transform: translate(0, 10px);
        }
        100% {
            transform: translate(0, 0);
        }
    }
}
</style>
