// or, add to an existing map:
map.addControl(new L.Control.Fullscreen({
    // To change fullscreen control text:
    title: {
    'false': 'View Fullscreen',
    'true': 'Exit Fullscreen'
    }

}));

/*map.on('fullscreenchange', function () {
    if (map.isFullscreen()) {
        console.log('entered fullscreen');
    } else {
        console.log('exited fullscreen');
    }
});
*/