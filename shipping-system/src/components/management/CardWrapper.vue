<template>
    <div class="wrapper">
        <transition name="fade">
            <div class="profile-cards">
                <EmployeeCard
                    v-for="profile in profileList"
                    :key="profile.id"
                    :profile="profile"
                />
            </div>
        </transition>
    </div>
</template>

<script>
import EmployeeCard from "./EmployeeCard.vue";

export default {
    name: "CardWrapper",
    components: {
        EmployeeCard,
    },
    props: {
        profileList: {
            type: Array,
            default: () => [],
        },
    },
};
</script>
<style lang="scss" scoped>
.wrapper {
    width: 100%;

    .profile-cards {
        margin: auto;
        width: 100%;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1rem;
    }
}
</style>
