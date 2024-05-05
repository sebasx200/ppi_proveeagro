import axios from 'axios';

const farmApi = axios.create({
    baseURL: 'http://localhost:8000/farm/farms/'
})
export const getAllFarms = () =>{
    return farmApi.get("/");
}

export const createFarm = (farm) =>{
    return farmApi.post("/", farm);
}
