$(document).ready(function() {

    $('#createForm').on('submit', function() {
    	
    	$.ajax({
			url: $(this).attr('action'),
			type: $(this).attr('method'),
			data: $(this).serialize(),
			dataType: 'json',
			success: function(data) {				
				$.each(data, function(key, value){	
					if(key!="error") {
						$("#giveLink").addClass("alert alert-success");
						$("#giveLink").html("<strong>" + key + "</strong>: "+"<input id=\"permalink\" type=\"text\" value=\"" + value +"\" onClick=\"javascript:focus();select();\" readonly=\"readonly\" />");
					}
					else {
						$("#giveLink").addClass("alert alert-error");
						$("#giveLink").html("<strong>" + key + "</strong>: "+value);
					}
					$('html, body').animate({ scrollTop: 0 }, 'slow');
				});	
			}
		});

        return false;
    });
});