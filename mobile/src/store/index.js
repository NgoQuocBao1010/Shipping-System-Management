import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Store instance.
 */

export default function (/* { ssrContext } */) {
    const Store = new Vuex.Store({
        state: {
            authenticated: false,
            token: false,
            user: null,
        },
        mutations: {
            authenticate(state, token) {
                // Authenticate: Store auth token
                state.authenticated = true;
                state.token = token;
                console.log("Global store: Authenticated");
            },
            updateProfile(state, profile) {
                /* Update profile state, store user information */
                state.user = profile;
            },
            logout(state) {
                state.authenticated = false;
                state.token = null;
                state.user = null;
                this.$router.replace({ name: "login" });
            },
        },
        actions: {
            async login(context, token) {
                // API call to get user token and information
                try {
                    const response = await axios.get(
                        "https://10.0.2.2:8000/account/verify",
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
                    console.log("Error login in: ", e);
                    return false;
                }
            },
        },
        strict: process.env.DEBUGGING,
    });

    return Store;
}
