import axios from "axios";

const getAllDistricts = async () => {
    /* 
        Provinces Open API
        Get all districts of VietNam
    */
    try {
        const url = `https://provinces.open-api.vn/api/?depth=2`;
        const response = await axios.get(url);

        let provicesData = [];
        let canthoDistrict = [];

        // Restructure response api data
        response.data.forEach((provinceData) => {
            provinceData.districts.forEach((districtData) => {
                const district = {
                    name: `${districtData.name}, ${provinceData.name}`,
                    id: districtData.code,
                    provinceCode: provinceData.code,
                    cityName: provinceData.name,
                };

                if (provinceData.code !== 92) provicesData.push(district);
                else canthoDistrict.push(district);
            });
        });

        provicesData = [...canthoDistrict, ...provicesData];
        return provicesData;
    } catch (e) {
        console.log("API: Error get province info", e);
        return {};
    }
};

const getWardList = async (districtId) => {
    /*  Get list of wards from given district id */
    try {
        const url = `https://provinces.open-api.vn/api/d/${districtId}/?depth=2`;
        const response = await axios.get(url);

        let wards = [];
        response.data.wards.forEach((ward) => {
            const wardObj = {
                name: ward.name,
                id: ward.code,
            };
            wards.push(wardObj);
        });
        return wards;
    } catch (err) {
        console.log(`Error getting subdistrict`, err);
        return [];
    }
};

const getWard = async (wardCode) => {
    /* Get a ward's info that correspond with given wardCode */
    try {
        const response = await axios.get(
            `https://provinces.open-api.vn/api/w/${wardCode}`
        );

        return response.data;
    } catch (e) {
        if (e.response.status === 404) {
            console.log("Invalid ward's code");
        } else console.log("Error getting wards", e.response);
        return {};
    }
};

export default { getAllDistricts, getWard, getWardList };
