document.getElementById('generate-joke').addEventListener('click', function() {
    fetch('http://127.0.0.1:5000') 
        .then(response => response.json())
        .then(data => document.getElementById('joke').textContent = data.joke)
        .catch(error => console.error('Error:', error));
});
