<template>
    <div>
        <h1>Update location</h1>
        <h3>{{ location }}</h3>
        <button @click="getLocation">Get location</button>
        <button @click="updateLocation">Update location</button>
        <button @click="updateDummyLocation">Update dummy location</button>
    </div>
</template>

<script>
import { RepositoryFactory } from "../api/backend/Factory";
const OrderAPI = RepositoryFactory.get("order");

export default {
    name: "DriverTest",
    data: () => ({
        location: "Hello",
        orderId: "nmskZA",
    }),
    methods: {
        getLocation() {
            navigator.geolocation.getCurrentPosition((position) => {
                const { coords } = position;
                const { latitude, longitude } = coords;
                this.location = JSON.stringify({
                    lat: latitude,
                    lon: longitude,
                });
            });
        },
        async updateLocation() {
            try {
                const { status } = await OrderAPI.updateLocation({
                    orderId: this.orderId,
                    data: { location: this.location },
                });

                this.$toast.success("Update success");
            } catch (e) {
                console.log(e);
            }
        },
        updateDummyLocation() {
            this.location = JSON.stringify({
                lat: 10.823099,
                lon: 106.629662,
            });
            this.updateLocation();
        },
    },
};
</script>

<style lang="scss" scoped></style>
