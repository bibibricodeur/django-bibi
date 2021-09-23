/***
Description:
Dependances:
Copyright (c) 20200222, bibi.
License: WTFPL
***/

// https://playground.deaxon.com/js/vanilla-js/
document.addEventListener("DOMContentLoaded", function() {
  // code
  console.log('bibiweather js en marche :-)');

  function fetchMeteo() {
    // https://developer.mozilla.org/fr/docs/Web/API/Fetch_API/Using_Fetch
    if(self.fetch) {
      // exécuter ma requête fetch ici
      // https://www.prevision-meteo.ch/services/json/matha
      var idville = 'matha';
      var requete = ('https://www.prevision-meteo.ch/services/json/' + idville + '');
      fetch(requete).then(function(response) {
        var contentType = response.headers.get("content-type");
        if(contentType && contentType.indexOf("application/json") !== -1) {
          return response.json().then(function(data) {
            // traitement du JSON
            console.log('requete = ' + requete);
            console.log(data);
            // https://developer.mozilla.org/fr/docs/Web/API/Body/json
            patelin = data.city_info.name;
            description = data.current_condition.condition;
            heure = data.current_condition.hour;
            humidite = data.current_condition.humidity;
            pression = data.current_condition.pressure;
            temperature = data.current_condition.tmp;
            // https://developer.mozilla.org/fr/docs/Web/API/Document/querySelector
            document.querySelector('#patelin').innerHTML = 'Météo: <strong>' + patelin + '</strong>';
            document.querySelector('#description').innerHTML = 'Description: <strong>' + description + '</strong>';
            document.querySelector('#heure').innerHTML = 'Heure: <strong>' + heure + '</strong>';
            document.querySelector('#humidite').innerHTML = 'Humidité: <strong>' + humidite + ' %</strong>';
            document.querySelector('#pression').innerHTML = 'Pression: <strong>' + pression + ' hPa</strong>';
            document.querySelector('#temperature').innerHTML = 'Temperature: <strong>' + temperature + ' °C</strong>';
          });
        } else {
          console.log("Oops, nous n'avons pas du JSON!");
        }
      })
      .catch(function(error) {
        console.log('Il y a eu un problème avec l\'opération fetch: ' + error.message);
      });
    } else {
      // Faire quelque chose avec XMLHttpRequest?
      console.log('Faire quelque chose avec XMLHttpRequest?');
    }
  }

  fetchMeteo();
});
