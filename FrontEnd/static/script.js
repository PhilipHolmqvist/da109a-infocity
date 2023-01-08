// **************************************
// Js för att presentera json i frontend
// **************************************
var currentrate = 0;
var originalcurrency = "SEK";

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
        document.getElementById('capital').innerHTML = "Capital: " + jsonFile.capital;
        document.getElementById('countryName').innerHTML = jsonFile.countryName;
        document.getElementById('currencyCodes').innerHTML = "Currency: " + jsonFile.currencyCodes;
        document.getElementById('flagImgUri').src = jsonFile.flagImgUri;
        document.getElementById('numRegions').innerHTML = "Num of regions: " + jsonFile.numRegions;
        document.getElementById('tenEuroConversion').innerHTML = "EUR to SEK: " + jsonFile.tenEuroConversion;

        document.getElementById('city-elevationMeters').innerHTML = "M.a.s.l: " + jsonFile.city.elevationMeters;
        document.getElementById('city-name').innerHTML = jsonFile.city.name;
        document.getElementById('city-population').innerHTML = "Population: " + jsonFile.city.population;
        document.getElementById('city-region').innerHTML = jsonFile.city.region;

        document.getElementById('city-weather-DayOne-chanceOfRain').innerHTML = "Rain chance: " + jsonFile.city.weather.DayOne.chanceOfRain;
        document.getElementById('city-weather-DayOne-icon').src = jsonFile.city.weather.DayOne.icon;
        document.getElementById('city-weather-DayOne-tempAvg').innerHTML = "Avg temp: " + jsonFile.city.weather.DayOne.tempAvg;
        document.getElementById('city-weather-DayOne-windMax').innerHTML = "Wind: " + jsonFile.city.weather.DayOne.windMax;

        document.getElementById('city-weather-DayTwo-chanceOfRain').innerHTML = "Rain chance: " + jsonFile.city.weather.DayTwo.chanceOfRain;
        document.getElementById('city-weather-DayTwo-icon').src = jsonFile.city.weather.DayTwo.icon;
        document.getElementById('city-weather-DayTwo-tempAvg').innerHTML = "Avg temp: " + jsonFile.city.weather.DayTwo.tempAvg;
        document.getElementById('city-weather-DayTwo-windMax').innerHTML = "Wind: " + jsonFile.city.weather.DayTwo.windMax;

        document.getElementById('city-weather-DayThree-chanceOfRain').innerHTML = "Rain chance: " + jsonFile.city.weather.DayThree.chanceOfRain;
        document.getElementById('city-weather-DayThree-icon').src = jsonFile.city.weather.DayThree.icon;
        document.getElementById('city-weather-DayThree-tempAvg').innerHTML = "Avg temp: " + jsonFile.city.weather.DayThree.tempAvg;
        document.getElementById('city-weather-DayThree-windMax').innerHTML = "Wind: " + jsonFile.city.weather.DayThree.windMax;

        $("#input").val(''); // reset the text field at the end.
        $('#loadWait').hide();
        
        originalcurrency = jsonFile.currencyCodes;
        currentrate = jsonFile.currentRate;
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
    resetContent();
    getCity();
}

function resetContent() {
    document.getElementById('callingCode').innerHTML = "";
    document.getElementById('capital').innerHTML = "";
    document.getElementById('countryName').innerHTML = "";
    document.getElementById('currencyCodes').innerHTML = "";
    document.getElementById('flagImgUri').src = "";
    document.getElementById('numRegions').innerHTML = "";
    document.getElementById('tenEuroConversion').innerHTML = "";

    document.getElementById('city-elevationMeters').innerHTML = "";
    document.getElementById('city-name').innerHTML = "";
    document.getElementById('city-population').innerHTML = "";
    document.getElementById('city-region').innerHTML = "";

    document.getElementById('city-weather-DayOne-chanceOfRain').innerHTML = "";
    document.getElementById('city-weather-DayOne-icon').src = "";
    document.getElementById('city-weather-DayOne-tempAvg').innerHTML = "";
    document.getElementById('city-weather-DayOne-windMax').innerHTML = "";

    document.getElementById('city-weather-DayTwo-chanceOfRain').innerHTML = "";
    document.getElementById('city-weather-DayTwo-icon').src = "";
    document.getElementById('city-weather-DayTwo-tempAvg').innerHTML = "";
    document.getElementById('city-weather-DayTwo-windMax').innerHTML = "";

    document.getElementById('city-weather-DayThree-chanceOfRain').innerHTML = "";
    document.getElementById('city-weather-DayThree-icon').src = "";
    document.getElementById('city-weather-DayThree-tempAvg').innerHTML = "";
    document.getElementById('city-weather-DayThree-windMax').innerHTML = "";
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