// define model for google map
var MapModel = Backbone.Model.extend({
	initMap: function() {
		var mapOptions = {
	        center: {
	            lat: 30.713,
	            lng: -74.000
	        },
	        zoom: 4,
    	};
    	this.set('mapOptions', mapOptions);
	}
});


// define view for google map
var MapView = Backbone.View.extend({
	// initialize map attr to google map instance
  initialize: function() {
		this.model.set('map',
			new google.maps.Map(document.getElementById('map-canvas'), this.model.get('mapOptions'))
		);
	},
	render: function() {
		return this;
	}
});


// define view for map markers
var MarkerView = Backbone.View.extend({
	marker_info: {},
	initialize: function(options) {
		this.marker_info = options.marker_info;
	},
	render: function(){
		var self = this;
		var myLatLng = new google.maps.LatLng(this.marker_info.location[0], this.marker_info.location[1]);
		var marker = new google.maps.Marker({
			map: this.model.map,
			position: myLatLng
		});
    var contentString = '<h4>'+this.marker_info.username +'</h4>'
                          + '<p>'+ this.marker_info.text +'</p>'
                          + '<p><i>Tweeted on '+ this.marker_info.created_at.substring(0,19)
                          + this.marker_info.created_at.substring(25) + '</i></p>';
		// define info-window
		var infowindow = new google.maps.InfoWindow({
		    content: contentString
		});
		// set marker with info-window on map
		if (typeof this.marker_info.text !== 'undefined'){
			marker.setMap(this.model.attributes.map);
			// open info-window when marker is clicked
			google.maps.event.addListener(marker, 'click', function() {
				infowindow.open(self.model.attributes.map, marker);
			});
		}
		return this;
	}
});