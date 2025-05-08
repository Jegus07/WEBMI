// Fonction pour afficher un message de bienvenue sur la page d'accueil
document.addEventListener("DOMContentLoaded", function () {
    const welcome = document.querySelector("#welcome-message");
    if (welcome) {
        welcome.style.opacity = 0;
        setTimeout(() => {
            welcome.style.transition = "opacity 1s ease-in-out";
            welcome.style.opacity = 1;
        }, 500);
    }
});

// Exemple de comportement interactif pour le bouton "Se connecter"
const loginBtn = document.querySelector(".login-btn");
if (loginBtn) {
    loginBtn.addEventListener("mouseover", () => {
        loginBtn.style.backgroundColor = "#004080";
    });

    loginBtn.addEventListener("mouseout", () => {
        loginBtn.style.backgroundColor = "#007BFF";
    });
}
