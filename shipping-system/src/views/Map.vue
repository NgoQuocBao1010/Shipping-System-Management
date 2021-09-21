<template>
    <div class="container">
        <h1>Test Map</h1>
        <input type="text" name="location" v-model="location" />
        {{ locationURL }}
        <button @click="searchLocation">Click</button>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "TestMap",
    data() {
        return {
            location: "",
        };
    },
    computed: {
        locationURL() {
            return encodeURIComponent(this.location);
        },
    },
    methods: {
        async searchLocation() {
            console.log(this.locationURL);
            const url =
                "https://nominatim.openstreetmap.org/search?format=json&limit=3&q=" +
                this.locationURL;

            try {
                const response = await axios.get(url);

                console.log(response.data);
            } catch (e) {
                console.log(e);
            }
        },
    },
};
</script>

<style lang="scss" scope></style>
