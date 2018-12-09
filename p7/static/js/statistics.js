$(document).ready(function() {
    /**
     * 
     *  Estadísticas 
     * 
     */
    $(function() {
        var fastFood = new Array('McDonald\'s', 'Burger King', 'Subway', 'Pizza Hut', 'Wendy\'s', 'KFC', 'Taco Bell', 'Domino\'s Pizza', 'Dunkin Donuts', 'Starbucks', 'Chipotle');
        var restData = new Array();

        function getRestData(rest) {
            // console.log("http://localhost:8080/restaurantes/stat/" + rest)
            $.ajax({
                type: "GET",
                url: "http://localhost:8080/restaurantes/stat/" + rest,
                success: function(data) {
                    if (data.success) {
                        console.log(data.success.amount + " - " + data.success.name)
                        restData.push({
                            'name': data.success.name,
                            'amount': data.success.amount
                        })
                    }
                },
                failure: function(jqXHR, textStatus, errorThrown) { 
                    console.log(jqXHR)
                    console.log(textStatus)
                    console.log(errorThrown)
                }
            });
        }
        
        for (var i = 0; i < fastFood.length; i++) {
            getRestData(fastFood[i])
        }

        console.log(restData[2])
        console.log(fastFood)

        $('#fastFoodStat').highcharts({
            chart: {
                type: 'bar'
              },
            title: {
              text: 'Establecimientos de comida rápida'
            },
            xAxis: {
              categories: fastFood
            },
            yAxis: {
            },
            series: [{
                name: "Nº establecimientos",
              data: restData
            }],
        });
    });
});