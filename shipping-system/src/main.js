import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import Vuelidate from "vuelidate";
import VueToast from "vue-toast-notification";
import axios from "axios";

import ProvincesAPI from "./api/routing/province-api";

Vue.config.productionTip = false;
Vue.use(Vuelidate);
Vue.use(VueToast);

// Global functions
Vue.prototype.$province = ProvincesAPI;
Vue.prototype.$func = {
    formatMoneyToVND(value) {
        if (value !== 0 && !value) return "Invalid";
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
    cleanAddress(address) {
        return address
            .replace("Thành phố", "")
            .replace("Quận", "")
            .replace("Phường", "")
            .replace("Xã", "")
            .trim();
    },
    async getFullAddress(wardId, search = false) {
        /* Construct and return the full address from wardId parameters */
        const ward = await ProvincesAPI.getWard(wardId);

        if (!ward.district_code) return "";

        const d = store.getters.district(ward.district_code);

        let fullAddress = `${ward.name}, ${d.name}`;

        fullAddress = !search
            ? fullAddress
            : encodeURIComponent(this.cleanAddress(fullAddress));

        return fullAddress;
    },
    async searchLocation(wardId) {
        /* Return latitude and longitude of an given district ID */
        const uriAddress = await this.getFullAddress(wardId, true);

        try {
            const url =
                "https://nominatim.openstreetmap.org/search?format=json&limit=3&q=" +
                uriAddress;
            const response = await axios.get(url);

            if (response.data.length > 0) {
                const result = response.data[0];

                return {
                    lat: parseFloat(result.lat),
                    lon: parseFloat(result.lon),
                };
            }
            console.log("Error finding location");
            return;
        } catch (e) {
            console.log("Error finding location", e);
        }
    },
};

new Vue({
    router,
    store,
    render: (h) => h(App),
}).$mount("#app");
