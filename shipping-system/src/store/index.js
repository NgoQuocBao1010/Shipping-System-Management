import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
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
        authenticate(state, token) {
            // Authenticate: Store auth token
            state.authenticated = true;
            state.token = token;
            localStorage.setItem("authToken", token);
            console.log("Global store: Authenticated");
        },
        updateProfile(state, profile) {
            /* Update profile state, store user information */
            state.user = profile;
        },
        logout(state) {
            // Logging out: Set all auth information to null
            state.user = null;
            state.token = null;
            state.authenticated = false;
            localStorage.setItem("authToken", "");
        },
        saveProvinceInfo(state, data) {
            // Save all the provice data from api call
            state.provinces = data;
        },
    },
    actions: {
        async login(context, token) {
            // API call to get user token and information
            try {
                const response = await axios.get(
                    "http://127.0.0.1:8000/account/verify",
                    {
                        headers: {
                            Authorization: `Token ${token}`,
                        },
                    }
                );

                if (response.status === 200) {
                    context.commit("authenticate", token);
                    context.commit("updateProfile", response.data);
                }
                return true;
            } catch (e) {
                console.log("Error login in: ", e.response);
                context.commit("logout");
                return false;
            }
        },
    },
    getters: {
        isAuthenticated: (state) => {
            return state.authenticated;
        },
        district: (state) => (id) => {
            /* Return district object by given id */
            return state.provinces
                ? state.provinces.find((dis) => dis.id === id)
                : {};
        },
        isAdmin: (state) => {
            /* Return if user is admin */
            return state.user ? state.user.isAdmin : false;
        },
        isStaff: (state) => {
            /* Return if user is a staff member */
            return state.user ? state.user.isStaff : false;
        },
        email: (state) => {
            /* Return current user's email */
            return state.user ? state.user.email : "email";
        },
    },
    modules: {},
});
