const dropList = document.querySelectorAll("form select"),
fromCurrency = document.querySelector(".from select"),
toCurrency = document.querySelector(".to select"),
getButton = document.querySelector("form button");

var previousCurrencyFrom = document.getElementById('currencyfrom');
var previousCurrencyTo = document.getElementById('currencyto');
var newrate = currentrate;
var stringresult = "";
var amount = 0;
var result = 0;

for (let i = 0; i < dropList.length; i++) {
    for(let currency_code in country_list){
        // Sätter default-case för valutorna.
        let selected = i == 0 ? currency_code == "EUR" ? "selected" : "" : currency_code == originalcurrency ? "selected" : "";
        // Skapar option tag med valutan i listan som värde och id samt lägger till valutan som text
        let optionTag = `<option value="${currency_code}" id="${currency_code}"${selected}>${currency_code}</option>`;
        // Lägger till skapade tags till Frontenden
        dropList[i].insertAdjacentHTML("beforeend", optionTag);
    }
}


//Bytar plats på valutorna om man klickar på ikonen med pilarna
const exchangeIcon = document.querySelector("form .icon");
exchangeIcon.addEventListener("click", ()=>{
    let temp = fromCurrency.value;
    fromCurrency.value = toCurrency.value; 
    toCurrency.value = temp; 
});

//Sköter valuta omvandlaren
function convert(){
    var callAPI = false;
    var currFrom = document.getElementById('currencyfrom').value;
    var currTo = document.getElementById('currencyto').value;

    /*
    kollar om de senaste hämtade valutorna är samma 
    som förra gången man tryckte på knappen. Om någon av valutorna
    skiljer sig åt kommer callAPI sättas till true.
    */
    if(currFrom !== previousCurrencyFrom || currTo !== previousCurrencyTo){
        callAPI = true;
        previousCurrencyFrom = currFrom;
        previousCurrencyTo = currTo;
    }

    //Om apin inte behöver kallas görs bara en uträkning baserat på senaste ratesen.
    if(!callAPI){
        alert("Didn't call API")
        amount = document.getElementById('amount').value;
        result = (amount * currentrate);
        stringresult = amount + " " + currFrom + " = " + result + " " + currTo;
        document.querySelector('.exchange-rate').innerHTML = stringresult;
    }

    /*
    Om APIn behöver kallas görs detta, currentrate uppdateras och ny uträkning görs
    */
    if(callAPI){
        alert("Called API")
        /*
        @todo
        call api with currTo, CurrFrom & amount
        */
        getRate();
        currentrate = 1.0000; //get new rate from response
        result = 0; // get result from the api call
        stringresult = amount + " " + currFrom + " = " + result + " " + currTo;

        //kallar på APIn
    }
}

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
        var jsonFile = JSON.parse(xhr.responseText);
        var result = jsonFile.rates.currencyto.rate_for_amount;
        currentrate = jsonFile.rates.currencyto.rate;
        stringresult = result + " " + currTo;
        document.querySelector('.exchange-rate').innerHTML = stringresult;
    }
}


function getRate(){
    console.log("Getting rates...");
    var currFrom = document.getElementById('currencyfrom').value;
    var currTo = document.getElementById('currencyto').value;
    var amount = document.getElementById('amount').value;
    xhr = getXmlHttpRequestObject();
    xhr.onreadystatechange = dataCallback;
    xhr.open("GET", "http://localhost:6969/convert?from=" + currFrom + "&to=" + currTo + "&amount=" + amount, true);
    xhr.send(null);
}



