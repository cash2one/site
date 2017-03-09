"use strict";

var loadCityMap = function( map_id, filter_type ) {

    var settings = {
        map_container: null,
        map: null,
        options: {
            center: {},
            zoom: 11
        },
        filter_type: null,
        markers: [],
        useInfoWindows: true,
        infoWindowUrl: "/get_geobject_info/" //TODO: выцепить из шаблона по {% url %}
    };

    function init_map() {
        var map_object = $(map_id);

        if( map_object.length ) {
            settings.map_container = map_object;
        }

        var filter_object = $(filter_type);

        if( filter_object.length ) {
            settings.filter_type = filter_object;
        }

        settings.useInfoWindows = typeof (map_object.data('use-infowindows')) !== 'undefined';

        if (settings.map_container) {
            if( typeof google === 'undefined') {
                $.cachedScript( map_object.data('api-url') ).done(function( script, textStatus ) {
                    create_map();
                });
            } else {
                create_map();
            }
        }
    }

    function create_map() {

        var data = typeof (window.city_marker_data) === "undefined" ?  false : window.city_marker_data;
        if( data ) {
            settings.options.center = {lat: parseFloat(data[0].coords[0]), lng: parseFloat(data[0].coords[1])};

            settings.map =  new google.maps.Map(settings.map_container[0], settings.options);

            var LatLngList = [];
            for( var  i = 0; i < data.length; i++ ) {

                var point = data[i];

                LatLngList.push(new google.maps.LatLng (parseFloat(point.coords[0]), parseFloat(point.coords[1])));


                var marker = new google.maps.Marker({
                    position: {lat: parseFloat(point.coords[0]), lng: parseFloat(point.coords[1])},
                    map: settings.map,
                    type: point.type,
                    object_id: point.object_id
                });

                setIcon(marker,'');

                var infoWindow = new google.maps.InfoWindow();

                var current_marker = null;

                if (settings.useInfoWindows) {
                    google.maps.event.addListener(marker,'click', function() {
                        resetIcons();
                        setIcon(this,'active');
                        showInfowindowContent(this, infoWindow);
                        current_marker = this;
                    });

                    google.maps.event.addListener(infoWindow,'closeclick',function(){
                        resetIcons();
                    });

                    google.maps.event.addListener(infoWindow, 'domready', function() {

                        var iwOuter = $('.gm-style-iw');
                        var iwBackground = iwOuter.prev();
                        iwOuter.addClass('gm-style-iw-city');
                        iwOuter.parent().parent().css({left: '20px'});
                        iwOuter.next().css({'border-radius' : '15px', 'top': 'auto', 'bottom': iwOuter.outerHeight() - 20 + 'px', 'right': '65px'});
                        iwBackground.children(':nth-child(2)').css({'display' : 'none'});
                        iwBackground.children(':nth-child(4)').css({'display' : 'none'});
                        iwBackground.children(':nth-child(1)').addClass('gm-style-iw-corner').attr('style', function(i,s){ return s + 'left: 100px !important;'});
                        iwBackground.children(':nth-child(3)').addClass('gm-style-iw-corner').attr('style', function(i,s){ return s + 'left: 100px !important;'});
                        iwBackground.children(':nth-child(3)').find('div').children().css({'box-shadow': 'none','background-color': '#271961'});
                    });
                }

                /*google.maps.event.addListener(marker,'mouseover', function() {
                 resetIcons();
                 setIcon(this,'hover');
                 });

                 google.maps.event.addListener(marker,'mouseout', function() {
                 resetIcons();
                 setIcon(this,'');
                 });*/

                settings.markers.push(marker);
            }

            var latlngbounds = new google.maps.LatLngBounds();

            LatLngList.forEach(function(latLng){
                latlngbounds.extend(latLng);
            });


            settings.map.setCenter(latlngbounds.getCenter());

            if( data.length > 1 ) {
                settings.map.fitBounds(latlngbounds);
            }  else {
                settings.map.setZoom(16);
            }

        }

        if( settings.filter_type ) {
            settings.filter_type.on("click", set_filter);
        }

        window.setTimeout(function(){
            // Это для selenium, нех тут удивляться
            $('body').append('<div id="its_a_print_page"></div>');
        }, 1500);
    }

    function showInfowindowContent(marker, infowindow) {
        if (typeof(marker.html_content) === "undefined") {
            marker.html_content = "<i class='marker-loading'></i>";

            $.ajax({
                url: settings.infoWindowUrl,
                type: 'GET',
                data: {
                    id: marker.object_id
                },

                success: function (data) {
                    if (data["success"] === true) {
                        marker.html_content = data["html_content"];

                        infowindow.setContent(marker.html_content);
                        infowindow.open(settings.map, marker);
                    } else {
                        infowindow.close();
                    }
                },
                error: function (textStatus) {
                    infowindow.close();
                }
            });
        }

        infowindow.setContent(marker.html_content);
        infowindow.open(settings.map, marker);
    }


    function resetIcons(){
        for( var i = 0; i < settings.markers.length; i++ ) {
            var marker = settings.markers[i];

            setIcon(marker, '');

        }
    }


    var marker_icon_types = typeof (window.marker_icon_types) === "undefined" ?  false : window.marker_icon_types;

    function setIcon(marker, action) {
        var type_url = marker_icon_types[marker.type];
        if (type_url) {
            var markerImage = new google.maps.MarkerImage(
                type_url,
                new google.maps.Size(30,30),
                new google.maps.Point(0,0),
                new google.maps.Point(0,30)
            );

            marker.setIcon(markerImage);
        }
    }


    function set_filter(e) {
        var _this = $(this),
            _type = _this.attr('data-type');

        if( !_this.hasClass('active') )	{

            settings.filter_type.removeClass('active');
            _this.addClass('active');

            for( var i = 0; i < settings.markers.length; i++ ) {
                var marker = settings.markers[i];

                if( marker.type === _type) {
                    marker.setVisible(true);
                } else {
                    marker.setVisible(false);
                }
            }

        } else {
            _this.removeClass('active');

            for( var i = 0; i < settings.markers.length; i++ ) {
                var marker = settings.markers[i];

                marker.setVisible(true);
            }

        }

    }

    init_map();
};