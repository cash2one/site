var mobile_navbar =function() {
    "use strict";

    var $navbar = $("#navbar");
        $navbar.is_active = false;
    var $button = $("#toggle_navbar");
    var $backdrop = $("#navbar_backdrop");

    var show_navbar = function() {
        $navbar.toggleClass("active", true);
        $button.toggleClass("active", true);
        $backdrop.toggleClass("active", true);
        $navbar.is_active = true;
    };

    var hide_navbar = function() {
        $navbar.toggleClass("active", false);
        $button.toggleClass("active", false);
        $backdrop.toggleClass("active", false);
        $navbar.is_active = false;
    };

    $button.on("click", function(e) {
        e.preventDefault();
        if ($navbar.is_active === true) {
            hide_navbar();
        } else {
            show_navbar();
        }
    });

    $backdrop.on("click", function() {
        if ($navbar.is_active === true) {
            hide_navbar();
        }
    });

    $(document).keyup(function(e) {
        if (e.keyCode == 27) {
            hide_navbar();
        }
    });




    var prev_point = 0;
    var touch_dist = 0;
    var touch_busy = false;
    var swipe_threshold = 100;

    var open_threshold = 100;


    var evaluate_touch_start = function(start) {
        if ($navbar.is_active === false) {
            return start < open_threshold;
        } else {
            return true;
        }
    };

    var evaluate_touch = function (touch_dist) {
        if (Math.abs(touch_dist) > swipe_threshold) {
            if (touch_dist > 0) {
                show_navbar();
            } else {
                hide_navbar();
            }
        }
    };

    var $body = $("body");

    $body.on("touchstart", function (e) {
        if (touch_busy === false) {
            touch_busy = true;
            touch_dist = 0;


            prev_point = e.originalEvent.touches[0].pageX;
            if (evaluate_touch_start(prev_point) === true) {
                $body.on("touchmove", function (e) {
                    touch_dist += e.originalEvent.touches[0].pageX - prev_point;
                    prev_point = e.originalEvent.touches[0].pageX
                });
            }
        }
    });

    $body.on("touchend", function () {
        evaluate_touch(touch_dist);
        $body.unbind("touchmove");
        touch_dist = 0;
        touch_busy = false;
    });

};


