import Repository from "./Repository";

const resource = "/account";

const useLocalToken = () => {
    /* Use local token to authorized */
    Repository.interceptors.request.use((config) => {
        const token = localStorage.getItem("authToken");
        config.headers.Authorization = token ? `Token ${token}` : "";
        return config;
    });
};

export default {
    get(email) {
        /* get profile correspond to an user email */
        useLocalToken();
        return Repository.get(`${resource}/profile/${email}`);
    },
    update(data) {
        /* Update profile */
        useLocalToken();
        return Repository.post(`${resource}/verify/`, data);
    },
    queryProfile({ role = null }) {
        useLocalToken();
        return Repository.get(`${resource}/list/?q=${role}`);
    },
};
