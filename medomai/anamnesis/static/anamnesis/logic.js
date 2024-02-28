document.addEventListener('DOMContentLoaded', function() {

    // alert a new patient was added
    document.getElementById('newPatient').addEventListener('submit', () => {
        alert('New patient added');
    });

    // See all patients
    document.querySelector('#seeallpatients').addEventListener('click', () => display_patients());

});

function display_patients() {
    console.log("Function called");

    //Fetch all patients and display them
    fetch('/patients', {
        method: 'GET',
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        data = data["data"];
        data.forEach(element => {
            console.log(`This is patient ${element.name}`)

            // Create the <a> tag
            var link = document.createElement('a');
            link.href = `file/${element.id}`; // Set the href attribute as needed
            link.className = 'list-group-item list-group-item-action';
            

            // Create the <li> element
            var patient = document.createElement('li');
            patient.innerHTML = `${element.name} ${element.lastname}`;

            // Append the <li> to the <a>
            link.appendChild(patient);

            // Append the <a> to the list
            var list = document.getElementById('listofpatients');
            list.appendChild(link);


        });
    });
}