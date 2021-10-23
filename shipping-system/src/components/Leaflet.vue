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
                style="height: 500px; width: 100%"
                :zoom="mapConfig.zoom"
                :center="center"
                ref="map"
            >
                <l-tile-layer
                    :url="mapConfig.url"
                    :attribution="mapConfig.attribution"
                ></l-tile-layer>
                <!-- <l-circle :lat-lng="center" :radius="10" color="red" /> -->
                <!-- <l-marker :lat-lng="center" :icon="icons.companyIcons">
                    <l-popup><h1>Kaz Shipping Comapny</h1></l-popup>
                </l-marker> -->
            </l-map>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import { mapState } from "vuex";
import L from "leaflet";
import { LMap, LTileLayer, LPopup, LCircle, LMarker } from "vue2-leaflet";

export default {
    name: "Map",
    components: {
        LMap,
        LTileLayer,
        LCircle,
        LMarker,
        LPopup,
    },
    props: {
        order: Object,
    },
    data() {
        return {
            mapConfig: {
                url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                attribution:
                    '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
                zoom: 12,
            },
            icons: {
                companyIcons: L.icon({
                    iconUrl: require("../assets/markers/red-marker.svg"),
                    iconSize: [40, 40],
                    iconAnchor: [20, 0],
                }),
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
        mapOject() {
            return this.$refs.map.mapObject;
        },
    },
    methods: {
        async routing() {
            console.log(this.order.consignee.wardId);

            const coors = await this.$func.searchLocation(
                this.order.consignee.wardId
            );

            console.log(coors);
            // let marker = L.marker(coors, {
            //     icon: this.icons.companyIcons,
            // });

            const routingControl = L.Routing.control({
                waypoints: [L.latLng(this.center), L.latLng(coors)],
                addWaypoints: false,
                createMarker: (i, waypoint, n) => {
                    const marker = L.marker(waypoint.latLng, {
                        draggable: false,
                        bounceOnAdd: false,
                        bounceOnAddOptions: {
                            duration: 1000,
                            height: 800,
                        },
                        icon: this.icons.companyIcons,
                    });
                    return marker;
                },
            }).addTo(this.mapOject);
        },
    },
    async created() {
        this.routing();
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
        min-height: 500px;
        overflow: hidden;
    }
}
</style>
