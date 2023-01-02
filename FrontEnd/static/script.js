// ******************************
// EXEMPEL LATHUND FÖR JAVASCRIPT
// ******************************

function fetchCity() {
    return function() {

        cityname = $("#input").val();

      $.ajax({
        url: "http://127.0.0.1:5000/" + cityname, // Vi refererar till vår sida!
        headers: {"Accept": "application/json"}
      })
      .done(function (data) {
        alert("hej")
        $('#titel-info').text(data['name']);
        });
    }
  }
        


$(document).ready(function () {

    $("#search").click(fetchCity());
    
 
});
    // Get value on button click and show alert
    

$("#search").click(function () {
    countryName = $("#input").val();
    alert("Search was pressed with text: " + countryName)
    console.log("hej")

    $.ajax({
        url: "http://127.0.0.1:5000", // Vi refererar till vår sida!
        method: "GET", // Vi vill ha get metod.
        headers: {"Accept": "application/json"}

    }).done(function (response) { // Här ska vi behandla responsen. 

        console.log(response['city']['name']); // Kolla i konsollen, en json fil ska finnas. 

        
        // Nedan ska vi koppla elementer från html med id och sätta det vi vill presentera i sidan från vår json fil. Johans lab är perfek hjälp till detta :)
        $('#ID_Element_1').text(response['vår_json_fil_sökväg_1']['vår_json_fil_sökväg_2']['vår_json_fil_sökväg_x']);


    });

});
