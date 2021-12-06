<template>
    <div class="map">
        <l-map
            style="height: 500px; width: 800px"
            :zoom="mapConfig.zoom"
            :center="center"
            @ready="ready"
        >
            <l-tile-layer
                :url="mapConfig.url"
                :attribution="mapConfig.attribution"
            ></l-tile-layer>
            <l-marker ref="marker" :lat-lng="center" :icon="icon">
                <l-popup class="popup"><h3>Kaz Delivery Comapny</h3></l-popup>
            </l-marker>
        </l-map>
    </div>
</template>
<script>
import { mapState } from "vuex";
import L from "leaflet";
import { LMap, LTileLayer, LPopup, LCircle, LMarker, LIcon } from "vue2-leaflet";

export default {
    name: "Company",
    components: {
        LMap,
        LTileLayer,
        LCircle,
        LMarker,
        LPopup,
        LIcon,
    },
    computed: {
        ...mapState(["currentLocation"]),
        center() {
            return [this.currentLocation.latitude, this.currentLocation.longitude];
        },
    },
    data() {
        return {
            mapConfig: {
                url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                attribution:
                    '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
                zoom: 15,
            },
            icon: L.icon({
                iconUrl: require("../assets/markers/blue-marker.svg"),
                iconSize: [40, 42],
                iconAnchor: [16, 0],
            }),
        };
    },
    methods: {
        ready() {
            const map = this.$refs.marker.mapObject;
            map.openPopup();
        },
    },
};
</script>
<style lang="scss" scoped>
.map {
    border-radius: 15px;
    border: 2px solid var(--primary-color);
    margin: 2rem;
    min-height: 500px;
    overflow: hidden;
    position: relative;
}

.popup {
    width: max-content;
}
</style>
