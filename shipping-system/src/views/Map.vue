<template>
    <div class="container">
        <button @click="routing2">Sth new</button>
        <input type="text" v-model="location" />
        <button @click="searchLocation">Find location</button>
        <br />
        {{ center }}
        <div class="map-container">
            <l-map class="map" :zoom="zoom" :center="center" ref="myMap">
                <l-tile-layer
                    :url="url"
                    :attribution="attribution"
                ></l-tile-layer>
                <l-circle
                    :lat-lng="center"
                    :radius="circle.radius"
                    :color="circle.color"
                />
            </l-map>
        </div>
        <button @click="routing">Search routes</button>
        <button @click="getLocation">Get current location</button>
    </div>
</template>

<script>
import axios from "axios";
import L from "leaflet";
import { IRouter, IGeocoder, LineOptions } from "leaflet-routing-machine";
import { LMap, LTileLayer, LIcon, LCircle } from "vue2-leaflet";
export default {
    name: "PageIndex",
    components: {
        LMap,
        LTileLayer,
        LCircle,
    },
    data() {
        return {
            // Map
            url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
            attribution:
                '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            zoom: 12,
            markerLatLng: [51.504, -0.159],
            // Locations
            location: "",
            myLat: 10.0184892,
            myLon: 105.739714,
            circle: {
                radius: 100,
                color: "red",
            },
            // Waypoint Routing
            routingControl: null,
            startIcon: L.icon({
                iconUrl: require("../assets/test/user-icon.jpg"),
                iconSize: [30, 30],
                iconAnchor: [30, 32],
                // popupAnchor: [-3, -76]
            }),
            destinationIcon: L.icon({
                iconUrl: require("../assets/test/user-icon.jpg"),
                iconSize: [30, 30],
                iconAnchor: [10, 32],
                // popupAnchor: [-3, -76]
            }),
        };
    },
    computed: {
        locationURL() {
            return encodeURIComponent(this.location);
        },
        center() {
            return [this.myLat, this.myLon];
        },
        mapOject() {
            return this.$refs.myMap.mapObject;
        },
    },
    methods: {
        async searchLocation() {
            const url =
                "https://nominatim.openstreetmap.org/search?format=json&limit=3&q=" +
                this.locationURL;
            try {
                const response = await axios.get(url);
                const firstResult = response.data[0];
                this.myLat = parseFloat(firstResult.lat);
                this.myLon = parseFloat(firstResult.lon);
            } catch (e) {
                console.log(e);
            }
        },
        routing() {
            // Routing between points
            if (this.routingControl) {
                console.log("There is routing");
                this.mapOject.removeControl(this.routingControl);
            }

            console.log(this.myLat, this.myLon);
            this.routingControl = L.Routing.control({
                waypoints: [
                    L.latLng(this.myLat, this.myLon),
                    L.latLng(10.01792665, 105.78839074112506),
                ],
                createMarker: (i, waypoint, n) => {
                    const markerIcon =
                        i == 0 ? this.startIcon : this.destinationIcon;
                    const marker = L.marker(waypoint.latLng, {
                        draggable: true,
                        bounceOnAdd: false,
                        bounceOnAddOptions: {
                            duration: 1000,
                            height: 800,
                            function() {
                                bindPopup(myPopup).openOn(map);
                            },
                        },
                        icon: markerIcon,
                    });
                    return marker;
                },
                // router: L.Routing.osrmv1({
                //     serviceUrl: "http://my-osrm/route/v1"
                // })
            }).addTo(this.mapOject);

            this.routingControl.on("routesfound", function (e) {
                console.log(e.routes);
            });
            // this.routingControl._container.style.display = "None";
        },
        async routing2() {
            const ninhkieu = [10.0243192, 105.7727087];
            const hungphu = [10.01792665, 105.78839074112506];

            try {
                const url = `https://api.openrouteservice.org/v2/directions/driving-car?api_key=5b3ce3597851110001cf6248f8c35fd1e82d4754933bf5d8fea33263&start=${ninhkieu[0]},${ninhkieu[1]}&end=${hungphu[0]},${hungphu[1]}`;

                const response = await axios.get(url, {
                    headers: {
                        "Content-Type":
                            "application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8",
                    },
                });

                console.log(JSON.stringify(response.data));
            } catch (e) {
                console.log(e.response);
            }
        },
        getLocation() {
            var options = {
                enableHighAccuracy: true,
                maximumAge: 3600000,
            };
            const result = navigator.geolocation.getCurrentPosition(
                (position) => {
                    this.myLat = position.coords.latitude;
                    this.myLon = position.coords.longitude;

                    console.log(this.myLat, this.myLon);
                },
                (error) => {
                    if (error) {
                        this.error = error;
                        console.log(error);
                    }
                },
                options
            );
        },
    },
};
</script>

<style lang="scss" scoped>
.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
.map-container {
    width: 800px !important;
    height: 300px;
    overflow: hidden;
    border: 1px solid black;
    .map {
        width: 100%;
        height: 100%;
    }
    .leaflet-control-container .leaflet-routing-container-hide {
        display: none;
    }
}
</style>
