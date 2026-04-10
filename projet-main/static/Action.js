// function changeText() {
    // const btn = document.getElementById("btn");
    // const textarea = document.querySelector('textarea[name="clé"]');

    // Si le texte est caché → on l'affiche
    // if (textarea.style.webkitTextSecurity === "disc") {
        // textarea.style.webkitTextSecurity = "none";
        // btn.value = "Cacher le mot de passe";
    // } 
    // Sinon → on le cache
    // else {
        // textarea.style.webkitTextSecurity = "disc";
        // btn.value = "Afficher le mot de passe";
    // }
// }

// const toggle = document.getElementById("toggle");

// toggle.addEventListener("click", () => {
    // toggle.classList.toggle("active");
// });

const menuBtn = document.getElementById("menu-btn");
const menu = document.getElementById("menu");
const closeBtn = document.getElementById("close-btn");

menuBtn.addEventListener("click", () => {
    menu.style.display = "flex";
});

closeBtn.addEventListener("click", () => {
    menu.style.display = "none";
});
