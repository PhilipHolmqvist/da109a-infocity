// **************************************
// Js för att presentera json i frontend
// **************************************

var xhr = null;
getXmlHttpRequestObject = function () {
    if (!xhr) {
        // Create a new XMLHttpRequest object 
        xhr = new XMLHttpRequest();
    }
    return xhr;
};

function dataCallback() {
    // Check response is ready or not
    if (xhr.readyState == 4 && xhr.status == 200) {
        console.log("Data received!");
        //getDate();

        var jsonFile = JSON.parse(xhr.responseText);
        
        document.getElementById('callingCode').innerHTML = "Landskod: " + jsonFile.callingCode;
        document.getElementById('capital').innerHTML = "Huvudstad: " + jsonFile.capital;
        document.getElementById('countryName').innerHTML = jsonFile.countryName;
        document.getElementById('currencyCodes').innerHTML = "Valuta: " + jsonFile.currencyCodes;
        document.getElementById('flagImgUri').src = jsonFile.flagImgUri;
        document.getElementById('numRegions').innerHTML = "Antal regioner: " + jsonFile.numRegions;
        document.getElementById('tenEuroConversion').innerHTML = "Eur to sek: " + jsonFile.tenEuroConversion;

        document.getElementById('city-elevationMeters').innerHTML = "M.Ö.H: " + jsonFile.city.elevationMeters;
        document.getElementById('city-name').innerHTML = jsonFile.city.name;
        document.getElementById('city-population').innerHTML = "Invånare: " + jsonFile.city.population;
        document.getElementById('city-region').innerHTML = jsonFile.city.region;

        document.getElementById('city-weather-DayOne-chanceOfRain').innerHTML = "Regn Risk: " + jsonFile.city.weather.DayOne.chanceOfRain;
        document.getElementById('city-weather-DayOne-icon').src = jsonFile.city.weather.DayOne.icon;
        document.getElementById('city-weather-DayOne-tempAvg').innerHTML = "Temp: " + jsonFile.city.weather.DayOne.tempAvg;
        document.getElementById('city-weather-DayOne-windMax').innerHTML = "Vind: " + jsonFile.city.weather.DayOne.windMax;

        document.getElementById('city-weather-DayTwo-chanceOfRain').innerHTML = "Regn Risk: " + jsonFile.city.weather.DayTwo.chanceOfRain;
        document.getElementById('city-weather-DayTwo-icon').src = jsonFile.city.weather.DayTwo.icon;
        document.getElementById('city-weather-DayTwo-tempAvg').innerHTML = "Temp: " + jsonFile.city.weather.DayTwo.tempAvg;
        document.getElementById('city-weather-DayTwo-windMax').innerHTML = "Vind: " + jsonFile.city.weather.DayTwo.windMax;

        document.getElementById('city-weather-DayThree-chanceOfRain').innerHTML = "Regn Risk: " + jsonFile.city.weather.DayThree.chanceOfRain;
        document.getElementById('city-weather-DayThree-icon').src = jsonFile.city.weather.DayThree.icon;
        document.getElementById('city-weather-DayThree-tempAvg').innerHTML = "Temp: " + jsonFile.city.weather.DayThree.tempAvg;
        document.getElementById('city-weather-DayThree-windMax').innerHTML = "Vind: " + jsonFile.city.weather.DayThree.windMax;

        $("#input").val(''); // reset the text field at the end.
        $('#loadWait').hide();

        //dataDiv = document.getElementById('titel');
        //dataDiv.innerHTML = jsonFile.city.name;

    }
}

function getCity() {
    $('#loadWait').show();
    console.log("Get city...");
    cityName = $("#input").val();
    xhr = getXmlHttpRequestObject();
    xhr.onreadystatechange = dataCallback;
    // asynchronous requests
    xhr.open("GET", "http://localhost:6969/" + cityName, true);
    // Send the request over the network
    xhr.send(null);
}

function hideResultShowIntro() {
    $("#result-page").hide();
    $("#intro-page").show();
    $("#input").val('');
}

function hideIntroShowResult() {
    $("#intro-page").hide();
    $("#result-page").show();
    getCity();
}

$(document).ready(function () {
    hideResultShowIntro();
    $('#loadWait').hide();
    $("#listTopCities").css("line-height", "50");
    //document.getElementById('input').addEventListener('keypress', (e) => {
    //   e.preventDefault();
    //});
});



function getDate() {
    date = new Date().toString();
    document.getElementById('dateTime').textContent
        = date;
}
(function () {
    getDate();
})();