// ajax stuff that retrives/saves data from/to the backend
$(document).ready(function () {
  function loadjson(id) {
    $.ajax("/api/load", {
      data: id,
      method: "POST",
      contentType: "application/json",
      dataType: "json",
    }).then(function (response) {
      console.log(response);
      let input = JSON.parse(response);
      $("#1").val(input.primarystats[0]);
      $("#2").val(input.primarystats[1]);
    });
  }

  loadjson('{"id":"6165820632433090988877a5"}');

  function saveJSON() {
    // make this send  only parts updated by stripping away undeeded key/vslue pairs
    const character = {
      // make this so you dont have to specify each element by id . either itterate through or do by class
      primarystats: [$("#1").val(), $("#2").val()],
      // secondarystat1:
    };

    const processedJSON = JSON.stringify(character);
    console.log(processedJSON);
    $.ajax("/api/save", {
      data: processedJSON,
      method: "POST",
      contentType: "application/json",
      dataType: "json",
    }).then(function (response) {
      console.log(response);
    });
  }

  $(".InnerStatBox").change(function () {
    saveJSON();
  });
});
let renderContents = [];
ReactDOM.render(element, $("root"));
