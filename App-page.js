// ... inside the login form's submit event listener, after successful login:
const userData = {
    username: username, // From your login form
    email: email,       // From your login form
    // ... other user data
};
localStorage.setItem('userData', JSON.stringify(userData));
window.location.href = "user.html"; // Redirect to the user page