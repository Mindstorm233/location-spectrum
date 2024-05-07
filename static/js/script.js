let latitude = 0;
let longitude = 0;

function getLocation() {
    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(function (position) {
            latitude = position.coords.latitude;
            longitude = position.coords.longitude;
            document.getElementById("latitude").textContent = "基于此设备的纬度: " + latitude;
            document.getElementById("longitude").textContent = "基于此设备的经度: " + longitude;
            // 自动填充表单中的经纬度输入框
            document.getElementById("latitudeInput").value = latitude;
            document.getElementById("longitudeInput").value = longitude;
        }, function (error) {
            document.getElementById("locationInfo").textContent = "Error: " + error.message;
        });
    } else {
        document.getElementById("locationInfo").textContent = "Geolocation is not supported by your browser.";
    }
}

function sendLocation() {
    // 从输入框读取经纬度，而非全局变量
    const latitude = document.getElementById("latitudeInput").value;
    const longitude = document.getElementById("longitudeInput").value;

    if (!latitude || !longitude) {
        alert("Location not available or not yet retrieved. Please make sure location is enabled and try again.");
        return;
    }
    const data = {
        latitude: latitude,
        longitude: longitude,
        start: document.getElementById("startFrequency").value,
        end: document.getElementById("endFrequency").value
    };
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
