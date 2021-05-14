//adding osm tilelayer
var osm = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> WGST',
}).addTo(map);


var plc = JSON.parse(document.getElementById('places').textContent);
var BUKplc = L.geoJSON(plc).bindPopup(function (layer) { return layer.feature.properties.name; }).addTo(map);
//map.fitBounds(feature.getBounds(), { padding: [100, 100] });


var rd = JSON.parse(document.getElementById('road').textContent);
var BUKrd = L.geoJSON(rd).bindPopup(function (layer) { return layer.feature.properties.name; }).addTo(map);
//map.fitBounds(feature.getBounds(), { padding: [100, 100] });


var bound = JSON.parse(document.getElementById('boundary').textContent);
var BUKbound = L.geoJSON(bound).bindPopup(function (layer) { return layer.feature.properties.id; }).addTo(map);

var Topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
	maxZoom: 17,
	attribution: 'Map data: &copy; <a href="#">OpenStreetMap</a> contributors, <a href="#">WGST</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="#">CC-BY-SA</a>)'
});
var Esri = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
	attribution: '#'
});

// leaflet layer control
var baseMap = {
   'OSM' : osm,
   'Esri_WorldImagery' : Esri,
   'TOpenTopoMap' : Topo,
   //'bukrd' : BUKrd,
}

var overlayMaps = {
    'GeoJSON Markers' : marker,
    'Road' : BUKrd,
    'Places' : BUKplc,
    'Boundry' : BUKbound,

}
L.control.layers(baseMap, overlayMaps, {
    position: 'bottomright',
    collapsed: false
    }).addTo(map);
marker.addTo(map);
BUKrd.addTo(map);
