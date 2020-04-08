var endpoint= '/covid/api/state/{{state}}';
var defaultData = [];
var labels = [];
var ctx = document.getElementById('myChart').getContext('2d');
function chart1(data) {
	new Chart(ctx, {
	    type: 'line',

	    data: {
	    	labels:data.labels,
	        datasets: [
/*
	        {
	            label: '# of Tested',
	            data: data.tested,
	            fill: true,
	            pointRadius: 2,
	            borderWidth: 0,
	            backgroundColor: "#7c77b9"
	        },
	        {
	            label: '# of Positive',
	            data: data.positive,
	            fill: true,
	            pointRadius: 2,
	            borderWidth: 0,
	            backgroundColor: "#0bc9cd"
	        },
*/
	        {
	            label: '# of Deaths',
	            data: data.deaths,
	            fill: true,
	            pointRadius: 2,
	            borderWidth: 0,
	            backgroundColor: "#ff6600"
	        }

	        ]
		},
		options : {
			title: { 
				display:true,
				text:data.state
            		}
			// scales: {
			// 	yAxes: [{
			// 		stacked: true
			// 	}]
			//}
		}
	})


}
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
