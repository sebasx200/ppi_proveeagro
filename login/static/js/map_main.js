// Initialize map
const map = L.map('map')
var location_medellin = [6.25184, -75.56359];
map.setView(location_medellin, 13);

var OpenStreetMap_Mapnik = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});

OpenStreetMap_Mapnik.addTo(map);

// Add fullscreen control
map.addControl(new L.Control.Fullscreen());

// Add geocoder control
L.Control.geocoder().addTo(map);

var lc = L.control
  .locate({
    position: "topleft",
    strings: {
      title: "Mostrar dónde estoy"
    }
  })

  .addTo(map);
  
fetch('/get_suppliers/')
  .then(response => response.json())
  .then(suppliers => {
      for (var i = 0; i < suppliers.length; i++) {
        if (suppliers[i].latitude != null && suppliers[i].longitude != null){
          var marker = L.marker([suppliers[i].latitude, suppliers[i].longitude]).addTo(map);
          marker.bindPopup(suppliers[i].name + "<br>" + suppliers[i].address + "");
        }
        else{
          console.log("Supplier without location: " + suppliers[i].name);
        }
      }
  });
