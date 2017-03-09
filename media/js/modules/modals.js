var init_modalz = function(el, toggler, destroy, callback) {
    destroy = (typeof destroy === "undefined") ? true : destroy;
    toggler = (typeof toggler === "undefined") ? false : toggler;

    var $content = el.find("[data='modal-content']");

    var position_modal = function() {
        var where = $(document).scrollTop()+($(window).height()-$content.height())/2;
        if ( where < 0 ) {
            where = 0;
        }
        where = where+"px";
        $content.css("margin-top", "0px");
        $content.css("top", where);
    };

    if (destroy === true) {
        position_modal();
    }

    var show_modal = function() {
        el.toggleClass("active", true);
        position_modal();
        if (callback) {
            callback();
        }
    };

    var hide_modal = function() {
        if (destroy === true) {
            el.remove();
        } else {
            el.toggleClass("active", false);
        }
    };

    el.find("[data='close-modal']").on("click", function(e) {
        e.preventDefault();
        hide_modal();
    });

    if (toggler !== false) {
        toggler.on("click", function(e){
            e.preventDefault();
            show_modal();
        });
    }

    $(document).keyup(function(e) {
        if (e.keyCode == 27) {
            hide_modal();
        }
    });
};