var commonXAxisOptions = 
{
    type: 'datetime',
    dateTimeLabelFormats: 
    {
        second: '%H:%M:%S'
    }
};

// Fonction générique pour créer un graphique Highcharts
function createChart(renderTo, titleText, yAxisTitle, yAxisMin, yAxisMax) 
{
    return new Highcharts.Chart({
        chart: { renderTo: renderTo },
        title: { text: titleText },
        series: 
        [{
            showInLegend: false,
            data: []
        }],
        plotOptions: 
        {
            line: {
                animation: false,
                dataLabels: { enabled: true }
            },
        },
        xAxis: commonXAxisOptions,
        yAxis: 
        {
            title: { text: yAxisTitle },
            min: yAxisMin,
            max: yAxisMax
        },
        credits: { enabled: false }
    });
}

var chartT = createChart('chart_temperature', 'Temperature', 'Temperature (Celsius)', -10, 40);
var chartH = createChart('chart_humidity', 'Humidite', 'Humidite (%)', 0, 100);
var chartP = createChart('chart_pressure', 'Pressure', 'Pressure (hPa)', 1000, 1020);

setInterval(function () {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() 
    { 
        if (this.status == 200 && this.readyState == 4)
        {
            var text = String(this.responseText).replace("\"", "").replace("[", "").replace("]", "").replace("\n", "").split(",");
            
            var TChart = [];
            var HChart = [];
            var PChart = [];
            
            for (var i = 0 ; i < text.length ; i+=7) 
            {
                var find_time           = text[i + 1].split(":")[1];
                var find_temperature    = text[i + 2].split(":")[1];
                var find_humidite       = text[i + 3].split(":")[1];
                var find_pressure       = text[i + 4].split(":")[1];
                
                TChart.push([find_time * 1000, parseFloat(find_temperature)]);
                HChart.push([find_time * 1000, parseFloat(find_humidite)]);
                PChart.push([find_time * 1000, parseFloat(find_pressure)]);
            }
            
            chartT.series[0].setData(TChart);
            chartH.series[0].setData(HChart);
            chartP.series[0].setData(PChart);
        }
    }
    xmlHttp.open("GET", "http://192.168.1.234:8008/livingroom/get_all", true); // true for asynchronous
    xmlHttp.send();
}, 2000);