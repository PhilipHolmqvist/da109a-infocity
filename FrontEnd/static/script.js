// ******************************
// EXEMPEL LATHUND FÖR JAVASCRIPT
// ******************************

var cityName = ""

function fetchCity() {
    return function () {
        cityName = $("#input").val();

        //alert(cityName + " 1");
        //console.log("Hello");

        $.ajax({
            url: "https://http://localhost:5000/" + cityName, // Vi refererar till vår sida!
            headers: { "Accept": "application/json" }
        }).done(function (response) { // Här ska vi behandla responsen.

            console.log(response.text); // Kolla i konsollen, en json fil ska finnas.

            // Nedan ska vi koppla elementer från html med id och sätta det vi vill presentera i sidan från vår json fil. Johans lab är perfek hjälp till detta :)
            $('#test').text(cityName); //response['city']['name']
            alert(cityName + " 2");

        });
    }
}


$(document).ready(function () {
    $("#search").click(fetchCity());
});