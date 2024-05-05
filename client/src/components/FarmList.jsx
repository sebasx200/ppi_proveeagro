import { useEffect, useState } from "react"
import { getAllFarms } from "../api/farm.api"
import { FarmCard } from "./FarmCard"

export function FarmList(){

    const [farms, setFarms] = useState([]);

    useEffect(() => {

        async function loadFarms(){
            const response = await getAllFarms()
            setFarms(response.data)
        }
        loadFarms()
    }, [])
    
    return <div>
        {farms.map((farm) => (
            <FarmCard key = {farm.id} farm={farm}/>
        ))}
    </div>;
}