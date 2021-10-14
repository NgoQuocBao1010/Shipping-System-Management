import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import Vuelidate from "vuelidate";

import ProvincesAPI from "./api/locationAPI";

Vue.config.productionTip = false;
Vue.use(Vuelidate);

// Global functions
Vue.prototype.$province = ProvincesAPI;
Vue.prototype.$func = {
    formatMoneyToVND(value) {
        if (!value) return "Invalid";
        return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    },
};

new Vue({
    router,
    store,
    render: (h) => h(App),
}).$mount("#app");
