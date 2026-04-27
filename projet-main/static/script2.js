const mots = [
        "Hello",
        "Bonjour",
        "NSI",
        "Ordinateur",
        "Code",
        "Javascript",
        "Cyber",
        "Secret",
        "Hacker",
        "Internet",
        "Openai",
        "Python",
        "Cryptographie",
        "Reseau",
        "Serveur"
    ];

    let motActuel = "";

    function texteVersHex(texte) {
        return texte
            .split("")
            .map(c => c.charCodeAt(0).toString(16))
            .join("");
    }

    function nouveauMot() {
        motActuel = mots[Math.floor(Math.random() * mots.length)];
        let hex = texteVersHex(motActuel);

        document.getElementById("message").innerText = hex;
        document.getElementById("rep").value = "";
        document.getElementById("resultat").innerHTML = "";
    }

    function verifier() {
        let rep = document.getElementById("rep").value.trim().toLowerCase();
        let correct = motActuel.toLowerCase();
        let res = document.getElementById("resultat");

        if (rep === correct) {
            res.innerHTML = "✅ Probablement";
            res.style.color = "#00ffcc";
            setTimeout(nouveauMot, 1000);
        } else {
            res.innerHTML = "❌ Non";
            res.style.color = "red";
        }
    }

    window.onload = nouveauMot;