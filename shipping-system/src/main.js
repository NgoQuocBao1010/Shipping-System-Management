import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import Vuelidate from "vuelidate";
import VueToast from "vue-toast-notification";

import ProvincesAPI from "./api/locationAPI";

Vue.config.productionTip = false;
Vue.use(Vuelidate);
Vue.use(VueToast);

// Global functions
Vue.prototype.$province = ProvincesAPI;
Vue.prototype.$func = {
    formatMoneyToVND(value) {
        if (!value) return "Invalid";
        return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    },
    handleError(error) {
        console.log(error);
        let message = "";

        if (error.response.status === 404) {
            message = "Not found";
        } else if (error.response.status === 401) {
            router.push({ name: "Unauthorized" });
        } else if (error.response.status === 500) {
            router.push({ name: "InternalError" });
        }

        return message;
    },
};

new Vue({
    router,
    store,
    render: (h) => h(App),
}).$mount("#app");
