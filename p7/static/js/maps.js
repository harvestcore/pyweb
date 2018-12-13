$(document).ready(function() {

    var lat = latitud.replace(/,/g, '.')
    var long = longitud.replace(/,/g, '.')
    var idd = 'mapbox.satellite';
    
    $(function() {
        var editmap = L.map('editmap').setView([lat, long], 20);

        L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
            attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
            maxZoom: 20,
            id: idd,
            accessToken: 'pk.eyJ1IjoiaGFydmVzdGNvcmUiLCJhIjoiY2pwbDJvMTZ3MDk2eTN4bXJjcXg0cHA5MCJ9.fe2mpIycGvg05DPNyDSDIw'
        }).addTo(editmap);
        
        var marker = L.marker([lat, long]).addTo(editmap).bindPopup("<b>" + restname + "</b>").openPopup();
    });


    /**
     * Rutero
     
     $(function() {
        var ruteromap = L.map('ruteromap').setView([57.74, 11.94], 20);
        console.log("aaaaaaaaaaaaaaaaaaaaa")
        
        L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
            attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
            maxZoom: 20,
            id: idd,
            accessToken: 'pk.eyJ1IjoiaGFydmVzdGNvcmUiLCJhIjoiY2pwbDJvMTZ3MDk2eTN4bXJjcXg0cHA5MCJ9.fe2mpIycGvg05DPNyDSDIw'
        }).addTo(ruteromap);
        
        var marker = L.marker([57.74, 11.94]).addTo(ruteromap).bindPopup("<b>" + restname + "</b>").openPopup();
        
        L.Routing.control({
            waypoints: [
                L.latLng(57.74, 11.94),
                L.latLng(57.6792, 11.949)
            ]
        }).addTo(ruteromap);
    });
    */
});
    
    
    
    
    
