import {Link} from 'react-router-dom';

export function Navigation() {
    return (
        <div>
            <Link to="/farms">
            <h1>Fincas</h1>
            </Link>
            <Link to="/farms/add">Añadir nueva finca</Link>
        </div>
    )
}
