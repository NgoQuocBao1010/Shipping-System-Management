<template>
    <div class="profile">
        <div class="profile__header">
            <h1 class="title">
                Profile Information <span class="role manager">Manager</span>
                <button class="small" @click="signOut">
                    <i class="fas fa-sign-out-alt"></i>Logout
                </button>
            </h1>
        </div>
        <form @submit.prevent="submit" class="profile__content">
            <div class="input">
                <label for="name">Full Name: </label>
                <input
                    :class="{ active: edit }"
                    name="name"
                    type="text"
                    v-model="fullName"
                    :readonly="!edit"
                    required
                />
            </div>
            <div class="input">
                <label for="email">Email: </label>
                <input
                    name="email"
                    type="email"
                    v-model="email"
                    readonly="true"
                    required
                />
            </div>
            <div class="input">
                <label for="phone">Phone Number: </label>
                <input
                    :class="{ active: edit }"
                    name="phone"
                    type="text"
                    v-model="phone"
                    :readonly="!edit"
                    required
                />
            </div>
            <div class="input">
                <label for="dob">Date of birth: </label>
                <input
                    name="dob"
                    type="date"
                    v-model="dateOfBirth"
                    :readonly="!edit"
                    :class="{ active: edit }"
                />
            </div>
            <div class="input">
                <label for="address">Address: </label>
                <input
                    :class="{ active: edit }"
                    name="address"
                    type="text"
                    v-model="address"
                    :readonly="!edit"
                />
            </div>
            <div class="input">
                <label for="subdistrict">Sub-district</label>
                <div class="select" :class="{ active: edit }">
                    <i class="fas fa-chevron-down"></i>
                    <select
                        name="subdistrict"
                        v-model="subDistrictId"
                        :disabled="!edit"
                    >
                        <option
                            v-for="subDistrict in subDistricts"
                            :key="subDistrict.code"
                            :value="subDistrict.code"
                        >
                            {{ subDistrict.name }}
                        </option>
                    </select>
                </div>
            </div>
            <div class="input">
                <label for="province">Province - District</label>
                <div class="select" :class="{ active: edit }">
                    <i class="fas fa-chevron-down"></i>
                    <select
                        name="province"
                        v-model="districtId"
                        :disabled="!edit"
                    >
                        <option
                            v-for="dstr in districts"
                            :key="dstr.disCode"
                            :value="dstr.disCode"
                        >
                            {{ dstr.name }}
                        </option>
                    </select>
                </div>
            </div>

            <loading-animation class="animation" v-show="animate" />
            <div class="edit-buttons">
                <div class="btn small" @click="edit = true" v-show="!edit">
                    <i class="far fa-edit"></i>Edit
                </div>
                <div class="btn small editing" v-show="edit">
                    <i class="far fa-edit"></i>Editing ...
                </div>
                <button
                    class="btn small"
                    type="submit"
                    @click="edit = false"
                    v-show="edit"
                >
                    <i class="fas fa-save"></i>Save
                </button>
            </div>
        </form>
    </div>
</template>

<script>
import { mapState, mapMutations } from "vuex";
import axios from "axios";

import LoadingAnimation from "../../components/LoadingAnimation.vue";

