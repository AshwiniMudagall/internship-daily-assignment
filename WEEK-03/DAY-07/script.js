
const signupForm = document.getElementById("signupForm");
const signupMsg = document.getElementById("message");

if(signupForm) {
    signupForm.addEventListener("submit", function(e){
        e.preventDefault(); 
        signupMsg.textContent = "You have successfully registered!";
        signupForm.reset();
    });
}

// Login form
const loginForm = document.getElementById("loginForm");
const loginMsg = document.getElementById("loginMessage");

if(loginForm) {
    loginForm.addEventListener("submit", function(e){
        e.preventDefault(); 
        loginMsg.textContent = "You have successfully logged in!";
        loginForm.reset();
    });
}