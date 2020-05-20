<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <style>
    .highcharts-figure, .highcharts-data-table table {
      min-width: 600px;
      max-width: 1080px;
      margin: 1em auto;
    }
    .highcharts-data-table table {
      font-family: Verdana, sans-serif;
      border-collapse: collapse;
      border: 1px solid #EBEBEB;
      margin: 10px auto;
      text-align: center;
      width: 100%;
      max-width: 500px;
    }
    .highcharts-data-table caption {
      padding: 1em 0;
      font-size: 1.2em;
      color: #555;
    }
    .highcharts-data-table th {
      font-weight: 600;
      padding: 0.5em;
    }
    .highcharts-data-table td, .highcharts-data-table th, .highcharts-data-table caption {
      padding: 0.5em;
    }
    .highcharts-data-table thead tr, .highcharts-data-table tr:nth-child(even) {
      background: #f8f8f8;
    }
    .highcharts-data-table tr:hover {
      background: #f1f7ff;
    }
    </style>

    <script src="https://code.highcharts.com/highcharts.js"></script>
    <script src="https://code.highcharts.com/modules/series-label.js"></script>
    <script src="https://code.highcharts.com/modules/exporting.js"></script>
    <script src="https://code.highcharts.com/modules/export-data.js"></script>
    <script src="https://code.highcharts.com/modules/accessibility.js"></script>
    <script src="https://code.jquery.com/jquery-3.5.0.js"></script>
  </head>
  <body>
    <figure class="highcharts-figure">
      <div id="container"></div>
      <p class="highcharts-description">
      </p>
    </figure>
    <script>
      Highcharts.chart('container', {
        title: {
          text: {{! locname }}
        },

        yAxis: {
          title: {
            text: '单价'
          }
        },

        xAxis: {
          type: 'datetime'
        },

        plotOptions: {
          series: {
            pointStart: Date.UTC(2020, 05, 15),
            pointInterval: 24 * 3600 * 1000 // one day
          }
        },

        legend: {
          layout: 'vertical',
          align: 'right',
          verticalAlign: 'middle'
        },

        series: {{! pricesData }} ,
        responsive: {
          rules: [{
            condition: {
              maxWidth: 500
            },
            chartOptions: {
              legend: {
                layout: 'horizontal',
                align: 'center',
                verticalAlign: 'bottom'
              }
            }
          }]
        }

      });
    </script>
  </body>



</html>
