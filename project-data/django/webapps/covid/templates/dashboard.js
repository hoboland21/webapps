var endpoint= '/covid/api/{{country}}';
var defaultData = [];
var labels = [];
var ctx = document.getElementById('myChart').getContext('2d');

function chart1(data) {
	new Chart(ctx, {
	    type: 'line',

	    data: {
	    	labels:data.labels,
	        datasets: [
	        {
	            label: '# of Deaths',
	            data: data.deaths,
	            fill: true,
	            pointRadius: 2,
	            borderWidth: 0,
	            backgroundColor: "#ff6600"
	        },
	        {
	            label: '# of Critical',
	            data: data.critical,
	            fill: true,
	            pointRadius: 2,
	            borderWidth: 0,
	            backgroundColor: "#7c77b9"
	        },
	        {
	            label: '# of Recovered',
	            data: data.recovered,
	            fill: true,
	            pointRadius: 2,
	            borderWidth: 0,
	            backgroundColor: "#0bc9cd"
	        }

	        ]
		},
		options : {
			title: { 
				display:true,
				text:data.country
            		},
			scales: {
				yAxes: [{
					stacked: true
				}]
			}
		}
	})


}

function chart2(data) {

	new Chart(document.getElementById("pie-chart"), {
    type: 'bar',
    data: {
      labels: data.labels,
      datasets: [{
        label: "Daily Death Change",
        backgroundColor: "#8fbfe0",
        data: data.newdeaths
      }]
    },
    options: {
      title: {
        display: true,
        text: data.country
      }
    }
});
}

$.ajax({
	method: "GET",
	url: endpoint,
	success: function(data) {
		console.log(data);
		chart1(data);
		chart2(data);
	},
		error: function(error_data) {
		console.log("error",error_data);

	}
})
