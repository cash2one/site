"use strict";

var YaHelper = new Object();
YaHelper.ya_counter = false;
YaHelper.get_ya_counter = function() {
    try {
        YaHelper.ya_counter = Ya._metrika.counter;
        return true;
    } catch(e) {
        return false;
    }
};

YaHelper.reachgoal = function(key, callback) {
    if (key.length) {
        if (YaHelper.get_ya_counter() !== false) {
            YaHelper.ya_counter.reachGoal(key, callback());
        }
    }
};

$(document).ready(function() {


    // scroll-to-top-button
    $(function() {
        $('.backtotop').click(function(){
            $('html, body').animate({scrollTop:0}, 'slow');
        });
    });

    // owl-carousel
    var $backgrounds = $(".owlslider__slide__background");

    $('.owl-carousel').owlCarousel({
        items: 1,
        margin: 100,
        singleItem: true,
        autoPlay: 4000,
        afterAction: function(el) {
            $backgrounds.removeClass('active');
            $backgrounds.eq(this.currentItem).addClass('active');
        },
        pagination: true,
        navigation: false,
        navigationText: [
            '<button class="btn"><i class="fa fa-angle-left"></button>',
            '<button class="btn"><i class="fa fa-angle-right"></i></button>'
        ]
    });

    init_modalz($("#feedbackModal"), $(".show_feedback_form"), false);

    init_modalz($("#basicModal"), false, true);

    var $managers = $(".show_manager_form");
    if ($managers.length > 0) {
        var $manager_modal = $("#managerModal");
        var $manager_input = $manager_modal.find('[name="manager"]');
        $managers.each(function(i) {
            init_modalz(
                $manager_modal,
                $managers.eq(i),
                false,
                function() {
                    $manager_input.val($managers.eq(i).data('manager-id'));
                }
            );
        });
    }


    //init_sticky_top_menu();
    mobile_navbar();
    sidebar();
    mapelements("#mapa");

    var main_menu_params = {
                navbar: '.js-main-menu-wrap',
                menu: '.js-main-menu',
                menu_link: '.js-main-menu-link',
                more: '.js-more-links',
                more_menu: '.js-more-links-menu'
    };

    FontFaceOnload("GothamProMedium", {
        success: function() {
            main_menu(main_menu_params);
        },
        error: function() {},
        timeout: 5000 // in ms. Optional, default is 10 seconds
    });

    // main_menu(main_menu_params);

    $('select').select2({
        minimumResultsForSearch: Infinity
    });
    
    
    if( $('.js-input-date').length ) {
        $.datepicker.setDefaults( $.datepicker.regional[ "ru" ] );

        $('.js-input-date').datepicker({
            dateFormat: "dd-mm-yy",
            showOtherMonths: true,
            beforeShow: function (textbox, instance) {
                var docHeight = $(document).height();
                var bodyHeight = $(document.body).height();
                var txtBoxOffset = $(this).offset();
                var top = txtBoxOffset.top;
                var left = txtBoxOffset.left;
                var txtHeight = $(this).outerHeight();
                var datePickerHeight = $('.ui-datepicker').outerHeight();
                var bottom = bodyHeight - top + 12;
                setTimeout(function () {
                    instance.dpDiv.css({
                        top: 'auto',
                        bottom: bottom,
                        left: left
                    });
                }, 50);

            },
            onChangeMonthYear: function(year, month, instance) {
                var docHeight = $(document).height();
                var bodyHeight = $(document.body).height();
                var txtBoxOffset = $(this).offset();
                var top = txtBoxOffset.top;
                var left = txtBoxOffset.left;
                var txtHeight = $(this).outerHeight();
                var datePickerHeight = $('.ui-datepicker').outerHeight();
                var bottom = bodyHeight - top + 12;
                setTimeout(function () {
                    instance.dpDiv.css({
                        top: 'auto',
                        bottom: bottom,
                        left: left
                    });
                }, 50);
            }
        });

    }

    if( $('.js-load-box').length ) {
        window.sr = ScrollReveal({ reset: false });
        sr.reveal('.js-load-box', { duration: 550, scale: 0.5});
    }

    loadCityMap('#city-map', '.js-promo-type');
    loadCityMap('#pasport-map');
    $(".fakefancy").easyPhotoSwipe({use_zoom_effect: true});

    frontMap('.js-city-map-container');

});
