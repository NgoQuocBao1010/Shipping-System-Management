<template>
    <div class="management">
        <div class="management__header">
            <h1 class="title">Employee</h1>
            <div class="btn-header">
                <button><i class="fas fa-plus-circle"></i>Add Employee</button>
                <button>Status</button>
            </div>
        </div>
        <hr />
        <div class="management__content">
            <EmployeeCard />
            <EmployeeCard />
            <EmployeeCard />
            <EmployeeCard />
            <EmployeeCard />
        </div>
    </div>
</template>

<script>
import EmployeeCard from "../components/EmployeeCard.vue";
export default {
    name: "Management",
    components: {
        EmployeeCard,
    },
};
</script>

<style lang="scss" scoped>
.management {
    &__header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 0.8rem;

        .title {
            font-size: 1.5rem;
        }

        .btn-header {
            button {
                padding-left: 1rem;
                padding-right: 1rem;
                margin: 0 0.5rem;
                border-radius: 10px;

                i {
                    margin-right: 0.5rem;
                }
            }
        }
    }

    &__content {
        padding: 2rem 0;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 1.5rem;
    }
}
</style>
