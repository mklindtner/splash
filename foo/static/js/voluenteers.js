var signUpForm = document.getElementById("tab-2");
var voluenteerForm = document.getElementById("tab-1");
var elements = document.getElementsByClassName('participants');
signUpForm.onclick = () => {    
    for(i = 0; i < elements.length; i++) {
        elements[i].style.display = "none";
    }
};
voluenteerForm.onclick = () => {
    for(i = 0; i < elements.length; i++) {
        elements[i].style.display = "block";
    }
}
