var rd = JSON.parse(document.getElementById('road').textContent);
L.geoJSON(rd).bindPopup(function (layer) { return layer.feature.properties.name; }).addTo(map);
map.fitBounds(feature.getBounds(), { padding: [100, 100] });