export default {
    name: "Profile",
    components: {
        LoadingAnimation,
    },
    data() {
        return {
            fullName: "",
            email: "",
            dateOfBirth: "",
            phone: "",
            address: "",
            provinceId: null,
            districtId: null,
            subDistrictId: null,
            edit: false,
            animate: false,

            districts: [],
            subDistricts: [],
        };
    },
    computed: {
        ...mapState(["user", "token"]),
    },
    watch: {
        districtId(newVal, oldVal) {
            if (oldVal) {
                this.provinceId = this.districts.find(
                    (info) => info.disCode === newVal
                ).proCode;

                this.subDistrictId = "";

                this.getSubDistricts(newVal)
                    .then((response) => {
                        this.subDistricts = response.data.wards;
                    })
                    .catch((error) => console.log(error));
            }
        },
    },
    methods: {
        ...mapMutations(["logout", "authenticate"]),
        getAllProvinces() {
            const url = `https://provinces.open-api.vn/api/?depth=2`;
            axios
                .get(url)
                .then((response) => {
                    const provinces = response.data;

                    // Get info from api then rearrange it to get the info for Can Tho city to the front
                    let results = [];
                    let ctInfo = [];

                    for (let province of provinces) {
                        for (let district of province.districts) {
                            const disObj = {
                                proCode: province.code,
                                disCode: district.code,
                                name: `${district.name} - ${province.name}`,
                            };

                            if (province.code === 92) ctInfo.push(disObj);
                            else results.push(disObj);
                        }
                    }

                    this.districts = [...ctInfo, ...results];
                })
                .catch((error) => console.log(error));
        },
        getSubDistricts(districtCode) {
            const url = `https://provinces.open-api.vn/api/d/${districtCode}/?depth=2`;

            return axios.get(url);
        },
        signOut() {
            this.logout();
            this.$router.push({ name: "Home" });
        },
        async submit() {
            const profileForm = {
                email: this.email,
                fullName: this.fullName,
                gender: this.gender,
                dateOfBirth: this.dateOfBirth,
                phone: this.phone,
                address: this.address,
                provinceId: this.provinceId,
                districtId: this.districtId,
                subDistrictId: this.subDistrictId,
            };

            try {
                this.animate = true;
                const url = "http://127.0.0.1:8000/account/profile";
                const response = await axios.post(url, profileForm, {
                    headers: {
                        Authorization: `Token ${this.token}`,
                    },
                });

                if (response.status === 200) {
                    this.authenticate({ profile: profileForm });
                }

                this.animate = false;
            } catch (e) {
                console.log(e);
            }
        },
    },
    mounted() {
        ({
            email: this.email,
            fullName: this.fullName,
            gender: this.gender,
            dateOfBirth: this.dateOfBirth,
            phone: this.phone,
            address: this.address,
            provinceId: this.provinceId,
            districtId: this.districtId,
            subDistrictId: this.subDistrictId,
        } = this.user);

        this.districtId = this.districtId === null ? -1 : this.districtId;

        // Get address information from API
        this.getAllProvinces();
        if (this.districtId !== -1)
            this.getSubDistricts(this.districtId)
                .then((response) => {
                    this.subDistricts = response.data.wards;
                })
                .catch((error) => console.log(error));
    },
};
</script>

<style lang="scss" scoped>
.profile {
    &__header {
        display: flex;
        justify-content: space-between;
        margin-bottom: 0.8rem;
        position: relative;

        .title {
            font-size: 1.5rem;

            display: flex;
            align-items: center;
            gap: 3rem;
        }

        button {
            background: rgb(223, 71, 71);
            font-weight: 600;
            position: absolute;
            right: 10px;
        }
    }

    &__content {
        padding: 2rem;
        display: flex;
        flex-direction: column;
        box-shadow: rgba(17, 17, 26, 0.05) 0px 1px 0px,
            rgba(17, 17, 26, 0.1) 0px 0px 8px;
        position: relative;

        .input {
            display: flex;
            align-items: center;

            label {
                margin-right: 2rem;
                width: 200px;
            }

            input {
                flex: 1 1 300px;
                max-width: 400px;
                line-height: 2;
                padding: 0 5px;
                margin-bottom: 1rem;
                font-size: 1rem;
                font-weight: 600;
                border: none;
                border-bottom: 1px solid black;

                &:focus {
                    outline: none;
                }

                &.active,
                &.active:focus {
                    border: none;
                    outline: 2px solid black;
                }

                &[type="password"] {
                    letter-spacing: 3px;
                    font-size: 1.2rem;
                }
            }

            .select {
                padding: 8px 5px;
                width: 100%;
                margin-bottom: 1rem;
                max-width: 400px;
                font-size: var(--input-font-size);
                font-weight: 600;
                line-height: 1.2rem;
                outline: none;
                border-bottom: 1px solid black !important;
                position: relative;

                &:focus {
                    border: 1px solid black !important;
                    outline: none;
                }

                i {
                    position: absolute;
                    cursor: pointer;
                    right: 10px;
                    top: 50%;
                    transform: translateY(-50%);
                    z-index: -1;
                    opacity: 0;
                }

                select {
                    cursor: initial;
                    width: 100%;
                    font-size: var(--input-font-size);
                    font-weight: 600;
                    line-height: 1.2rem;
                    background: transparent;

                    &:disabled {
                        opacity: 1;
                        color: black;
                    }
                }

                &.active {
                    border-bottom: none !important;
                    border: 2px solid black !important;

                    i {
                        opacity: 1;
                    }

                    select {
                        cursor: pointer;
                    }
                }
            }
        }

        .edit-buttons {
            position: absolute;
            top: 40px;
            right: 20px;
            display: flex;
            flex-direction: column;

            > * {
                margin: 0.5rem 0;
                font-weight: bold;

                &.editing {
                    background: rgb(51, 187, 51);
                    cursor: initial;
                }
            }
        }

        .animation {
            position: absolute;
            top: 15px;
            right: 30px;
        }
    }
}
</style>
