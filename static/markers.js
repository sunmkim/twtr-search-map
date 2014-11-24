// create google map
var map = new MapModel();
map.initMap();
var mapView = new MapView({model: map});
mapView.render();


// listen for events from /stream decorator
var source = new EventSource(
    "/stream"
);
source.onmessage = function(event){
	// convert event.data str to obj
	event_source_tweet = JSON.parse(event.data);
    var marker_info = {
    	username: event_source_tweet.screen_name,
    	text: event_source_tweet.text,
    	created_at: event_source_tweet.created_at,
    	location: event_source_tweet.coord
    };
    var markerView = new MarkerView({model: map, marker_info: marker_info});
    markerView.render();
};
