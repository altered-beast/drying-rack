
function makejson(){
  const jsonobj = {
      stat1: parseInt($("#1").val()) ,
      stat2: parseInt($("#2").val()) ,
    }
    const json = JSON.stringify(jsonobj);
    console.log(json)
};


$(document).ready(function(){
  $(".StatBox").change(function(){
    console.log("cum")
  });
});
