$(document).ready(function() {
    // Animación menú lateral
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });

    // Aumentar tamaño barras porcentajes
    // Se cambia el atributo "width" del css
    $("#bt1").click(function() {
        newsize = $(".habprog").width() * 1.1;
        if (newsize < 1227)
            $(".habprog").css("width", newsize);
    });

    // Disminuir tamaño barras porcentajes
    // Se cambia el atributo "width" del css
    $("#bt2").click(function() {
        newsize = $(".habprog").width() / 1.1;
        if (newsize > 200)
            $(".habprog").css("width", newsize);
    });

    // Cambiar estilo de tabla
    // Se añaden y quitan clases
    $("#changetable").click(function() {
        if ($("#estilotabla").hasClass('table-dark') || $("#tablarestaurantes").hasClass('table-dark')) {
            $("#estilotabla").removeClass('table-dark');
            $("#tablarestaurantes").removeClass('table-dark');
        }
        else {
            $("#estilotabla").addClass('table-dark');
            $("#tablarestaurantes").addClass('table-dark');
        }
    });
    
    // Panel con la información de contacto
    // Se activa/desactiva con un deslizado lento
    $("#botoncontacto").click(function(){
        $("#panelcontacto").slideToggle("slow");
    });

    // Filtro rápido en las tablas
    $("#entradaFiltroRest").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#estilotabla tr").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });

        $("#tablarestaurantes tr").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });

    // Paginador jQuery
    //
    // Cargo todos los datos de la tabla y hasta que no se selecciona un valor
    // en el selector no se activa la paginación.
    //
    // Divide las entradas en el número de páginas necesario según el número de
    // entradas que queramos paginar.
    //
    $('#selectorpaginadorrest').on('change', function() {
        var table = '#tablarestaurantes'

        var trnum = 0;
        var maxrows = parseInt($(this).val());
        var totalrows = $(table + ' tbody tr').length;
        
        // Primera página
        $(table + ' tr:gt(0)').each(function() {
            trnum++;
            if (trnum > maxrows)
                $(this).hide();
            else
                $(this).show();
        });
        
        // Si hay varias páginas agrego un deslizador y el número de la página
        if (totalrows > maxrows) {
            var pagenum = Math.ceil(totalrows / maxrows);

            // Si existiera el deslizador y el número de página se eliminan
            $('.slidecontainer input').remove()
            $('.slidecontainer p').remove()

            // Si el deslizador/nº pag no existe se crea
            if ( !$('.slidecontainer input').length && !$('.slidecontainer p').length) {
                $('.slidecontainer').append('<input type="range" min="1" max="' + pagenum + '" value="1" class="slider" id="pageSlider">').show()
                $('.slidecontainer').append('<p class="pagevalue">Página: <span id="sliderValue">1</span> / ' + pagenum + '</p>').show()
            }
        }
    });

    // Cada vez que se cambia el deslizador muestra la página a la que corresponde y cambia el valor de la página
    $('#paginadorRest').on('change', '#pageSlider', function() {
        var slider = document.getElementById('pageSlider');
        var output = document.getElementById('sliderValue');
        var selectorpaginador = document.getElementById('selectorpaginadorrest');
        var maxrows = selectorpaginador.value;
        var pagenum = slider.value;
        var trindex = 0;
        
        $('#tablarestaurantes tr:gt(0)').each(function() {
            trindex++;
            if (trindex > (maxrows * pagenum) || trindex <= ((maxrows * pagenum) - maxrows))
                $(this).hide();
            else
                $(this).show();
        });

        // Valor página
        output.innerHTML = slider.value;
        slider.oninput = function() {
            output.innerHTML = this.value;
        }
    });

    // Agrega columna con el número de elemento
    $(function() {
        $('#tablarestaurantes table tr:eq(0)').prepend('<th>Nº</th>');
        var id = 0;
        $('#tablarestaurantes table tr:gt(0)').each(function() {
            id++;
            $(this).prepend('<td>' + id + '</td>')
        });
    });


    // Paginador JQuery + AJAX
    $(function() {
        var page = 0, pagelimit = 10, totalelements = 0;

        // Muestro datos por defecto (una página de 10 elementos)
        showData();

        // Selector de número de elementos por página
        // Por defecto es 10
        $('#selectorpaginadorrest').on('change', function() {
            if (parseInt($(this).val()) == 0)
                pagelimit = totalelements;
            else
                pagelimit = parseInt($(this).val())

            showData();
        });


        // Boton prev
        $('#prev-btn').on('click', function() {
            if (page > 0) {
                page--;
                showData();
            }
        });

        // Botón next
        $('#next-btn').on('click', function() {
            if (page * pagelimit < totalelements) {
                page++;
                showData();
            }
        });

        // Ir a número de página
        $("#entradaNumPag").on("keyup", function() {
            if (parseInt($(this).val()) > 0) {
                page = parseInt($(this).val()) - 1;
                showData();
            } else {
                page = 0;
                showData();
            }
        });
        
        
        // Función para mostrar los datos
        function showData (datos) {
            $.ajax({
                url: "/restaurantes/intervalodatos/" + (page*pagelimit) + "/" + pagelimit + "/" + String(restname),
                type: "GET",
                success: function(data) {
                    if (data.success) {
                        var dataArray = data.success.data;
                        var html = "";
                        
                        totalelements = data.success.totalelements;
                        html = ''
                    
                        for (var i = 0; i < dataArray.length; i++) {
                            html += '<tr>' +
                                        '<td>' + dataArray[i].name + '</td>' +
                                        '<td>' + dataArray[i].id + '</td>' +
                                        '<td>[' + dataArray[i].location.coordinates[1] + ', ' + dataArray[i].location.coordinates[0] + ']</td>' +
                                        '<td>' + dataArray[i].location.type + '</td>' +
                                    '</tr>'
                        }
                        
                        $('#restFetchedContent').html(html)
                    }
                },
                failure: function(jqXHR, textStatus, errorThrown) { 
                    console.log(jqXHR)
                    console.log(textStatus)
                    console.log(errorThrown)
                }
            });
        }
    });
});