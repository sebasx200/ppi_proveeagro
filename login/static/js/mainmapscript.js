const map = L.map('map')
var location_medellin = [6.25184, -75.56359];
map.setView(location_medellin, 13);

var OpenStreetMap_Mapnik = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});

OpenStreetMap_Mapnik.addTo(map);

let marker;

var lat = document.getElementById('id_latitude');
var lng = document.getElementById('id_longitude');

map.on('click', function(e) {
    if (marker) {
        map.removeLayer(marker);
    }
    marker = L.marker(e.latlng).addTo(map);
    lat.value = e.latlng.lat;
    lng.value = e.latlng.lng;
});

map.addControl(new L.Control.Fullscreen());