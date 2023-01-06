// **************************************
// Js för att presentera json i frontend
// **************************************

$(document).ready(function () {

    $("#searchCity").click(function () {

        var cityName = $("#input").val();

        $.ajax({
            url: 'http://localhost:5000/' + cityName, // Vi refererar till vår sida.
            headers: {"Accept": "application/json"}   // Vi vill ha tillbaka json.
          })
          .done(function (data) { // Här ska vi behandla data.

            //alert($('#cityNameForm input[name=id]').val());

            // Get response and present on the html using jquery.

            // INFO
            $('#cityName').text(data['city']['name'] + ", " + data['countryName']);
            $('#cityInfo').text("Population: " + data['city']['population']);
            $("#cityFlag").attr("src", data['flagImgUri']);

            // CURRENCY
            $('#cityCurrency').text("Currency: " + data['currencyCodes']);

            // WEATHER

            // day 1
            $('#chanceOfRain1').text("Chance of rain: " + data['city']['weather']['DayOne']['chanceOfRain'] + " %.");
            $("#icon1").attr("src", data['city']['weather']['DayOne']['icon']);
            $('#tempAvg1').text("Avg temp: " + data['city']['weather']['DayOne']['tempAvg'] + " C.");
            $('#windMax1').text("Wind max: " + data['city']['weather']['DayOne']['windMax'] + " kph.");

            // day 2
            $('#chanceOfRain2').text("Chance of rain: " + data['city']['weather']['DayTwo']['chanceOfRain'] + " %.");
            $("#icon2").attr("src", data['city']['weather']['DayTwo']['icon']);
            $('#tempAvg2').text("Avg temp: " + data['city']['weather']['DayTwo']['tempAvg'] + " C.");
            $('#windMax2').text("Wind max: " + data['city']['weather']['DayTwo']['windMax'] + " kph.");

            // day 3
            $('#chanceOfRain3').text("Chance of rain: " + data['city']['weather']['DayThree']['chanceOfRain'] + " %.");
            $("#icon3").attr("src", data['city']['weather']['DayThree']['icon']);
            $('#tempAvg3').text("Avg temp: " + data['city']['weather']['DayThree']['tempAvg'] + " C.");
            $('#windMax3').text("Wind max: " + data['city']['weather']['DayThree']['windMax'] + " kph.");

            // Lastly, reset the input field.
            $("#input").val(""); 
        });
    });


    /*
    $.ajax({
        url: 'http://localhost:5000',
        headers: {"Accept": "application/json"}
    })
    .done(function (result) { 
    });
    */


});
