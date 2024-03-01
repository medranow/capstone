document.addEventListener('DOMContentLoaded', function() {

    // alert a new patient was added
    document.getElementById('newPatient').addEventListener('submit', () => {
        alert('New patient added');
    });

    // See all patients and hide them and go back
    document.querySelector('#seeallpatients').addEventListener('click', () => display_patients());
    document.querySelector('#goBackToNewForm').addEventListener('click', () => goBackForm());
    document.querySelector('#searchbtn').addEventListener('click', () => search());
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

            // Hide the newform and show the list of patients
            document.getElementById('divnewpatient').style.display = 'none';
            document.getElementById('seeallpatients').style.display = 'none';
            document.getElementById('goBackToNewForm').style.display = 'block';
            document.getElementById('listofpatients').style.display = 'block';

        });
    });
}

function goBackForm() {
      // Hide the list of patients and show the new form
          document.getElementById('seeallpatients').style.display = 'block';
          document.getElementById('goBackToNewForm').style.display = 'none';
          document.getElementById('divnewpatient').style.display = 'block';
          document.getElementById('listofpatients').style.display = 'none';
          document.getElementById('matchsearch').style.display = 'none';
}

function search() {
    console.log("Function called");

    var input = document.getElementById('searchinput').value;
    console.log(`This is the input being passed: ${input}`)

    //Fetch all patients and display them
    fetch(`/search/${input}`, {
        method: 'GET',
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    });
    
}