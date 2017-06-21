$(document).ready(function() {

	$("#modalbutton").click(function(even){
					even.preventDefault()

	        $("#messagemodal").modal('show');
	    });

	$('#mass').on('submit', function(events) {
		events.preventDefault()
		console.log("form submitted!")  // sanity check
		var formData = $("#mass").serializeArray()
		$.ajax({
			url: "/profile/message",
			data: formData,
			type: 'post',
			dataType: 'json',
			success: function (data) {
				if (data.form_is_valid) {
					$("#messagemodal").modal('hide');

				}

			}
		});
	});



});
