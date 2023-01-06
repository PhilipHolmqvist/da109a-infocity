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
        document.getElementById('tenEuroConversion').innerHTML = jsonFile.tenEuroConversion;
        document.getElementById('wikidataID').innerHTML = jsonFile.wikidataID;

        document.getElementById('city-elevationMeters').innerHTML = "M.Ö.H: " + jsonFile.city.elevationMeters;
        document.getElementById('city-name').innerHTML = jsonFile.city.name;
        document.getElementById('city-population').innerHTML = "Invånare: " + jsonFile.city.population;
        document.getElementById('city-region').innerHTML = jsonFile.city.region;
        document.getElementById('city-wikidataID').innerHTML = jsonFile.city.wikidataID;

        document.getElementById('city-weather-DayOne-chanceOfRain').innerHTML = jsonFile.city.weather.DayOne.chanceOfRain;
        document.getElementById('city-weather-DayOne-icon').innerHTML = jsonFile.city.weather.DayOne.icon;
        document.getElementById('city-weather-DayOne-tempAvg').innerHTML = jsonFile.city.weather.DayOne.tempAvg;
        document.getElementById('city-weather-DayOne-windMax').innerHTML = jsonFile.city.weather.DayOne.windMax;
        
        document.getElementById('city-weather-DayTwo-chanceOfRain').innerHTML = jsonFile.city.weather.DayTwo.chanceOfRain;
        document.getElementById('city-weather-DayTwo-icon').innerHTML = jsonFile.city.weather.DayTwo.icon;
        document.getElementById('city-weather-DayTwo-tempAvg').innerHTML = jsonFile.city.weather.DayTwo.tempAvg;
        document.getElementById('city-weather-DayTwo-windMax').innerHTML = jsonFile.city.weather.DayTwo.windMax;

        document.getElementById('city-weather-DayThree-chanceOfRain').innerHTML = jsonFile.city.weather.DayThree.chanceOfRain;
        document.getElementById('city-weather-DayThree-icon').innerHTML = jsonFile.city.weather.DayThree.icon;
        document.getElementById('city-weather-DayThree-tempAvg').innerHTML = jsonFile.city.weather.DayThree.tempAvg;
        document.getElementById('city-weather-DayThree-windMax').innerHTML = jsonFile.city.weather.DayThree.windMax;

        //dataDiv = document.getElementById('titel');
        //dataDiv.innerHTML = jsonFile.city.name;

    }
}

function getCity() {
    console.log("Get city...");
    cityName = $("#input").val();
    xhr = getXmlHttpRequestObject();
    xhr.onreadystatechange = dataCallback;
    // asynchronous requests
    xhr.open("GET", "http://localhost:6969/" + cityName, true);
    // Send the request over the network
    xhr.send(null);
}

function getDate() {
    date = new Date().toString();
    document.getElementById('dateTime').textContent
        = date;
}
(function () {
    getDate();
})();