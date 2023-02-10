const dropList = document.querySelectorAll("form select"),
fromCurrency = document.querySelector(".from select"),
toCurrency = document.querySelector(".to select"),
getButton = document.querySelector("form button");

var previousCurrencyFrom = document.getElementById('currencyfrom').value;
var previousCurrencyTo = document.getElementById('currencyto').value;
var stringresult = "";
var amount = 0;
var result = 0;

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
        amount = document.getElementById('amount').value;
        result = (amount * currentrate);
        stringresult = amount + " " + currFrom + " = " + result + " " + currTo;
        document.querySelector('.exchange-rate').innerHTML = stringresult;
    }

    /*
    Om APIn behöver kallas görs detta, currentrate uppdateras och ny uträkning görs
    */
    if(callAPI){
        getRate();
    }
}

var xhr2 = null;
getXmlHttpRequestObject = function () {
        if (!xhr2) {
            xhr2 = new XMLHttpRequest();
        }
        return xhr2;
};

function dataCallback2() {
    // Check response is ready or not
    if (xhr2.readyState == 4 && xhr2.status == 200) {
        var jsonFile = JSON.parse(xhr2.responseText);
        let rates = jsonFile.rates;
        let currencyCode;
        for (currencyCode in rates) {
            let currency = rates[currencyCode];
            currentrate = parseFloat(currency.rate);
            result = currency.rate_for_amount;
          }
        amount = document.getElementById('amount').value;
        let from = document.getElementById('currencyfrom').value;
        stringresult = amount + " " + from + " = " + result + " " + currencyCode;
        document.querySelector('.exchange-rate').innerHTML = stringresult;
    }
}


function getRate(){
    console.log("Getting rates...");
    
    var currFrom = document.getElementById('currencyfrom').value;
    var currTo = document.getElementById('currencyto').value;
    var amount = document.getElementById('amount').value;
    xhr2 = getXmlHttpRequestObject();
    xhr2.onreadystatechange = dataCallback2;
    xhr2.open("GET", "http://localhost:6969/convert?from=" + currFrom + "&to=" + currTo + "&amount=" + amount, true);
    xhr2.send(null);
}





