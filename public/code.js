var main = function () {
	$(document).keydown(function (event) {
		$.ajax({
			type: "PUT",
			url: "/control",
			data: {"direction":""}
		}).done(function() { });
	});
};

$(document).ready(main);
