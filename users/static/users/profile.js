$(document).ready(function(){
  $("#flip").click(function(){
    $("#panel").show(3000);
  });
   $("#flip").click(function(){
    $("#showbutton").show(3000);
  });
  $("#showbutton").click(function(){
    $("#panel").hide(3000);
  });
   $("#showbutton").click(function(){
    $("#showbutton").hide(3000);
  });

});