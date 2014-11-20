// define model for map markers
var MarkerModel = Backbone.Model.extend({
	defaults: {
		username: '',
		text: '',
		created_at: '',
		location: []
	}
});

// define view for map markers
var MarkerView = Backbone.View.extend({
	tagName: 'li',
	
	el: $('.log'),

	initialize: function(){
		console.log('View Initialized!');
		this.render();
	},

	render: function(){
		if (typeof this.model.get('text') !== 'undefined'){
			this.$el.append("<li>"+this.model.get('text')+"</li>");
		}
		return this;
	}

});



// listen for events from /stream decorator
var source = new EventSource(
    "/stream"
);
source.onmessage = function(event){
	// convert event.data str to obj
	event_source_tweet = JSON.parse(event.data);

    var marker = new MarkerModel();
    marker.set({
    	username: event_source_tweet.screen_name,
    	text: event_source_tweet.text,
    	created_at: event_source_tweet.created_at,
    	location: event_source_tweet.coord
    });
    console.log(marker.get('text'));
    var markerview = new MarkerView({model: marker});

};










