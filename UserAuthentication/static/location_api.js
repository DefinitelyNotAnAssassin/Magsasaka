
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
        var lat = position.coords.latitude;
        var lon = position.coords.longitude;

        if (lat != null && lon != null) {
            console.log('Latitude: ' + lat + ' Longitude: ' + lon);
        } else {
            console.log('Location not found');
        }
        document.getElementById('latitude').value = lat;
        document.getElementById('longitude').value = lon;
    });
} else {
    alert("Please enable location services to register.");
    
}