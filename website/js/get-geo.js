// get geolocation
window.onload = navigator.geolocation.getCurrentPosition(success, error);

function success(position) {
    var latitude = position.coords.latitude;
    var longitude = position.coords.longitude;

    // get form data
    var form = document.querySelector("form");
    form.addEventListener("submit", function(event) {
        var data = form.elements.foo.value;

        //setup xhr request
        var XHR = new XMLHttpRequest();

        // urlencode data
        urlEncodedData = encodeURIComponent(data);
	urlEncodedData = urlEncodedData.replace(/%20/g, '+');
        urlEncodedLat = encodeURIComponent(latitude);
        urlEncodedLon = encodeURIComponent(longitude);

	// Create query string
        queryString = '?q=' + urlEncodedData + '&lat=' + urlEncodedLat + '&lon=' + urlEncodedLon; 
    
        var searchUrl = 'http://192.168.1.118:8000/geoFilter' + queryString;

      // We define what will happen if the data are successfully sent
      XHR.addEventListener("load", function(event) {
	document.getElementById("results").innerHTML = "";
	var resultsTemplate = document.getElementById("results-template").innerHTML;
	  var template = Handlebars.compile(resultsTemplate);
	var data = JSON.parse(event.target.responseText);
	if (data.length !== 0) {
        var searchResults = template(data);
	document.getElementById("results").innerHTML += searchResults;
	    } else {
		document.getElementById("results").innerHTML = "<h2>No results Found</h2>";}
    });

    // We define what will happen in case of error
    XHR.addEventListener("error", function(event) {
      alert('Oups! Something goes wrong.');
    });

    XHR.open('GET', searchUrl);
    XHR.send();

    event.preventDefault();});}

  function error() {
      console.log('unable to geolocate');
  }
