<template>
    <div class="wrapper">
        <div class="profile">
            <q-icon name="person"></q-icon>
            <div class="information">
                <p>Full name: {{ user.fullName }}</p>
                <p>Phone Number: {{ user.phone }}</p>
                <p>Driver License: {{ user.driverLicense }}</p>
            </div>
        </div>
    </div>
</template>

<script>
import { mapState } from "vuex";

export default {
    name: "PageIndex",
    components: {},
    data: () => ({}),
    computed: {
        ...mapState(["user"]),
    },
};
</script>

<style lang="scss" scoped>
p {
    margin: 0;
    padding: 0;
}

.profile {
    display: flex;
    justify-content: center;
    margin: 1rem;

    i {
        font-size: 3rem;
    }

    .information {
        margin: 0 1rem;

        p {
            margin-bottom: 1rem;
        }
    }
}
</style>
