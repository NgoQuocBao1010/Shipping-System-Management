import axios from "axios";

// Base domain and base url
const BASE_DOMAIN = "http://127.0.0.1:8000/";
const baseURL = BASE_DOMAIN;

export default axios.create({ baseURL });
