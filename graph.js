var lineChartData = [
    {
        label: "prices",
        values: []
    }
];

var chart = $('#lineChart').epoch({
    type: 'time.line',
    data: lineChartData
});

socket = new WebSocket('ws://localhost:8765');
socket.onopen = function() { }
socket.onmessage = function(s) {
    message = JSON.parse(s.data);
    console.log(message);
    plotPoint = [{
        time: message.time,
        y: message.price
    }];

    chart.push(plotPoint);
}