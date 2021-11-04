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
    // GET method
    get(orderId) {
        /* Get detail of an order */
        useLocalToken();
        return Repository.get(`${resource}/detail/${orderId}/`);
    },
    getList(status = null, payment = null, startDate = null, endDate = null) {
        /* get list of orders */
        useLocalToken();
        return Repository.get(
            `${resource}/list/?status=${status}&payment=${payment}&start=${startDate}&end=${endDate}`
        );
    },
    getPrice(distance) {
        /* get the shipping price of given distance */
        const distanceInKm = distance / 1000;
        return Repository.get(
            `${resource}/shipping-money/?distance=${distanceInKm}`
        );
    },
    // POST method
    create(data) {
        useLocalToken();
        return Repository.post(`${resource}/create/`, data);
    },
};
