var mapelements = function(selector) {
    var $map_container = $(selector);

    var settings = {
        map_url: false,
        marker_url: false,
        token: false
    };

    var markers = {};
    var map;

    var value_or_false = function(value) {
        return typeof(value) === "undefined" ? false : value;
    };

    var setup_map = function () {
        var marker_shape = {
            coords: [11, 1, 20, 10, 11, 32, 1, 10],
            type: 'poly'
        };

        var marker_icon = {
            url: "/media/images/map-marker.png",
            size: new google.maps.Size(105, 55),
            origin: new google.maps.Point(0, 0),
            anchor: new google.maps.Point(55, 45)
        };

        var mapOptions = {
            mapTypeId: google.maps.MapTypeId.ROADMAP,
            'scrollwheel': false,
            streetViewControl: false,
            overviewMapControl: false,
            mapTypeControl: false
        };

        var markers_count = 0;
        var latlngbounds = new google.maps.LatLngBounds();
        var infowindow = new google.maps.InfoWindow({
            pixelOffset: new google.maps.Size(-0, 13)
        });

        var show_infowindow = function(map_marker, id) {

            if (typeof(markers[id].html_content) === "undefined") {
                markers[id].html_content = "<i class='marker-loading'></i>";

                $.ajax({
                    url: settings.marker_url,
                    type: 'POST',
                    data: {
                        csrfmiddlewaretoken: settings.token,
                        id: id
                    },

                    success: function (data) {
                        if (data["success"] === true) {
                            markers[id].html_content = data["html_content"];
                            infowindow.setContent(data["html_content"]);
                            infowindow.open(map, map_marker);
                            // $(".fakefancy_" + id).easyPhotoSwipe({use_zoom_effect: false})
                        } else {
                            infowindow.close();
                        }
                    },
                    error: function (textStatus) {
                        infowindow.close();
                    }
                });
            }

            infowindow.setContent(markers[id].html_content);
            infowindow.open(map, map_marker);
            // $(".fakefancy_" + id).easyPhotoSwipe({use_zoom_effect: false})
        };

        var create_markers = function(markers_obj) {
            $.each(markers_obj, function(marker_id, marker) {
                markers_count++;
                var coord = (marker.coordinates.split(','))
                var newLatLng = new google.maps.LatLng(coord[0], coord[1]);

                var new_marker = new google.maps.Marker({
                    position: newLatLng,
                    map: map,
                    icon: marker_icon,
                    // shape: marker_shape
                });

                google.maps.event.addListener(new_marker, 'click', (function(new_marker, i) {
                    return function() {
                        show_infowindow(new_marker, marker_id);
                    }
                })(new_marker, marker_id));

                latlngbounds.extend(newLatLng);
            });
        };


        map = new google.maps.Map($map_container[0], mapOptions);

        create_markers(markers);

        $map_container.toggleClass("active", true);
        $map_container.toggleClass("loading", false);
        window.setTimeout(function(){
            map.setCenter(latlngbounds.getCenter());

            if (markers_count > 1) {
                map.fitBounds(latlngbounds);
            } else {
                map.setZoom(16);
            }
        },650);
    };

    var build_map = function () {
        if (settings.map_url !== false && settings.token !== false) {
            console.log("setup map");
            $.ajax({
                url: settings.map_url,
                type: 'POST',
                data: {
                    csrfmiddlewaretoken: settings.token
                },
                success: function (data) {
                    if (data["success"]) {
                        if (data["has_markers"]) {
                            markers = data["markers"];
                            $map_container.toggleClass("open", true);
                            $map_container.toggleClass("loading", true);
                            $.cachedScript( data["api_script_url"] ).done(function( script, textStatus ) {
                                setup_map();
                            })
                        }
                    }
                },
                error: function (textStatus) {}
            });
        }
    };

    var init = function () {
        if ($map_container.length > 0) {
            settings.map_url = value_or_false($map_container.attr("data-get-map-url"));
            settings.marker_url = value_or_false($map_container.attr("data-get-marker-url"));
            settings.token = value_or_false($map_container.attr("data-token"));

            var vp_offset = "0%";
            try {
                vp_offset = (-1 + $(window).width()/window.innerWidth) * 100 + "%"
            } catch (e) {}
            $map_container.viewportChecker({
                offset: vp_offset,
                callbackFunction: function(){
                    build_map();
                }
            });
        }
    };

    init();
};