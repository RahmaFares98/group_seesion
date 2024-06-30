function playVideo(element) {
    element.play();
}

function stopVideo(element) {
    element.pause();
}

function validateForm(formName) {
    // Get form elements
    var form = document.forms[formName];
    var first_name = form["first_name"].value;
    var last_name = form["last_name"].value;
    var Email = form["Email"].value;
    var password = form["password"].value;

    // Check if any required field is empty
    if (first_name == "" || last_name == "" || Email == "" || password == "") {
        alert("Please fill out all required fields.");
        return false; // Prevent form submission
    }

    return true;
}
