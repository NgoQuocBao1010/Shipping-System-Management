import axios from "axios";

const getAllDistricts = async () => {
    try {
        // Open API url to get all provinces and their districts
        const url = `https://provinces.open-api.vn/api/?depth=2`;
        const response = await axios.get(url);

        const provicesData = [];

        // Restructure response api data
        response.data.forEach((provinceData) => {
            provinceData.districts.forEach((districtData) => {
                const district = {
                    name: `${districtData.name}, ${provinceData.name}`,
                    id: districtData.code,
                    province_code: provinceData.code,
                };
                provicesData.push(district);
            });
        });
        return promiseData;
    } catch (e) {
        console.log("API: Error get province info");
    }
};

export default { getAllDistricts };
