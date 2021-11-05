<template>
    <div class="container">
        <!-- Headers -->
        <div class="headers">
            <p class="title">Order's tracking</p>
            <div class="information">
                <p>
                    Company location
                    <img src="../assets/markers/blue-marker.svg" alt="" />
                </p>
                <p>
                    Consignee location
                    <img src="../assets/markers/red-marker.svg" alt="" />
                </p>
                <!-- <p>Current location: ...</p> -->
            </div>
        </div>

        <!-- Leaflet map -->
        <div class="map">
            <transition name="fade">
                <div class="animation" v-if="!routes">
                    <LoadingAnimation size="large" />
                    <p>Tracking your order ...</p>
                </div>
            </transition>

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
            </l-map>
        </div>
        <button @click="setZoomLevel">Reset Map</button>
    </div>
</template>

<script>
import { mapState } from "vuex";
import L from "leaflet";
import { LMap, LTileLayer, LPopup, LCircle, LMarker } from "vue2-leaflet";

import LocationAPI from "../api/routing/location";

import LoadingAnimation from "./CircleAnimation.vue";

export default {
    name: "Map",
    components: {
        LMap,
        LTileLayer,
        LCircle,
        LMarker,
        LPopup,
        LoadingAnimation,
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
                blueIcons: L.icon({
                    iconUrl: require("../assets/markers/blue-marker.svg"),
                    iconSize: [40, 40],
                    iconAnchor: [20, 20],
                }),
                redIcons: L.icon({
                    iconUrl: require("../assets/markers/red-marker.svg"),
                    iconSize: [40, 40],
                    iconAnchor: [20, 0],
                }),
            },

            consigneeAddress: null,

            routes: null,
            initialZoom: null,
            initialCenter: null,
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
        mapObject() {
            return this.$refs.map.mapObject;
        },
    },
    methods: {
        async routing() {
            /* Routing for order tracking */
            const { latitude, longitude } = await LocationAPI.search(
                this.consigneeAddress
            ); // Get consignee location

            // Routing process configuration
            const routingControl = L.Routing.control({
                waypoints: [
                    L.latLng(this.center),
                    L.latLng({ lat: latitude, lon: longitude }),
                ],
                fitSelectedRoutes: true,
                addWaypoints: false,
                lineOptions: {
                    styles: [{ color: "#362222", opacity: 1, weight: 5 }],
                },
                createMarker: (i, waypoint, n) => {
                    const markerIcon =
                        i === 0 ? this.icons.blueIcons : this.icons.redIcons;

                    const popUpContent =
                        i === 0
                            ? "Kaz Shipping System"
                            : "Estimated Consignee Location";

                    const marker = L.marker(waypoint.latLng, {
                        draggable: false,
                        bounceOnAdd: false,
                        bounceOnAddOptions: {
                            duration: 1000,
                            height: 800,
                        },
                        icon: markerIcon,
                    }).bindPopup(`<h3>${popUpContent}</h3>`);
                    return marker;
                },
            }).addTo(this.mapObject);

            routingControl.hide(); // Hide routing instruction

            routingControl.on("routesfound", (e) => {
                /* Handle event when routes found */
                this.routes = e.routes;

                this.mapObject.on("zoom", (e) => {
                    // console.log(this.mapObject._zoom);
                    // console.log(this.mapObject.getCenter());
                });
            });
        },
        setZoomLevel() {
            this.mapObject.setZoom(12);
        },
    },
    async created() {
        this.consigneeAddress = await this.$func.getFullAddress(
            this.order.consignee.wardId
        );

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
            font-size: 1.4rem;
            font-weight: bold;
        }

        .information {
            margin-top: 2rem;
            display: flex;
            align-items: center;
            justify-content: space-evenly;

            p {
                font-size: 1rem;
                font-weight: 600;

                img {
                    height: 40px;
                }
            }
        }
    }

    .map {
        border-radius: 15px;
        border: 2px solid var(--primary-color);
        margin: 2rem;
        width: 80%;
        min-height: 500px;
        overflow: hidden;
        position: relative;

        .animation {
            position: absolute;
            inset: 0;
            background: rgba(255, 255, 255, 0.8);
            z-index: 1200;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;

            p {
                font-size: 1.5rem;
                font-weight: 500;
            }
        }
    }
}
</style>
