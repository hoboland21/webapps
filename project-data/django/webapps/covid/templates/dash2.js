var endpoint= '/covid/api/state/{{state}}';
var defaultData = [];
var labels = [];
//var ctx = document.getElementById('myChart').getContext('2d');

$.ajax({
	method: "GET",
	url: endpoint,
	success: function(data) {
		console.log(data);
		chart1(data);
		
	},
		error: function(error_data) {
		console.log("error",error_data);

	}
})
