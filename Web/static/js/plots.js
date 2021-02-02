d3.csv("../ETL/Data/CrashImpacts.csv").then(function(crashImpacts) {

  console.log(crashImpacts);



  // Cast the hours value to a number for each piece of tvData
  crashImpacts.forEach(function(d) {
    d.PersonsInjured = +d.PersonsInjured;
    d.PersonsKilled = +d.PersonsKilled;
    d.PedestriansInjured = +d.PedestriansInjured;
    d.PedestriansKilled = +d.PedestriansKilled;
    d.CyclistInjured = +d.CyclistInjured;
    d.CyclistKilled = +d.CyclistKilled;
    d.MotoristInjured = +d.MotoristInjured;
    d.MotoristKilled = +d.MotoristKilled;
 
    var boroughlist= crashImpacts.map(d=>d.Borough) 
    var personsinjuredlist = crashImpacts.map(d=>d.PersonsInjured)
      var personskilledlist = crashImpacts.map(d=>d.PersonsKilled)
      var pedestriansinjuredlist = crashImpacts.map(d=>d.PedestriansInjured)
      var pedestrianskilledlist = crashImpacts.map(d=>d.PedestriansKilled)
      var cyclistinjuredlist = crashImpacts.map(d=>d.CyclistInjured)
      var cyclistkilledlist = crashImpacts.map(d=>d.CyclistKilled)
      var motoristinjuredlist = crashImpacts.map(d=>d.MotoristInjured)
      var motoristkilledlist = crashImpacts.map(d=>d.MotoristKilled)



var trace1 = {
	x: boroughlist,
  y: personsinjuredlist,
  name: "Persons Injured",
  marker: {
    color: 'rgba(67,162,202,0.6)'},
  type: "bar",
  };
  
  var trace2 = {
    x: boroughlist,
    y: pedestriansinjuredlist,
    name: "Pedestrians Injured",
    marker: {
      color: 'rgba(123,204,196,0.6)'},
    type: "bar",
    };

  var trace3 = {
    x: boroughlist,
    y: cyclistinjuredlist,
    name: "Cyclists Injured",
    marker: {
      color: 'rgba(173,203,175,0.6)'},
    type: "bar",
  };

  var trace4 = {
    x: boroughlist,
    y: motoristinjuredlist,
    name: "Motorists Injured",
    marker: {
      color: 'rgba(8,104,172,0.6)'},
    type: "bar",
  }
    
  
  var data = [trace1, trace2, trace3, trace4];
  
  var layout = {
    title: "Total Motor Vehicle Crashes NYC April 2020",
    xaxis: { title: "<b>Boroughs</b>"},
    yaxis: { title: "<b># of Persons Killed</b>"},
  };
  
  Plotly.newPlot("plot", data, layout);
})
});