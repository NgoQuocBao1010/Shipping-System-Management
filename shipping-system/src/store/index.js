import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        orders: [
            {
                id: 1,
                date: "22/06/2021",
                consignor: "Nguyễn Quần",
                consignorPhone: "0939983979",
                placeOfReceipt: "số 5, Phan Đình Phùng, Ô Môn, Cần Thơ",
                consignee: "Phan Nhân",
                consigneePhone: "0939983979",
                placeOfDelivery: "số 10, Nguyễn Trãi, Ô Môn, Cần Thơ",
                paymentMethod: "Pay by consignee",
                shipper: "Trần Trung",
                status: 1,
            },
            {
                id: 2,
                date: "15/06/2021",
                consignor: "Nguyễn Áo",
                consignorPhone: "0939983979",
                placeOfReceipt: "số 5, Phan Đình Phùng, Ô Môn, Cần Thơ",
                consignee: "Phan Lập",
                consigneePhone: "0939983979",
                placeOfDelivery: "số 10, Nguyễn Trãi, Ô Môn, TP Hồ Chí Minh",
                paymentMethod: "Pay by consignor",
                shipper: "Ng Trung",
                status: 1,
            },
            {
                id: 3,
                date: "22/01/2021",
                consignor: "Nguyễn Giày",
                consignorPhone: "0939983979",
                placeOfReceipt: "số 5, Phan Đình Phùng, Ô Môn, Hà Nội",
                consignee: "Phan Phan",
                consigneePhone: "0939983979",
                placeOfDelivery: "số 10, Nguyễn Trãi, Ô Môn, Cần Thơ",
                paymentMethod: "Pay by consignee",
                shipper: "Bùi Trung",
                status: 0,
            },
        ],
        user: null,
        token: null,
        authenticated: false,

        // Current location
        currentLocation: {
            longitude: 105.7842959,
            latitude: 10.0171277,
        },

        // Provinces
        provinces: null,
    },
    mutations: {
        authenticate(state, authInfo) {
            // Authenticate: Store auth token and user information

            if (authInfo.token) {
                state.authenticated = true;
                state.token = authInfo.token;
                localStorage.setItem("authToken", authInfo.token);
            }

            state.user = authInfo.profile;
            console.log("Global store: Authenticated");
        },
        logout(state) {
            // Logging out: Set all auth information to null
            state.user = null;
            state.token = null;
            state.authenticated = false;
            localStorage.setItem("authToken", "");
        },
        saveProviceInfo(state, data) {
            // Save all the provice data from api call
            state.provinces = data;
        },
    },
    actions: {
        async login(context, token) {
            // API call to get user token and information
            try {
                const response = await axios.get(
                    "http://127.0.0.1:8000/account/profile",
                    {
                        headers: {
                            Authorization: `Token ${token}`,
                        },
                    }
                );

                const authInfo = {
                    token,
                    profile: response.data,
                };

                context.commit("authenticate", authInfo);
                return true;
            } catch (e) {
                console.log("Error login in: ", e.response);
                context.commit("logout");
                return false;
            }
        },
        async getProvinceInfo(context) {
            try {
                // Open API url to get all provinces and their districts
                const url = `https://provinces.open-api.vn/api/?depth=2`;
                const response = await axios.get(url);

                const provicesData = [];

                // Restructure response api data
                response.data.forEach((provinceData) => {
                    provinceData.districts.forEach((districtData) => {
                        const district = {
                            name: `${districtData.name}, ${provinceData.name}`,
                            id: districtData.code,
                            province_code: provinceData.code,
                        };
                        provicesData.push(district);
                    });
                });

                context.commit("saveProviceInfo", provicesData);
            } catch (e) {
                console.log("Error get province info");
            }
        },
    },
    modules: {},
});
