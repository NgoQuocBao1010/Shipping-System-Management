<template>
    <q-layout view="lHh Lpr lFf">
        <Nav />
        <q-page-container>
            <router-view />
        </q-page-container>
    </q-layout>
</template>

<script>
import Nav from "components/Nav.vue";

export default {
    name: "MainLayout",
    components: { Nav },
    data() {
        return {};
    },
};
</script>
