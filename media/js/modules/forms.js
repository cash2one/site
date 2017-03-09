//TODO: refactor this

$(document).ready(function() {
    "use strict";
    var hide_errors_on_keydown = function() {
        $("form").find("input, textarea").each(function() {
            $(this).on("keydown",function() {
                $(this).toggleClass("has-error", false);
            });

        });
    };

    //Callback handler for form submit event
    var bind_ajax_submit = function () {
        $(document).find('form[remote="true"]').each(function(index, el) {
            var $el = $(el);

            $el.not_loading = true;

            $el.submit(function(event) {
                event.preventDefault();
                if ($el.not_loading === true) {
                    $el.toggleClass("loading", true);
                    $el.not_loading = false;
                    var formObj = $el;
                    var formURL = formObj.attr("action");
                    var formData = formObj.serialize();

                    return $.ajax({
                        url: formURL,
                        type: 'POST',
                        data:  formData,
                        success: function(data) {

                            var response_data = data;
                            var form_errors = response_data["form_errors"];

                            formObj.find("input, textarea, select").each(function () {
                                $(this).removeClass("has-error");
                            });

                            for (var error_class in form_errors) {
                                var el_name = "[name='"+error_class+"']";
                                formObj.find(el_name).addClass("has-error");
                            }

                            if (response_data["success"] === true) {
                                window.location.reload();
                            } else {
                                $el.not_loading = true;
                                $el.toggleClass("loading", false);
                            }
                        },
                        error: function(textStatus) {
                            $el.toggleClass("loading", false);
                            $el.not_loading = true;
                        }
                    });
                }
            });
        });
    };

    hide_errors_on_keydown();
    bind_ajax_submit();
});