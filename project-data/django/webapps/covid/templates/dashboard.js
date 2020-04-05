var endpoint= '/covid/api/{{highlight}}';
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
	            borderColor:"red"
	        },
	        {
	            label: '# of Critical',
	            data: data.critical,
	            borderColor:"Yellow"
	        },
	        {
	            label: '# of Recovered',
	            data: data.recovered,
	            borderColor:"Green"
	        }

	        ]
		},
		options : {
			title: { 
				display:true,
				text:data.country
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
        backgroundColor: data.barcolor,
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
