var input_delay = (function() {
    var timer = 0;
    return function(callback, ms) {
        clearTimeout (timer);
        timer = setTimeout(callback, ms);
    };
})();

var init_sticky_top_menu = function() {
    "use strict";

    var $detect = $("#sticky_detect");
    var $menu = $("#sticky_menu");

    if( $menu.length ) {
        var mar_top = $detect.offset().top;
        var scroll = 0;
        var $doc = $(document);

        var sticky_top_menu = function() {
            scroll = $doc.scrollTop();
            if ( scroll > mar_top ) {
                $menu.toggleClass("sticky", true);
            } else {
                $menu.toggleClass("sticky", false);
            }
        };

        $(window).scroll(function() {
            input_delay(sticky_top_menu, 70);
        });
    }
};