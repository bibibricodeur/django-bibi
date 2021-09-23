// https://learn.jquery.com/using-jquery-core/document-ready/

// A $( document ).ready() block.
$( document ).ready(function() {
  console.log( "django-bibi ready!" );
  $('.sidenav').sidenav();
  //$(".dropdown-trigger").dropdown();
});

function fetchLiens() {
  // https://developer.mozilla.org/fr/docs/Web/API/Fetch_API/Using_Fetch
  if(self.fetch) {
    // exécuter ma requête fetch ici
    var requete = ('/static/datas/liens.json');
    fetch(requete).then(function(response) {
      var contentType = response.headers.get("content-type");
      if(contentType && contentType.indexOf("application/json") !== -1) {
        return response.json().then(function(liens) {
          // traitement du JSON
          console.log(liens);
          // https://developer.mozilla.org/fr/docs/Web/API/Body/json
          liensWidget = [];
          for (lien in liens) {
            //console.log(liens[lien].name)          
            //console.log(liens[lien].url)
            liensWidget += '<a href=' + liens[lien].url + ' class="collection-item">' + liens[lien].name + '</a>';
            document.getElementById('widgetLiens').innerHTML = liensWidget;
          }
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

fetchLiens();

function fetchCitations() {
  // https://developer.mozilla.org/fr/docs/Web/API/Fetch_API/Using_Fetch
  if(self.fetch) {
    // exécuter ma requête fetch ici
    var requete = ('/static/datas/citations.json');
    fetch(requete).then(function(response) {
      var contentType = response.headers.get("content-type");
      if(contentType && contentType.indexOf("application/json") !== -1) {
        return response.json().then(function(citations) {
          // traitement du JSON
          console.log(citations);
          // https://developer.mozilla.org/fr/docs/Web/API/Body/json
          citationsWidget = [];
          for (citation in citations) {
            //console.log(citations[citation].citation)
            //console.log(citations[citation].name)                    
            //console.log(citations[citation].url)
            citationsWidget += '<p class="grey-text text-lighten-4">"' + citations[citation].citation + '" <a class="orange-text text-dark-3" href="' + citations[citation].url + '">' + citations[citation].name + '</a></p>';
            document.getElementById('widgeCitations').innerHTML = citationsWidget;
          }
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

fetchCitations();

// Fin
