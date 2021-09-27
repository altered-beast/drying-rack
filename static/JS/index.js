//
// function exportJSON(){
//   // optimise this so it just updates parts changed
//   const jsonout = {
//       stat1: parseInt($("#1").val()) ,
//       stat2: parseInt($("#2").val()) ,
//     }
//     const json = JSON.stringify(jsonout);
//     console.log(json)
//
//       let jsonin = JSON.parse(json)
//       console.log(jsonin.stat1)
// };
// function importJSON(file){
//   let input = JSON.parse(file)
//
//   $("#1").val(input.stat1)
//   $("#2").val(input.stat2)
//
// }
//
// $(document).ready(function(){
//   let test = JSON.stringify({ stat1: "1", stat2: "2" })
//   importJSON(test)
//   $(".StatBox").change(function(){
//     exportJSON()
//   });
//
// });
 $(document).ready(function(){

  function importJSON(file){
  let input = JSON.parse(file)

  $("#1").val(input.stat1)
  $("#2").val(input.stat2)
  }

const character = {

  stat1: parseInt($("#1").val()) ,
  stat2: parseInt($("#2").val()) ,

  // secondarystat1:

}
  function exportJSON(){
  const processedJSON = JSON.stringify(character)
  console.log(processedJSON)
  $.ajax("/api", {


    data: processedJSON,
    method: "POST",
    contentType : 'application/json',
    dataType : 'json'


  });

}


  $(".StatBox").change( function(){ exportJSON() })
});
