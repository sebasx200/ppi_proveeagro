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

var nearbySuppliers = [];

const onLocationFound = (e) => {
  fetch('/get_suppliers/')
      .then(response => response.json())
      .then(suppliers => {
          for (var i = 0; i < suppliers.length; i++) {
              if (suppliers[i].latitude != null && suppliers[i].longitude != null) {
                  var supplierLocation = {latitude: suppliers[i].latitude, longitude: suppliers[i].longitude};
                  var distance = getDistance(e, supplierLocation);  // calculate the distance to the supplier

                  // if the supplier is within 5 km of the user's location, add a marker to the map
                  if (distance <= 2) {
                      var marker = L.marker([suppliers[i].latitude, suppliers[i].longitude]).addTo(map);
                      marker.bindPopup("<b>" + suppliers[i].name + "</b><br>" + suppliers[i].address + "<br>");

                      // add the supplier to the list of nearby suppliers
                      nearbySuppliers.push(suppliers[i]);
                  }
              }
              else{
                  console.log("Supplier without location: " + suppliers[i].name);
              }
          }
          var ol = document.getElementById("nearby_suppliers");
          for (var i = 0; i < nearbySuppliers.length; i++) {
            var li = document.createElement("li");
            li.appendChild(document.createTextNode(nearbySuppliers[i].name));
            ol.appendChild(li);
          }
      });
}


// function to calculate the distance between two points using the Haversine formula
function getDistance(location1, location2) {
  var R = 6371;  // radius of the Earth in km
  var dLat = deg2rad(location2.latitude - location1.latitude);
  var dLon = deg2rad(location2.longitude - location1.longitude);
  var a = Math.sin(dLat/2) * Math.sin(dLat/2) +
          Math.cos(deg2rad(location1.latitude)) * Math.cos(deg2rad(location2.latitude)) *
          Math.sin(dLon/2) * Math.sin(dLon/2);
  var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
  var distance = R * c;  // distance in km
  return distance;
}

// function to convert degrees to radians
function deg2rad(deg) {
  return deg * (Math.PI/180);
}
map.on('locationfound', onLocationFound);
