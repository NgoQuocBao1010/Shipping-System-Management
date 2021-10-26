<template>
    <div class="assign">
        <div class="driver__intro">
            <EmployeeCard />
        </div>
    </div>
</template>

<script>
import EmployeeCard from "@/components/management/EmployeeCard.vue";

export default {
    name: "OrderAssign",
    components: {
        EmployeeCard,
    },
};
</script>

<style lang="scss" scoped></style>
