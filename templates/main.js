document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('upload-button').addEventListener('click', function(e) {
        e.preventDefault();
        var formData = new FormData(document.getElementById('upload-form'));
        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.text())
        .then(data => alert(data))
        .catch(error => alert(error));
    });

    document.getElementById('ask-button').addEventListener('click', function(e) {
        e.preventDefault();
        var questionData = { question: document.querySelector('input[name="question"]').value };
        fetch('/ask', {
            method: 'POST',
            body: JSON.stringify(questionData),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('response').innerHTML = data.response;
        })
        .catch(error => alert(error));
    });
});
