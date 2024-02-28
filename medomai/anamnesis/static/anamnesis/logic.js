document.addEventListener('DOMContentLoaded', function() {

    // alert a new patient was added
    document.getElementById('newPatient').addEventListener('submit', () => {
        alert('New patient added');
    });

    // See all patients
    document.querySelector('#seeallpatients').addEventListener('click', () => display_patients());

});

function display_patients() {
    console.log("Get all patients");

    fetch('/patients', {
        method: 'GET',
    })

    .then(response => response.json())
    .then(data => {
        console.log(data)
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
}