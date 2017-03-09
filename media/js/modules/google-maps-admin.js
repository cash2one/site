function googleMapAdmin() {
    var geocoder = new google.maps.Geocoder();
    var map;
    var marker;

    var self = {
        initialize: function() {
            var lat = 0;
            var lng = 0;
            var zoom = 2;
            // set up initial map to be world view. also, add change
            // event so changing address will update the map
            existinglocation = self.getExistingLocation();
            if (existinglocation) {
                lat = existinglocation[0];
                lng = existinglocation[1];
                zoom = 18;
            }

            var latlng = new google.maps.LatLng(lat,lng);
            var myOptions = {
                zoom: zoom,
                center: latlng,
                mapTypeId: google.maps.MapTypeId.ROADMAP
            };
            map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
            if (existinglocation) {
                self.setMarker(latlng);
            }
        },

        getExistingLocation: function() {
            var geolocation = $('[data-gma-type="coordinates"]').val();
            if (geolocation) {
                return geolocation.split(',');
            }
        },

        codeAddress: function() {
            var address = $('[data-gma-type="address"]').val();
            geocoder.geocode({'address': address}, function(results, status) {
                if (status == google.maps.GeocoderStatus.OK) {
                    var latlng = results[0].geometry.location;
                    map.setCenter(latlng);
                    map.setZoom(18);

                    self.setMarker(latlng);
                    self.updateGeolocation(latlng);
                }
            });
        },

        setMarker: function(latlng) {
            if (marker) {
                self.updateMarker(latlng);
            } else {
                self.addMarker({'latlng': latlng, 'draggable': true});
            }
        },

        addMarker: function(Options) {
            marker = new google.maps.Marker({
                map: map,
                position: Options.latlng
            });

            var draggable = Options.draggable || false;
            if (draggable) {
                self.addMarkerDrag(marker);
            }
        },

        addMarkerDrag: function() {
            marker.setDraggable(true);
            google.maps.event.addListener(marker, 'dragend', function(new_location) {
                self.updateGeolocation(new_location.latLng);
            });
        },

        updateMarker: function(latlng) {
            marker.setPosition(latlng);
        },

        updateGeolocation: function(latlng) {
            $('[data-gma-type="coordinates"]').val(latlng.lat() + "," + latlng.lng());
        }
    };

    return self;
}


var bind_city_autocomplete = function($inputs) {
    var bind_inputs;
    bind_inputs = function ($inputs) {
        $inputs.each(function (i, el) {

            var $input = $inputs.eq(i);
            var autocomplete;
            var opts = {
                //componentRestrictions: {country: "ru"},
                place_changed: function () {
                    var result = autocomplete.getPlace();
                    if (result) {
                        $input.val(result["name"]);
                    }
                }
            };
            console.log(el)
            autocomplete = new google.maps.places.Autocomplete(el, opts);
            canvas = googleMapAdmin();
            canvas.initialize();
            canvas.codeAddress();
            autocomplete.addListener('place_changed', function (){
                canvas.codeAddress();
            });
        });
    };

    bind_inputs($inputs);

};



$(document).ready(function() {
    bind_city_autocomplete($('[data-gma-type="address"]'));
    $("form").on('keydown', function(event) {
        if (event.keyCode && event.keyCode == 13) {
            return false;
        }
    });
});