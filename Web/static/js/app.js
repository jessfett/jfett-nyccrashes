
// Links from API 
var urlcrashcount = "http://127.0.0.1:5000/crashcount"
var urlinfo = "http://127.0.0.1:5000/crashinfo"
var urlinjuries = "http://127.0.0.1:5000/injuries"


// Load data from hours-of-tv-watched.csv
d3.csv("../ETL/Data/CrashImpacts.csv").then(function(boroughData) {

	console.log(boroughData);
	var personinjured = boroughData.PersonsInjured; 
	console.log(personinjured);
})


