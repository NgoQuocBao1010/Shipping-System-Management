import axios from "axios";

const OPENSERVICE_API_KEY =
    "5b3ce3597851110001cf6248f8c35fd1e82d4754933bf5d8fea33263";

const cleanAddress = (address) => {
    /* Remove all prefix of address */
    return address
        .replace("Thành phố", "")
        .replace("Quận", "")
        .replace("Phường", "")
        .replace("Huyện", "")
        .replace("Xã", "")
        .trim();
};

const reduceAddress = (address) => {
    /* Reduce some parts of an address to enhace change of finding location */
    let splitAddress = cleanAddress(address).split(",");
    splitAddress.shift();

    return splitAddress.join(",");
};

const searchLocation = async (address) => {
    /* Make openstreet API call to get geolocation of an address */
    try {
        const url =
            "https://nominatim.openstreetmap.org/search?format=json&limit=3&q=" +
            encodeURIComponent(cleanAddress(address));
        const { data } = await axios.get(url);

        if (data.length > 0) {
            const { lat, lon } = data[0];
            console.log(lat, lon);

            return {
                latitude: parseFloat(lat),
                longitude: parseFloat(lon),
            };
        }

        console.log("No location found on given address: ", address);
        return null;
    } catch (e) {
        console.log("Error while finding locaition", e);
        return null;
    }
};

export default {
    async search(address) {
        /* Return an object of longitude and latitude of an given address */
        console.log(address);
        const location = await searchLocation(address);

        if (!location) {
            const newAddress = reduceAddress(address);
            return await searchLocation(newAddress);
        }

        return location;
    },
    async estimateDistance(from, to) {
        const fromCoors = [from.longitude, from.latitude];

        const toCoors = [to.longitude, to.latitude];

        try {
            const headers = {
                Accept: "application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8",
                Authorization: OPENSERVICE_API_KEY,
                "Content-Type": "application/json; charset=utf-8",
            };
            const { data } = await axios.post(
                "https://api.openrouteservice.org/v2/directions/driving-car/geojson",
                { coordinates: [fromCoors, toCoors] },
                { headers }
            );

            const routing = data.features[0].properties.summary;

            return routing;
        } catch (e) {
            console.log("Error while routing ", e);
        }
    },
};
