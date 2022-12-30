// ******************************
// EXEMPEL LATHUND FÖR JAVASCRIPT
// ******************************

$(document).ready(function () {

    // Get value on button click and show alert
    $("#ID_Sök_Knapp").click(function () {
        countryName = $("#ID_Textbox_Input").val();

        $.ajax({
            async: true, // ?
            crossDomain: true, // ?
            url: "https://http://localhost:5000/", // Vi refererar till vår sida!
            method: "GET", // Vi vill ha get metod.
            data: {
                // Här ska stå de parameterna som finns i vårt json... 
            },
            headers: { // Behöver vi ens ha headers här??
                "X-RapidAPI-Key": "0ab490636dmsh7da5c2757e98131p159b59jsn6b2e12133ae3",
                "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
            }
        }).done(function (response) { // Här ska vi behandla responsen. 

            console.log(response); // Kolla i konsollen, en json fil ska finnas. 

            
            // Nedan ska vi koppla elementer från html med id och sätta det vi vill presentera i sidan från vår json fil. Johans lab är perfek hjälp till detta :)
            $('#ID_Element_1').text(response['vår_json_fil_sökväg_1']['vår_json_fil_sökväg_2']['vår_json_fil_sökväg_x']);


        });

    });

});