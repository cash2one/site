"use strict";

var frontMap = function( map_container ) {

    //FIX ME (maybe not)
    var regions = [
        {
            city_id: 'magnitogorsk',
            svg_path: 'M 153 421 L 154 420 L 156 419 L 162 413 L 176 415 L 180 418 L 180 432 L 170 440 L 156 440 L 153 443 Z',
            city_name: 'Магнитогорск',
            city_name_path: {x: 182, y: 425},
            city_marker_path: 'M167,422a4,4 0 1,0 8,0a4,4 0 1,0 -8,0Z',
            city_capital: false
        },
        {
            city_id: 'zlatoust',
            svg_path: 'M 199 165 L 202 165 L 209 158 L 213 158 L 215 160 L 212 164 L 211 167 L 217 174 L 216 177 L 212 183 L 207 183 L 198 174 Z',
            city_name: 'Златоуст',
            city_name_path: {x: 190, y: 160},
            city_marker_path: 'M206,170a4,4 0 1,0 8,0a4,4 0 1,0 -8,0Z',
            city_capital: false
        },
        {
            city_id: 'miass',
            svg_path: 'M 235 184 L 245 167 L 245 164 L 249 159 L 249 164 L 251 165 L 250 166 L 246 176 L 244 182 L 247 185 L 247 188 L 246 190 L 244 198 L 241 198 L 239 200 L 239 203 L 237 203 L 238 199 L 234 196 Z',
            city_name: 'Миасс',
            city_name_path: {x: 253, y: 190},
            city_marker_path: 'M238,186a4,4 0 1,0 8,0a4,4 0 1,0 -8,0Z',
            city_capital: false
        },
        {
            city_id: 'chebarkul',
            svg_path: 'M 271 196 L 276 192 L 282 192 L 288 193 L 295 196 L 292 205 L 291 215 L 279 222 L 275 216 L 275 202 Z',
            city_name: 'Чебаркуль',
            city_name_path: {x: 293, y: 205},
            city_marker_path: 'M279,200a4,4 0 1,0 8,0a4,4 0 1,0 -8,0Z',
            city_capital: false
        },
        {
            city_id: 'chelyabinsk',
            svg_path: 'M 376 155 L 372 163 L 373 168 L 375 168 L 375 174 L 377 175 L 377 185 L 381 189 L 381 191 L 374 191 L 372 195 L 367 200 L 363 194 L 358 197 L 356 196 L 358 194 L 360 193 L 360 190 L 356 188 L 357 184 L 353 182 L 353 174 L 355 173 L 355 167 L 359 163 L 359 157 L 363 154 L 367 154 L 370 157 Z',
            city_name: 'Челябинск',
            city_name_path: {x: 323, y: 151},
            city_marker_path: 'M356,165a7,7 0 1,0 14,0a7,7 0 1,0 -14,0Z',
            city_capital: true
        },
        {
            city_id: 'troitsk',
            svg_path: 'M 371 338 L 372 334 L 379 329 L 392 330 L 394 334 L 394 338 L 391 339 L 392 345 L 389 345 L 386 345 L 382 350 L 380 354 L 380 354 L 379 350 L 378 348 L 375 348 L 374 346 Z',
            city_name: 'Троицк',
            city_name_path: {x: 374, y: 326},
            city_marker_path: 'M376,336a4,4 0 1,0 8,0a4,4 0 1,0 -8,0Z',
            city_capital: false
        },
        {
            city_id: 'yuzhnouralsk',
            svg_path: 'M 343 284 L 343 280 L 345 277 L 346 273 L 352 270 L 364 270 L 369 276 L 370 283 L 367 284 L 362 287 L 357 288 L 355 289 L 351 289 L 348 286 L 345 286 Z',
            city_name: 'Южноуральск',
            city_name_path: {x: 309, y: 260},
            city_marker_path: 'M356,275a4,4 0 1,0 8,0a4,4 0 1,0 -8,0Z',
            city_capital: false
        }
    ];

    var options = {
        map_container: null,
        svg_node: null
    };

    function initMap(){

        var mapContainerObject = $( map_container );

        if( mapContainerObject.length ) {
            options.map_container = mapContainerObject;

            constructMap();

        }

    }

    function constructMap(){

        var data = typeof (window.index_map_data) === "undefined" ? false : window.index_map_data;

        if( data ) {

            options.svg_node = document.createElementNS("http://www.w3.org/2000/svg",'svg');
            options.svg_node.setAttribute('width', 534);
            options.svg_node.setAttribute('height', 636);
            options.svg_node.setAttribute('class', 'program-chel-map-svg');
            options.map_container.append(options.svg_node);

            for( var i = 0; i < data.length; i++ ) {
                var object = data[i];

                var city = findCity(object);

                if( city ) {

                    //граница района
                    var city_path = document.createElementNS("http://www.w3.org/2000/svg",'path');
                    city_path.setAttribute('d', city.svg_path);
                    city_path.setAttribute('id', city.city_id);
                    city_path.setAttribute('fill', 'none');
                    city_path.setAttribute('stroke', 'none');
                    city_path.setAttribute('style', 'pointer-events:all;cursor:pointer');
                    city_path.onmouseover = function(){
                        this.setAttribute('fill', '#8cc92e');
                        document.querySelector('[data-id="'+this.getAttribute('id')+'"]').setAttribute('fill', '#8cc92e');
                    }
                    city_path.onmouseleave = function(){
                        this.setAttribute('fill', 'none');
                        document.querySelector('[data-id="'+this.getAttribute('id')+'"]').setAttribute('fill', '#3e2d8c');
                    }

                    options.svg_node.appendChild(city_path);

                    //Текст с названием города
                    var city_name = document.createElementNS("http://www.w3.org/2000/svg",'text');
                    city_name.setAttribute('x', city.city_name_path.x);
                    city_name.setAttribute('y', city.city_name_path.y)
                    city_name.setAttribute('fill', '#ffffff');
                    city_name.setAttribute('font-size', (city.city_capital ? '18' : '15') );
                    city_name.setAttribute('font-family', 'GothamProMedium');
                    city_name.setAttribute('style','text-shadow:0 0px 8px #141b0a');
                    city_name.textContent = city.city_name;
                    options.svg_node.appendChild(city_name);

                    //Маркер города
                    var city_label = document.createElementNS("http://www.w3.org/2000/svg",'path');
                    city_label.setAttribute('d', city.city_marker_path);
                    city_label.setAttribute('data-id', city.city_id);
                    city_label.setAttribute('fill', '#3e2d8c');
                    city_label.setAttribute('stroke', '#ffffff');
                    city_label.setAttribute('style', 'pointer-events:all;cursor:pointer');
                    city_label.setAttribute('stroke-width',(city.city_capital ? '3' : '2') );

                    city_label.onmouseover = function(){
                        this.setAttribute('fill', '#8cc92e');
                        document.querySelector('[id="'+this.getAttribute('data-id')+'"]').setAttribute('fill', '#8cc92e');
                    };
                    city_label.onmouseleave = function(){
                        this.setAttribute('fill', '#3e2d8c');
                        document.querySelector('[id="'+this.getAttribute('data-id')+'"]').setAttribute('fill', 'none');
                    };
                    options.svg_node.appendChild(city_label);

                    //всплывающий слой
                    createPopupLayer(city);



                }

            }

        }

    }

    function createPopupLayer(city_object) {
        var links = city_object.links ? city_object.links : [];

        var city_region = $('[id="'+city_object.city_id+'"]');
        var city_marker = $('[data-id="'+city_object.city_id+'"]');

        city_region.on('click', function(){
            window.location = city_object.url;
        });
        city_marker.on('click', function(){
            window.location = city_object.url;
        });
        if( links.length ) {
            var layer = $(document.createElement('div')).addClass('program-chel-map-popup').attr('data-popup-for',city_object.city_id).appendTo($(document.body));
            var layer_inner = $(document.createElement('div')).addClass('program-chel-map-popup-inner').appendTo(layer);

            for(var i = 0; i < links.length; i++) {
                var link = links[i];

                var anchor = $(document.createElement('a'))
                    .text(link.title)
                    .attr('href', link.url)
                    .appendTo(layer_inner);
            }



            $(window).on("resize", function(){
                setPosition(layer, city_marker);
            });

            setPosition(layer, city_marker);

            city_region.on("mouseover", function(e){showLayer(e,this);});
            city_region.on("mouseleave", function(e){showLayer(e,this);});

            city_marker.on("mouseover", function(e){showLayer(e,this);});
            city_marker.on("mouseleave", function(e){showLayer(e,this);});

        }
    }

    function showLayer(event,object) {
        var path = $(object),
            layer = $('[data-popup-for="'+ ( path.attr('id') || path.attr('data-id') ) +'"]'),
            marker = $('[data-id="'+ ( path.attr('id') || path.attr('data-id') ) +'"]');

        var timer = true;

        layer.on("mouseover", function(){
            layer.show();
            timer = false;
        });
        layer.on("mouseleave", function(){
            layer.hide();
            timer = true;
        });

        if( event.type === 'mouseover' ) {
            layer.show();
            setPosition(layer, marker);
            timer = false;
        } else if( event.type === 'mouseleave' ) {
            //if( timer ) {
            //setTimeout(function(){
            layer.delay(1500).hide();
            //  }, 1500);
            //}
        }

    }

    function setPosition(layer, marker) {
        var city_marker_position = marker[0].getBoundingClientRect();

        layer.css({
            'top': city_marker_position.top + window.pageYOffset - layer.outerHeight() + 10,
            'left': city_marker_position.left - layer.outerWidth()/2 + (city_marker_position.right - city_marker_position.left)/2
        });
    }

    function findCity(city) {

        var object = null;

        for( var i = 0; i < regions.length; i++ ) {

            var region = regions[i];

            if(region.city_id === city.id ) {
                object = region;
                object.url = city.url;
                if( city.hasOwnProperty('links') ) {
                    object.links = city.links;
                }

            }

        }


        return object;
    }


    initMap();

};