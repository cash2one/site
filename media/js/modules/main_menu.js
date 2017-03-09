"use strict";

var main_menu = function( params ) {
	
	var default_params = {
		navbar: null,
		menu: null,
		menu_link: null,
		more: null,
		more_menu: null
	};

	if( typeof params === 'object' ) {
		default_params = $.extend({}, params);
	}

	if( $(default_params.navbar).length && 
		$(default_params.menu).length &&
		$(default_params.menu_link).length &&
		$(default_params.more).length &&
		$(default_params.more_menu).length ) {
       

        processMenu();
	}

	function processMenu() {

		var links = [],
		    navbar = $(default_params.navbar),
		    more = navbar.find(default_params.more),
		    menu = navbar.find(default_params.menu),
		    more_menu = navbar.find(default_params.more_menu);
        
        function get_links_width() {
        	var menu_links_width = 0;
            menu.addClass('initial');

			for( var i = 0; i < menu.find(default_params.menu_link).length; i++ ) {
				var link_obj = $( menu.find(default_params.menu_link)[i] );
				menu_links_width += link_obj.outerWidth();
			}

			menu.removeClass('initial');

			return menu_links_width;
        }

        function watchMenu(){

		    var available_space = more.hasClass('is-hidden') ? navbar.outerWidth() : navbar.outerWidth() - more.outerWidth();
            //console.log(available_space);

		    if( get_links_width() > available_space ) {
                
                links.push( get_links_width() );

                menu.find(default_params.menu_link).last().prependTo(more_menu);

                if( more.hasClass('is-hidden')) {
			       more.removeClass('is-hidden');
			       menu.addClass('watch-state');
			    }

		    } else {
                
                if( available_space > links[links.length-1]) {

				    more_menu.find(default_params.menu_link).first().appendTo(menu);
				    links.pop();

				}

				    
				if( links.length < 1) {

				    more.addClass('is-hidden');
				    menu.removeClass('watch-state');
				    
				}

		    }

		    if( get_links_width() > available_space) {
			    watchMenu();
			}

		}
		var $w = $(window);

		$w.resize(function() {
		    watchMenu();
		});

		$w.load(function() {
		    watchMenu();
		});
		
		watchMenu();


		/*var menu_links_width = 0,
		    more_width = $(default_params.more).outerWidth();

		for( var i = 0; i < $(default_params.menu_link).length; i++ ) {
			var link_obj = $( $(default_params.menu_link)[i] );
			menu_links_width += link_obj.outerWidth(true);
		}

		var available_space = $(default_params.navbar).outerWidth(true) - more_width;

		if ( menu_links_width > available_space ) {
		    
		    var last_link = $(default_params.menu_link).last();

		    last_link.attr('data-width', last_link.outerWidth(true));

		    last_link.prependTo(default_params.more_menu);

		    processMenu();

		  } else {

		    var first_more_link = $(default_params.more_menu).find('li').first();

		    if ( menu_links_width + first_more_link.data('width') < available_space) {

		      first_more_link.insertBefore(default_params.more);

		    }

		  }
		  
		  if ( $(default_params.more_menu).find('li').length > 0) {

		    $(default_params.more).css({'display':'inline-block'});

		  } else {

		    $(default_params.more).css({'display':'none'});

		  }*/

	}

};