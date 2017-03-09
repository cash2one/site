//TODO: refactor this

$(document).ready(function() {
    "use strict";
    var $order_form = $('#js-address_order_form');

    if ($order_form.length > 0) {
        $('#js-address_order_summary').show();
        $order_form.not_loading = true;

        $order_form.submit(function(event) {
            console.log('onsubmit');
            event.preventDefault();
            form_submit();
        });

        var bind_buttons = function() {
            $order_form.find('[type="submit"]').each(function(i,el){
                $(el).on('click', function(e) {
                    e.preventDefault();
                    form_submit(el);
                });
            });
            $order_form.find('.js-address_order_checkbox').on('click', function(){
                form_submit({name: 'make_order', value: 'make_order'});
            });
        };

        var toggle_form = function(not_loading) {
            $order_form.not_loading = not_loading;
            $order_form.toggleClass("loading", !not_loading);
        };

        bind_buttons();

        var form_submit = function(button_object) {
            console.log('call', button_object);
            if ($order_form.not_loading === true) {
                toggle_form(false);

                var formURL = $order_form.attr("action");
                var formData = $order_form.serialize();
                if (button_object) {
                    if (button_object.name) {
                        console.log(button_object.value);
                        formData += "&" + button_object.name + "=" + button_object.value;
                    }
                }
                return $.ajax({
                    url: formURL,
                    type: 'GET',
                    data:  formData,
                    success: function(data) {
                        toggle_form(true);

                        if (data['data']) {
                            $order_form.html(data['data']);
                            bind_buttons();

                            $('select').select2({
                                minimumResultsForSearch: Infinity
                            });
                            
                        }
                    },
                    error: function(textStatus) {
                        toggle_form(true);
                    }
                });
            }
        }
    }
});