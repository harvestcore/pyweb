$(document).ready(function() {
    /**
     * 
     *  Estadísticas restaurantes de comida rápida
     * 
     */
    $(function() {
        var fastFood = ['McDonald\'s', 'Burger King', 'Subway', 'Pizza Hut', 'Wendy\'s', 'KFC', 'Taco Bell', 'Domino\'s Pizza', 'Dunkin Donuts', 'Starbucks', 'Chipotle'];
        var restName = new Array();
        var restAmount = new Array();
        var restData= new Array();

        function rData(name) {
            $.ajax({
                async: false,
                type: "GET",
                url: "/restaurantes/stat/" + name,
                success: function(data) {
                    if (data.success) {
                        restAmount.push(data.success.amount);
                        restName.push(data.success.name);
                        restData.push(data.success);
                    }
                },
                failure: function(jqXHR, textStatus, errorThrown) { 
                    console.log(jqXHR)
                    console.log(textStatus)
                    console.log(errorThrown)
                }
            });
        }
        
        function getRestData() {
            for (var i = 0; i < fastFood.length; i++) {
                rData(fastFood[i]);
            }                  
        }

        $.when( getRestData() ).then( function() {    
            $('#fastFoodTable').highcharts({
                chart: {
                    type: 'bar'
                },
                title: {
                    text: 'Número de establecimientos de comida rápida'
                },
                xAxis: {
                    categories: restName
                },
                yAxis: {
                },
                series: [{
                    name: "Nº establecimientos",
                    data: restAmount
                }],
            });

            var pValue = []

            for (var i = 0; i < restData.length; i++) {
                pValue.push({
                    'name': restData[i].name,
                    'y': restData[i].percentage
                });
            }

            $('#fastFoodPie').highcharts({
                chart: {
                    plotBackgroundColor: null,
                    plotBorderWidth: null,
                    plotShadow: false,
                    type: 'pie'
                },
                title: {
                    text: 'Porcentaje de establecimientos de comida rápida'
                },
                plotOptions: {
                    pie: {
                        allowPointSelect: true,
                        cursor: 'pointer',
                        dataLabels: {
                            enabled: true,
                            format: '{point.percentage:.1f} %',
                        },
                        showInLegend: true
                    }
                },
                series: [{
                    name: 'Porcentaje global',
                    colorByPoint: true,
                    data: pValue
                }]
            });

        });
    });
});
