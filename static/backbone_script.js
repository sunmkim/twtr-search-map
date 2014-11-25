// define model for google map
var MapModel = Backbone.Model.extend({
	initMap: function() {
		var mapOptions = {
	        center: {
	            lat: 40.713,
	            lng: -74.000
	        },
	        zoom: 11,
    	};
    	this.set('mapOptions', mapOptions);
	}
});


// define view for google map
var MapView = Backbone.View.extend({
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

	el: $('.log'),

	marker_info: {},

	initialize: function(options) {
		this.marker_info = options.marker_info;
	},


	render: function(){	
		var myLatLng = new google.maps.LatLng(this.marker_info.location[0], this.marker_info.location[1]);
		var marker = new google.maps.Marker({
			map: this.model.map,
			position: myLatLng
		});	
		if (typeof this.marker_info.text !== 'undefined'){
			marker.setMap(this.model.attributes.map);
			console.log(myLatLng);
			console.log(this.model.attributes.map);
			console.log('reached marker set func');
		}
		return this;
	}
});
