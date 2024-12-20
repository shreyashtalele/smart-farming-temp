const data = {
    nitrogen: 12.5,
    phosphorus: 8.3,
    potassium: 10.2,
    temperature: 25.0,
    humidity: 60.0,
    ph: 7.0,
    rainfall: 120.0
};

const url = 'http://localhost:8000/predict-crop/';

fetch(url, {
    method: 'POST', // HTTP method
    headers: {
        'Content-Type': 'application/json', 
    },
    body: JSON.stringify(data), 
})
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();     })
    .then(responseData => {
        console.log('Response:', responseData);     })
    .catch(error => {
        console.error('Error:', error);
    });