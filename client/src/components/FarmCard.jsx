export function FarmCard({farm}){
    return (
        <div>
        <h1>{farm.name}</h1>
        <p>{farm.location}</p>
        <hr/>
    </div>
    );
}