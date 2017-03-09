$(document).ready(function() {
    "use strict";

    var source_content_name = "source_content";
    var source_content_name_id = "id_" + source_content_name;

    var $select_type = $("#id_name");
    var $select_template = $("#id_template");

    var $current_input = $("#" + source_content_name_id);
    var current_template = $select_template.val();
    var $input_wrapper = $current_input.parent();

    var current_value = $current_input.val();
    var current_set;

    var templates = {
        phone :[
            ["phone_mobile","мобильный"]
        ],
        html: [
            ["email","E-mail"],
            ["skype","skype"],
            ["address","адрес"],
            ["phone","Телефоны"],
            ["html","Визуальный редактор"]
        ],
        only_html: [
            ["html","Визуальный редактор"]
        ]

    };

    var widget_processors = {
        phone_mobile: function() {
            $current_input.mask("+7 999 999 99 99", {placeholder:"+7 xxx xxx xx xx"});
        },
        html : function() {
            tinyMCE.init({"elements": source_content_name_id, "force_br_newlines": "true", "theme_advanced_toolbar_align": "left",  "content_css": "/media/css/bootstrap.css, /media/css/corporate.css, /media/css/font-awesome.css", "forced_root_block": "", "file_browser_callback": "djangoFileBrowser", "height": "500px", "directionality": "ltr", "plugins": "spellchecker,pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template", "force_p_newlines": "false", "theme_advanced_statusbar_location": "bottom", "theme_advanced_toolbar_location": "top", "language": "en", "theme_advanced_buttons4": "insertlayer,moveforward,movebackward,absolute,|,styleprops,spellchecker,|,cite,abbr,acronym,del,ins,attribs,|,visualchars,nonbreaking,template,blockquote,pagebreak,|,insertfile,insertimage", "theme_advanced_buttons1": "save,newdocument,|,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,|,styleselect,formatselect,fontselect,fontsizeselect", "theme_advanced_buttons3": "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr,|,print,|,ltr,rtl,|,fullscreen", "theme_advanced_buttons2": "cut,copy,paste,pastetext,pasteword,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,help,code,|,insertdate,inserttime,preview,|,forecolor,backcolor", "width": "90%", "theme": "advanced", "strict_loading_mode": 1, "mode": "exact", "external_link_list_url": "/tinymce/flatpages_link_list/", "spellchecker_languages": "Russian=ru,+English=en", "extended_valid_elements": "iframe[name|src|framespacing|border|frameborder|scrolling|title|height|width],object[declare|classid|codebase|data|type|codetype|archive|standby|height|width|usemap|name|tabindex|align|border|hspace|vspace]"});
        },
        skype : function() {
            console.log("skype", $current_input.val());
        },
        address : function() {
            console.log("address", $current_input.val());
        },
        email : function() {
            console.log("email", $current_input.val());
        },
        phone : function() {
            console.log("phone", $current_input.val());
        }
    };

    var update_template_options = function() {
        $select_template.empty();
        $.each(templates[current_set],function(index,el){
            $select_template.append('<option value="'+el[0]+'">' +el[1] +'</option>');
        });
        if (current_template) {
            $select_template.val(current_template);
        } else {
            $select_template.val(templates[current_set][0])
        }
    };

    var dispatch_template_options = function(value) {
        if (['header_phone1','header_phone2'].indexOf(value) > -1) {
            current_set = "phone";
        } else {
            if (value == "requisites") {
                current_set = "only_html";
            } else {
                current_set = "html";
            }
        }
        current_template = $select_template.val();
        update_template_options();
    };

    var update_input = function(template_key) {
        current_value = $current_input.val();
        $input_wrapper.empty();
        if (current_set === "phone") {
            $current_input = $("<input>", {
                id: source_content_name_id,
                name : source_content_name,
                type: "text"
            });
            $current_input.val(current_value)
        } else {
            $current_input = $("<textarea>", {
                id: source_content_name_id,
                name : source_content_name
            });
            $current_input.val(current_value)
        }

        $input_wrapper.append($current_input);
        widget_processors[template_key]();
    };

    $select_type.on("change", function() {
        current_value = $current_input.val();
        dispatch_template_options($select_type.val());
        update_input($select_template.val())
    });

    $select_template.on("change", function() {
        current_value = $current_input.val();
        update_input($select_template.val())
    });

    dispatch_template_options($select_type.val());
    update_input($select_template.val())
});










