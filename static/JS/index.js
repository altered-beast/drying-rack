$(document).ready(function () {
  function loadjson(id) {
    $.ajax("/load", {
      data: id,
      method: "GET",
      contentType: "text/html",
      dataType: "text",
    }).then(function (response) {
      console.log(response);
      let input = JSON.parse(response);
      $("#1").val(input.stat1);
      $("#2").val(input.stat2);
    });
  }

  loadjson("234");

  // let input = JSON.parse(file)
  //
  // $("#1").val(input.stat1)
  // $("#2").val(input.stat2)
  //
  function exportJSON() {
    // make this send  only parts updated by stripping away undeeded key/vslue pairs
    console.log($("#1").val);
    const character = {
      // make this so you dont have to specify each element by id . either itterate through or do by class
      primarystats: [$("#1").val(), $("#2").val()],
      // secondarystat1:
    };

    const processedJSON = JSON.stringify(character);
    console.log(processedJSON);
    $.ajax("/api", {
      data: processedJSON,
      method: "POST",
      contentType: "application/json",
      dataType: "json",
    }).then(function (response) {
      console.log(response);
    });
  }

  $(".InnerStatBox").change(function () {
    exportJSON();
  });
});
