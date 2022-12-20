var countryName = "";
var dayLimit = 4;

$(document).ready(function () {

    // Get value on button click and show alert
    $("#search").click(function () {
        countryName = $("#input").val();

        $.ajax({
            async: true,
            crossDomain: true,
            url: "https://weatherapi-com.p.rapidapi.com/forecast.json",
            method: "GET",
            data: {
                q: countryName,
                days: dayLimit
            },
            headers: {
                "X-RapidAPI-Key": "0ab490636dmsh7da5c2757e98131p159b59jsn6b2e12133ae3",
                "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
            }
        }).done(function (response) {

            //console.log(response);
            //['location']['country']

            
            $('#cityAndCountry').text(response['location']['name'] + ", " + response['location']['country']);

            $('#day1').text(response['forecast']['forecastday'][0]['date']);
            $('#temp1').text("Min temp: " + response['forecast']['forecastday'][0]['day']['mintemp_c'] + " C, Max temp: " + response['forecast']['forecastday'][0]['day']['maxtemp_c'] + " C");

            $('#day2').text(response['forecast']['forecastday'][1]['date']);
            $('#temp2').text("Min temp: " + response['forecast']['forecastday'][1]['day']['mintemp_c'] + " C, Max temp: " + response['forecast']['forecastday'][0]['day']['maxtemp_c'] + " C");

            $('#day3').text(response['forecast']['forecastday'][2]['date']);
            $('#temp3').text("Min temp: " + response['forecast']['forecastday'][2]['day']['mintemp_c'] + " C, Max temp: " + response['forecast']['forecastday'][0]['day']['maxtemp_c'] + " C");


        });

    });
    const toggleButton = document.querySelector('.toggle-button');
    const menu = document.querySelector('.menu');

    toggleButton.addEventListener('click', () => {
      menu.classList.toggle('active');
    });


});
