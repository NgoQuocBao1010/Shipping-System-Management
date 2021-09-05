<template>
    <div class="card">
        <div class="card__profile">
            <img src="../assets/test/user-icon.jpg" alt="" />
        </div>
        <div class="card__info">
            <div class="header">
                <p class="header__name">John Doe</p>
                <div class="role driver">driver</div>
            </div>
            <div class="line"></div>
            <div class="content">
                <p>
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Eum
                    beatae quam maxime quibusdam repudiandae! Molestiae quidem
                    nihil nobis dolore minus.
                </p>

                <div class="content__btn">
                    <router-link to="#" class="btn small">
                        <i class="fas fa-plus-circle"></i>Add Task
                    </router-link>
                    <router-link to="#" class="btn small">
                        <i class="fas fa-user-circle"></i>Profile
                    </router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "EmployeeCard",
};
</script>

<style lang="scss" scoped>
.card {
    min-width: 500px;
    max-width: 800px;
    flex: 1 1 40%;
    height: 200px;
    box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px;
    display: flex;
    padding: 1rem;

    &__profile {
        flex: 1 1 30%;
        border-right: 1px solid rgb(187, 181, 181);
        display: flex;
        justify-content: center;
        align-items: center;

        img {
            width: 60%;
            aspect-ratio: 1 / 1;
            border-radius: 50%;
        }
    }

    .line {
        height: 1px;
        width: 100%;
        background: rgb(187, 181, 181);
    }

    &__info {
        flex: 1 1 70%;
        padding-left: 1rem;

        display: flex;
        flex-direction: column;

        .header {
            margin-bottom: 0.5rem;

            &__name {
                font-weight: bold;
                font-size: 1.2rem;
            }
        }

        .content {
            flex: 1 1 80%;
            padding: 0.5rem 0;
            display: flex;
            flex-direction: column;
            justify-content: space-between;

            p {
                font-size: 0.8rem;
            }

            &__btn {
                .btn {
                    margin-right: 1rem;
                }
            }
        }
    }
}
</style>
