function initialize() {
    var mapOptions = {
        center: {
            lat: 40.713,
            lng: -74.000
        },
        zoom: 11
    };
    var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
}
google.maps.event.addDomListener(window, 'load', initialize);
