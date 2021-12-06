<template>
    <div id="q-app">
        <transition name="fade">
            <router-view />
        </transition>
    </div>
</template>

<script>
export default {
    name: "App",
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;500;600;700&display=swap");

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Quicksand", sans-serif;
    font-weight: bold;
}

:root {
    --primary-color: #1190cb;
    --secondary-color: #7dccff;
    --dark-color: #362222;
    --white: #ffffff;
}

.btn,
button {
    padding: 0.5rem 2rem;
    border: none;
    text-decoration: none;
    border-radius: 20px;
    font-size: 16px;
    color: #fff;
    background-color: var(--primary-color);
    cursor: pointer;
    transition: 0.3s ease-in-out all;

    i {
        margin-right: 5px;
        font-size: 0.8rem;
    }

    &.small {
        padding: 0.5rem 1rem;
        border-radius: 5px;
        font-size: 12px;
    }
}

.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.5s ease-in;
}
.fade-enter,
.fade-leave-to {
    opacity: 0;
}
</style>
