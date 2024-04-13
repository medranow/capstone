document.addEventListener('DOMContentLoaded', function() {

    // alert a new patient was added
    document.getElementById('newPatient').addEventListener('submit', () => {
        alert('New patient added');
    });

    // See all patients and go back to adding a new patient
    document.querySelector('#seeallpatients').addEventListener('click', () => display_patients());
    document.querySelector('#goBackToNewForm').addEventListener('click', () => goBackForm());
    document.querySelector('#searchbtn').addEventListener('click', (event) => {
        event.preventDefault(); // Prevent default form submission behavior
        search(); // Call the search function
    });
    //Print prescription
    document.querySelector('#printPrescription').addEventListener('click', () => printPage());



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
            link.className = '';
            

            // Create the <li> element
            var patient = document.createElement('li');
            patient.innerHTML = `${element.name} ${element.lastname}`;
            patient.className = 'list-group-item';

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
            document.getElementById('matchsearch').style.display = 'none';


        });
    });
}

function goBackForm() {

        //Clear the list of patients
        var listofpatients = document.querySelector('#listofpatients');
        listofpatients.innerHTML = " ";

      // Hide the list of patients and show the new form
          document.getElementById('seeallpatients').style.display = 'block';
          document.getElementById('goBackToNewForm').style.display = 'none';
          document.getElementById('divnewpatient').style.display = 'block';
          document.getElementById('listofpatients').style.display = 'none';
          document.getElementById('matchsearch').style.display = 'none';

         
}       

async function search() {
    console.log("Function called");

    // Empty the matchsearch element before appending new results
    document.getElementById('matchsearch').innerHTML = '';

    var input = document.getElementById('searchinput').value;
    console.log(`This is the input being passed: ${input}`);

    try {
        // Fetch all patients and display them
        const response = await fetch(`/search/${input}`, {
            method: 'GET',
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            }
        });

        if (!response.ok) {
            throw new Error('Network response was not ok.');
        }

        const data = await response.json();
        var message = data.message;
        var array = data.data;
        console.log(message);
        console.log(array);

        // loop over the array
        array.forEach(element => {
            console.log(element);

            // Create the <a> tag
            var link = document.createElement('a');
            link.href = `file/${element.id}`;
            link.className = 'list-group-item list-group-item-action textCenter';

            // Create the <li> element
            var patient = document.createElement('li');
            patient.innerHTML = `${element.name} ${element.lastname}`;
            patient.className = 'textCenter';

            // Append the <li> to the <a>
            link.appendChild(patient);

            // Append the <a> to the list
            var list = document.getElementById('matchsearch');
            list.appendChild(link);

            // Hide the list of patients and show the new form
            document.getElementById('seeallpatients').style.display = 'none';
            document.getElementById('goBackToNewForm').style.display = 'block';
            document.getElementById('divnewpatient').style.display = 'none';
            document.getElementById('listofpatients').style.display = 'none';
            document.getElementById('matchsearch').style.display = 'block';
            
        });
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}


function printPage() {
    window.print();
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

