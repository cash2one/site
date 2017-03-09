var sidebar = function() {
    "use strict";

    var bind_dropdown = function($toggler, $container) {
        $toggler.on("click", function(){
            $container.toggleClass("open");
        });
    };

    $(".sidebar .sidebar-caret").each(function(i, el) {
        var $el = $(el);
        bind_dropdown($el, $el.closest("li"));
    });
};
