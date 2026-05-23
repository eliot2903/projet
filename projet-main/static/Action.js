

const menuBtn = document.getElementById("menu-btn");
const menu = document.getElementById("menu");
const closeBtn = document.getElementById("close-btn");

menuBtn.addEventListener("click", () => {
    menu.style.display = "flex";
});

closeBtn.addEventListener("click", () => {
    menu.style.display = "none";
});