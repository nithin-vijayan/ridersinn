$(document).ready(function() {

    bootstrap_alert = function() {}
    bootstrap_alert.warning = function(message) {
        $('#successalert').html('<div class="alert alert-success alert-dismissable fade in"><a class="close" data-dismiss="alert">×</a><span>' + message + '</span></div>')
    }

    $("#add").click(function() {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function() {
                $("#messagemodal").modal("show");
            },
            success: function(data) {
                $("#chat-modal").html(data.html_form);
            }
        });
    });

    $("#modalbutton").click(function() {
        var btn = $(this);
        var data = {
            'touser': $("#modalbutton").attr("touser")
        }
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            data: data,
            dataType: 'json',
            beforeSend: function() {
                $("#messagemodal").modal("show");
            },
            success: function(data) {
                $("#chat-modal").html(data.html_form);
            }
        });
    });


    $("#friendform").submit(function(ve) {
        ve.preventDefault()
        console.log("form submitted!") // sanity check
        var formData = $("#friendform").serializeArray()
        $.ajax({
            url: "/profile/friendrequest",
            data: formData,
            type: 'post',
            dataType: 'json',
            success: function(data) {
                if (data.form_is_valid) {
                    $("#myModal").modal('hide');
                    bootstrap_alert.warning("myModal Sent !");
                }

            }
        });
    });

    $("#messagemodal").on('submit', function(e) {
        e.preventDefault()
        console.log("form submitted!") // sanity check
        var formData = $("#mass").serializeArray()
        $.ajax({
            url: "/profile/message",
            data: formData,
            type: 'post',
            dataType: 'json',
            success: function(data) {
                if (data.form_is_valid) {
                    $("#messagemodal").modal('hide');
                    bootstrap_alert.warning("Message Sent !");
                }
            }

        });

    });
});
