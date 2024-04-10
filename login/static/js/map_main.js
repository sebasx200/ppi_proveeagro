// Initialize map
const map = L.map('map')
var location_medellin = [6.25184, -75.56359];
map.setView(location_medellin, 13);

var OpenStreetMap_Mapnik = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});

OpenStreetMap_Mapnik.addTo(map);

let marker;

function onMapClick(e) {
    if (marker) {
        map.removeLayer(marker);
    }
    marker = L.marker(e.latlng).addTo(map);
}

// Add click event to map
map.on('click', onMapClick);
// Add fullscreen control
map.addControl(new L.Control.Fullscreen());
// Add locate control
var lc = L.control
  .locate({
    position: "topleft",
    strings: {
      title: "Mostrar dónde estoy"
    }
  })
  .addTo(map);
// Add geocoder control
L.Control.geocoder().addTo(map);