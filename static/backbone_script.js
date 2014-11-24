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

	marker_info: {
		username: '',
		text: '',
		created_at: '',
		location: []
	},

	render: function(){	
		var myLatLng = new google.maps.LatLng(this.marker_info.get('location')[0], this.marker_info.get('location')[1]);
		var marker = new google.maps.Marker({
			map: this.model.map
		});	
        console.log('MARKER VIEW: ', marker);
		if (typeof this.model.get('text') !== 'undefined'){
			marker.setMap(this.model);
			// this.$el.append("<li>"+this.model.get('text')+"</li>");
		}
		return this;
	}
});
