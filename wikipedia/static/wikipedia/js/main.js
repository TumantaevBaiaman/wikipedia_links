const form = document.querySelector('form');

form.addEventListener('submit', function() {
    const spinner = document.querySelector('#spinner');
    spinner.style.display = 'block';
    const button_post = document.querySelector('#button_post');
    button_post.style.display = 'none';
});

const spinner = document.querySelector('#spinner');
spinner.style.display = 'none';

const button_post = document.querySelector('#button_post');
button_post.style.display = 'block';


function submitForm() {
    var myButton = document.getElementById("myButton");
    var spinner = document.getElementById("spinner");

    myButton.style.display = "none";
    spinner.style.display = "block";


    myButton.style.display = "block";
    spinner.style.display = "none";
}