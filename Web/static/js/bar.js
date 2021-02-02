$(document).ready(function(){
var chart_labels = ['Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island'];
var injury_dataset = ['28', '43', '16', '21', '4'];
var crash_dataset = ['141', '276', '88', '175', '38'];
var ctx = document.getElementById("forecast").getContext('2d');
var config = {
    type: 'bar',
    data: {
        labels: chart_labels,
        datasets: [{
            type: 'line',
            label: "Injuries",
            yAxisID: "y-axis-0",
            fill: false,
            data: injury_dataset,
            backgroundColor: "#eaf8d3"
        }, {
            type: 'bar',
            label: "Number of Crashes",
            yAxisID: "y-axis-1",
            data: crash_dataset,
            backgroundColor: "#7bccc4"
        }]
    },
    options: {
        scales: {
            yAxes: [{
                position: "left",
                "id": "y-axis-0",
            }, {
                position: "right",
                "id": "y-axis-1",
            }]
        }
    }
};
var forecast_chart = new Chart(ctx, config);
$("#0").click(function() {
    var data = forecast_chart.config.data;
    data.datasets[0].data = injury_dataset;
    data.datasets[1].data = crash_dataset;
    data.labels = chart_labels;
    forecast_chart.update();
});
$("#1").click(function() {
    var chart_labels = ['Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island'];
    var injury_dataset = ['1.97', '1.68', '.84', '.93', '.98'];
    var crash_dataset = ['9.94', '10.78', '5.4', '7.76', '7.98'];
    var data = forecast_chart.config.data;
    data.datasets[0].data = injury_dataset;
    data.datasets[1].data = crash_dataset;
    data.labels = chart_labels;
    forecast_chart.update();
});

})