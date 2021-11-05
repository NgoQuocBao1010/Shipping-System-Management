import Repository from "./Repository";

const resource = "/order";

const useLocalToken = () => {
    /* Use local token to authorized */
    Repository.interceptors.request.use((config) => {
        const token = localStorage.getItem("authToken");
        config.headers.Authorization = token ? `Token ${token}` : "";
        return config;
    });
};

export default {
    /* Order API call */
    get(orderId) {
        /* Get detail of an order */
        useLocalToken();
        return Repository.get(`${resource}/detail/${orderId}/`);
    },
    getPreview(orderId) {
        /* get preview of an order for an uath user */
        return Repository.get(`${resource}/preview/${orderId}/`);
    },
    getList({
        status = null,
        payment = null,
        startDate = null,
        endDate = null,
    }) {
        /* get list of orders */
        useLocalToken();
        return Repository.get(
            `${resource}/list/?status=${status}&payment=${payment}&start=${startDate}&end=${endDate}`
        );
    },
    getListAsAdmin({ profileId = null, shipper = null, status = null }) {
        /* Query list of orders correspond to user account, only admin */
        useLocalToken();
        return Repository.get(
            `${resource}/list/?status=${status}&profileId=${profileId}&shipper=${shipper}`
        );
    },
    create(data) {
        useLocalToken();
        return Repository.post(`${resource}/create/`, data);
    },
    assignOrders(data) {
        /* assign orders to driver */
        useLocalToken();
        return Repository.post(`${resource}/assign/`, data);
    },
    unassignOrders(data) {
        /* assign orders to driver */
        useLocalToken();
        return Repository.post(`${resource}/edit/`, data);
    },
    /* Price List API */
    getPrice(distance = null) {
        /* get the shipping price of given distance */
        const distanceInKm = distance / 1000;
        return Repository.get(
            `${resource}/shipping-money/?distance=${distanceInKm}`
        );
    },
    getAllPrices() {
        /* get all price list */
        return Repository.get(`${resource}/shipping-money/`);
    },
    editShippingPrice(data) {
        useLocalToken();
        return Repository.post(`${resource}/shipping-money/`, data);
    },
    deletePrice(id) {
        useLocalToken();
        return Repository.delete(`${resource}/price-edit/${id}/`);
    },
};
