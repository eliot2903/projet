function changeText() {
    const btn = document.getElementById("btn");
    const textarea = document.querySelector('textarea[name="clé"]');

    // Si le texte est caché → on l'affiche
    if (textarea.style.webkitTextSecurity === "disc") {
        textarea.style.webkitTextSecurity = "none";
        btn.value = "Cacher le mot de passe";
    } 
    // Sinon → on le cache
    else {
        textarea.style.webkitTextSecurity = "disc";
        btn.value = "Afficher le mot de passe";
    }
}
