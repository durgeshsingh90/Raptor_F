// splunk2json/static/splunk2json/process_data_form.js
document.addEventListener('DOMContentLoaded', function () {
    var form = document.getElementById('data-form');
    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the form from submitting
        var inputData = document.getElementById('input-data').value;
        // Here you can process the input data or perform any other actions
        console.log('Input Data:', inputData);
        // For demonstration purposes, let's just display an alert
        alert('Input Data: ' + inputData);
    });
});
