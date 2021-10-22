<template>
    <div class="container">
        <div class="headers">
            <p class="title">Order's tracking</p>
            <div class="orders-information">
                <p>Consignee location: ...</p>
                <p>Consignor location: ...</p>
                <p>Current location: ...</p>
            </div>
        </div>

        <div class="map">
            <l-map
                style="height: 600px; width: 100%"
                :zoom="mapConfig.zoom"
                :center="center"
                ref="myMap"
            >
                <l-tile-layer
                    :url="mapConfig.url"
                    :attribution="mapConfig.attribution"
                ></l-tile-layer>
                <l-circle :lat-lng="center" :radius="10" color="red" />
            </l-map>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import { mapState } from "vuex";
import L from "leaflet";
import { LMap, LTileLayer, LIcon, LCircle } from "vue2-leaflet";

export default {
    name: "Map",
    components: {
        LMap,
        LTileLayer,
        LCircle,
    },
    data() {
        return {
            mapConfig: {
                url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                attribution:
                    '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
                zoom: 12,
            },
        };
    },
    computed: {
        ...mapState(["currentLocation"]),
        center() {
            return [
                this.currentLocation.latitude,
                this.currentLocation.longitude,
            ];
        },
    },
};
</script>

<style lang="scss" scoped>
.container {
    display: flex;
    align-items: center;
    justify-content: center;

    .headers {
        width: 100%;
        .title {
            font-size: 1.2rem;
            font-weight: bold;
        }
    }

    .map {
        border-radius: 15px;
        border: 2px solid var(--primary-color);
        margin: 2rem;
        width: 80%;
        min-height: 400px;
        overflow: hidden;
    }
}
</style>
