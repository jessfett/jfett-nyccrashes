

$(document).ready(function(){
    testObj = new Object();
    testObj.rawData="Raw Data";
    testObj.popData="Crashes Per 100,000 People";
    
  
  
  
    $("#btn1").click(function(){
      $("div").data(testObj);
    });
    $("#btn2").click(function(){
      alert($("div").data("rawData"));
    });
    $("#btn3").click(function(){
      alert($("div").data("popData"));
    }); 
  });





