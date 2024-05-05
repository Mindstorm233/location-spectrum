let latitude = 0;
let longitude = 0;

function getLocation() {
    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(function (position) {
            latitude = position.coords.latitude;
            longitude = position.coords.longitude;
            document.getElementById("latitude").textContent = "Latitude: " + latitude;
            document.getElementById("longitude").textContent = "Longitude: " + longitude;
        }, function (error) {
            document.getElementById("locationInfo").textContent = "Error: " + error.message;
        });
    } else {
        document.getElementById("locationInfo").textContent = "Geolocation is not supported by your browser.";
    }
}

function sendLocation() {
    if (latitude === 0 && longitude === 0) {
        alert("Location not available or not yet retrieved. Please make sure location is enabled and try again.");
        return;
    }
    const data = { latitude: latitude, longitude: longitude, start: document.getElementById("startFrequency").value, end: document.getElementById("endFrequency").value };
    fetch('http://127.0.0.1:5000/location', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
        .then(response => response.text())
        .then(result => alert('Return: ' + result))
        .catch(error => alert('Error sending location: ' + error));
}
