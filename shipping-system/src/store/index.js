import Vue from "vue";
import Vuex from "vuex";

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
    },
    mutations: {},
    actions: {},
    modules: {},
});
