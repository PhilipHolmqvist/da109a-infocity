// **************************************
// Js för att presentera json i frontend
// **************************************

var cityName = ""

$(document).ready(function () {

    $("#search").click(function () {

        cityName = $("#input").val();

        $.ajax({
            url: 'http://localhost:5000/' + cityName, // Vi refererar till vår sida.
            headers: {"Accept": "application/json"}   // Vi vill ha tillbaka json.
          })
          .done(function (data) { // Här ska vi behandla data.

            // Get response and present on the html using jquery.

            // INFO
            $('#cityName').text(data['city']['name'] + ", " + data['countryName']);
            $('#cityInfo').text("Population: " + data['city']['population']);
            $("#cityFlag").attr("src", data['flagImgUri']);

            // CURRENCY
            $('#cityCurrency').text("Currency: " + data['currencyCodes']);

            // WEATHER
            $('#cityWeather').text("Avg temp: " + data['city']['weather']['DayOne']['tempAvg'] + " C.");

            
            // Lastly, reset the input field.
            $("#input").val(""); 
        });
    });

});
