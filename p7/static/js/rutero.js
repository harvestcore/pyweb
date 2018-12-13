$(document).ready(function() {
    var busqueda = "";
    var ruta = [];

    function rData(name) {
        $.ajax({
            async: false,
            type: "GET",
            url: "/restaurantes/stat/" + name,
            success: function(data) {
                if (data.success) {
                    restData = data.success;

                    html = ''
                    
                    for (var i = 0; i < data.success.data.length; i++) {
                        html += '<tr>' +
                                    '<td>' + data.success.data[i].name + '</td>' +
                                    '<td>' + data.success.data[i].id + '</td>' +
                                    '<td>' +
                                        '<button class="btn btn-success" id="add-ruta" onclick=setIDtoAdd(\'' + data.success.data[i].id + '\')>+</button>' +
                                    '</td>' +
                                '</tr>'
                    }

                    $('#ruterosearchtable').html(html)
                }
            },
            failure: function(jqXHR, textStatus, errorThrown) { 
                console.log(jqXHR)
                console.log(textStatus)
                console.log(errorThrown)
            }
        });
    }

    $('#buscarrutero').click(function() {
        busqueda = $('#entradarutero').val();

        if (busqueda != "") {
            rData(busqueda);
        }
    });

    var idd = 'mapbox.satellite';
    var ruteromap = L.map('ruteromap').setView([40.7484405,-73.9856644], 18);

    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 20,
        id: idd,
        accessToken: 'pk.eyJ1IjoiaGFydmVzdGNvcmUiLCJhIjoiY2pwbDJvMTZ3MDk2eTN4bXJjcXg0cHA5MCJ9.fe2mpIycGvg05DPNyDSDIw'
    }).addTo(ruteromap);

    function getRest(id) {
        var dataxd;
        $.ajax({
            async: false,
            type: "GET",
            url: "/restaurantes/singlerest/" + id,
            success: function(data) {
                if (data.success) {
                    dataxd = {'name': data.success.name, 'id': data.success.id, 'lat': data.success.location.coordinates[1], 'lng': data.success.location.coordinates[0]}
                }
            },
            failure: function(jqXHR, textStatus, errorThrown) { 
                console.log(jqXHR)
                console.log(textStatus)
                console.log(errorThrown)
            }
        });

        return dataxd;
    }

    var rutero = L.Routing.control({
        waypoints: ruta
    });

    function updateruta() {
        var html2 = '';
        for (var i = 0; i < ruta.length; i++) {
            html2 += '<tr>' +
                        '<td>' + (i+1) + '</td>' +
                        '<td>' + ruta[i].name + '</td>' +
                        '<td>' + ruta[i].id + '</td>' +
                        '<td>Lat: ' + ruta[i].lat + ' - Long: ' + ruta[i].lng + '</td>' +
                        '<td>' +
                            '<button class="btn btn-danger" id="remove-ruta" onclick=setIDtoDel(\'' + ruta[i].id + '\')>-</button>' +
                        '</td>' +
                    '</tr>'
        }

        $('#rutaactualxd').html(html2)
    }

    $('#eliminarrutero').click(function() {
        rutero.remove()
        ruta = [];
        updateruta();
    });

    $('#ruterosearchtable').on('click', '#add-ruta', function() {
        var rest = getRest(idtoadd);

        rutero.remove();
        ruta.push(rest);

        rutero = L.Routing.control({
            waypoints: ruta
        }).addTo(ruteromap);

        updateruta();
    });

    $('#rutaactualxd').on('click', '#remove-ruta', function() {
        var ruta2 = ruta;
        ruta = [];

        for (var i = 0; i < ruta2.length; i++) {
            if (ruta2[i].id != idtodel) {
                ruta.push(ruta2[i]);
            }
        }

        rutero.remove();
        rutero = L.Routing.control({
            waypoints: ruta
        }).addTo(ruteromap);

        updateruta();
    });

    $("#entrada-filtro-rutero").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#ruterosearchtable tr").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
});





