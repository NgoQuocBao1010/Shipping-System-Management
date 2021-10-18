<template>
    <div class="management">
        <div class="management__header">
            <h1 class="title">Human Resources Management</h1>
            <div class="btn-header">
                <button><i class="fas fa-plus-circle"></i>Add Employee</button>
                <button>Status</button>
            </div>
        </div>

        <!-- Content -->
        <div class="management__content">
            <TabWrapper>
                <Tab title="Tab 1">Hello From Tab 1</Tab>
                <Tab title="Tab 2">Hello From Tab 2</Tab>
                <Tab title="Tab 3">Hello From Tab 3</Tab>
                <Tab title="Tab 4">Hello From Tab 4</Tab>
            </TabWrapper>
        </div>
    </div>
</template>

<script>
import { mapState } from "vuex";
import axios from "axios";

import EmployeeCard from "@/components/EmployeeCard.vue";
import TabWrapper from "@/components/management/TabWrapper.vue";
import Tab from "@/components/management/Tab.vue";

export default {
    name: "Management",
    components: {
        EmployeeCard,
        TabWrapper,
        Tab,
    },
    computed: {
        ...mapState(["token"]),
    },
    async created() {
        try {
            const url = "http://127.0.0.1:8000/account/staff";
            const response = await axios.get(url, {
                headers: {
                    Authorization: `Token ${this.token}`,
                },
            });

            console.log(response.data);
        } catch (e) {
            console.log(e);
        }
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
