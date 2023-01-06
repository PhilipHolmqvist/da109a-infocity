const dropList = document.querySelectorAll("form select"),
fromCurrency = document.querySelector(".from select"),
toCurrency = document.querySelector(".to select"),
getButton = document.querySelector("form button");

var previousCurrencyFrom = document.getElementById('currencyfrom');
var previousCurrencyTo = document.getElementById('currencyto');
var currentrate = 0.0931;


for (let i = 0; i < dropList.length; i++) {
    for(let currency_code in country_list){
        // Sätter default-case för valutorna.
        let selected = i == 0 ? currency_code == "EUR" ? "selected" : "" : currency_code == "SEK" ? "selected" : "";
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
/*
@todo
- Hämta rate från JSON objektet som kommer
- Kalla på APIn på egen hand om någon av valutorna skulle ändras 
*/
function convert(){
    //initierar callAPI-bool för kontroll om apin ska kallas eller inte
    var callAPI = false;
    //hämtar nuvarande valutor valda i selectboxarna
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
        var amount = document.getElementById('amount').value;
        var rate = 0.0931;
        var result = (amount * rate);
        var stringresult = amount + " " + fromCurrency.value + " = " + result + " " + toCurrency.value;
        document.querySelector('.exchange-rate').innerHTML = stringresult;
    }

    /*
    Om APIn behöver kallas görs detta, currentrate uppdateras och ny uträkning görs
    */
    if(callAPI){
        alert("Called API")
        //kallar på APIn
    }
}