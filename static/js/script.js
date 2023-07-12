// async function generateJoke(){
//     let topic = document.getElementById("topic-input").value;
//     let url = 'http://127.0.0.1:5000'
//     try{
//         //fetches joke from flask server
//         let response = await fetch(url);
//         let data = await response.json();
//         //updates joke container with new joke
//         document.getElementById('joke-container').innerText = data.joke;
//         document.getElementById('error-container').innerText = '';
//     } catch(error){
//         //displays error
//         document.getElementById('error-container').innerText = 'Something went wrong bruh';
//         document.getElementById('joke-container').innerText = '';
//     }

// }

function test_function() {
    $.ajax({
        type: "POST",
        url: "/generate_joke",
        data: null, //content of the text box
        success: function (response) {
            console.log(response);
        }
    })
}
