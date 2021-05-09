//Geojson load
var marker = L.markerClusterGroup();
var buk = L.geoJSON(data, {
    onEachFeature: function(feature, layer) {
        layer.bindPopup(feature.properties.name)
    }
});
buk.addTo(marker);
// marker.addTo(map);
