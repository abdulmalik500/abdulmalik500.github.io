//Map class initialize
var map = L.map('map', {
    //measureControl: true,
    //fullscreenControl: true,
}).setView([11.970148, 8.433266], 15);
//setting the zoom control position
map.zoomControl.setPosition('topleft');

map.on('fullscreenchange', function () {
    if (map.isFullscreen()) {
        console.log('entered fullscreen');
    } else {
        console.log('exited fullscreen');
    }
});

/***adding osm tilelayer
var osm = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> WGST',
}).addTo(map);

var Topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
	maxZoom: 17,
	attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
});
var Esri = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
	attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'
});
***/

L.Routing.control({
    waypoints: [
        L.latLng(11.964853, 8.417201),
        L.latLng(11.970143, 8.433938)
    ],
    //router: L.Routing.graphHopper('8b49699c-f011-4a5b-9d4f-e165edead5df'),
    router: L.Routing.mapbox('pk.eyJ1IjoibG9rYWNoaW1hcCIsImEiOiJjazZrdGxoM2MwN2hsM2tsa3Z5d3p5bmV2In0.Gcr52REffgWCkccKC0UwFg'),
    routeWhileDragging: true
}).addTo(map);

//adding marker to the map
var marker = L.marker([11.969099, 8.425501]).addTo(map);
marker.bindPopup("<b>Bayero University Kano</b>").openPopup();

//adding marker to the map
var marker = L.marker([11.970148, 8.433266]).addTo(map);
marker.bindPopup("<b>Mosque</b>").openPopup();

//adding temporary popup to map
var popup = L.popup()
.setLatLng([11.969099, 8.425501])
.setContent("Bayero University Kano New Campus")
.openOn(map);


// add a scale to map

L.control.scale({ position: 'bottomleft' }).addTo(map);

//leaflet search
L.Control.geocoder({ position: 'topleft' }).addTo(map);

// zoom to layer
$('.zoom-to-layer').click(function() {
    map.setView([11.970148, 8.433266])
});

//adding a zoom control also:
//L.control.zoom(zoomInTitle).addTo(map);

// map coordinate display
/*map.on('mousemove', function(e) {
    console.log(e)
    $('.coordinate').html('Lat: ${e.latlng.lat} Lng: ${e.latlng.lng}')
});
*/



var mapId = document.getElementById('map');
    function fullScreenView() {
        mapId.requestfullscreen();
    }


/**
//map print
$('.print-map').click(function() {
    windows.print()
})
L.control.browserPrint().addTo(map);
**/

//leaflet measure
//L.control.measure().addTo(map);


