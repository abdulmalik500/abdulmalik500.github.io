//adding osm tilelayer
var osm = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> WGST',
}).addTo(map);

var Topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
	maxZoom: 17,
	attribution: 'Map data: &copy; <a href="#">OpenStreetMap</a> contributors, <a href="#">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
});
var Esri = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
	attribution: '#'
});

// leaflet layer control
var baseMap = {
   'OSM' : osm,
   'Esri_WorldImagery' : Esri,
   'TOpenTopoMap' : Topo
}

var overlayMaps = {
    'GeoJSON Markers' : marker,

}
L.control.layers(baseMap, overlayMaps, {
    position: 'bottomright',
    collapsed: false
    }).addTo(map);
marker.addTo(map);