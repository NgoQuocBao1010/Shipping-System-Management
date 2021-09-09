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
    },
    mutations: {
        authenticate(state, token) {
            state.authenticated = true;
            state.token = token;
            localStorage.setItem("authToken", token);

            console.log("Authenticated");
        },
        updateUserProfile(state, profile) {
            state.user = profile;
        },
        logout(state) {
            state.user = null;
            state.token = null;
            state.authenticated = false;
            localStorage.setItem("authToken", "");
        },
    },
    actions: {
        async login(context, token) {
            try {
                context.commit("authenticate", token);
                const response = await axios.get(
                    "http://127.0.0.1:8000/account/profile",
                    {
                        headers: {
                            Authorization: `Token ${context.state.token}`,
                        },
                    }
                );
                context.commit("updateUserProfile", response.data);
            } catch (e) {
                console.log(e);
            }
        },
    },
    modules: {},
});
