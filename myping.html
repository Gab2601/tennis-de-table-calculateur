<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculateur de Classement</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            text-align: center;
        }

        header {
            background-color: #2c3e50;
            color: white;
            padding: 10px 20px;
        }

        h1 {
            margin: 0;
        }

        #calculateur-container {
            margin-top: 30px;
            width: 80%;
            margin-left: auto;
            margin-right: auto;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        form input, form button {
            padding: 10px;
            margin: 10px;
            width: 100%;
            font-size: 16px;
        }

        form button {
            background-color: #2c3e50;
            color: white;
            border: none;
            cursor: pointer;
        }

        form button:hover {
            background-color: #34495e;
        }

        #classement-result {
            font-size: 20px;
            margin-top: 20px;
            font-weight: bold;
        }

        footer {
            background-color: #2c3e50;
            color: white;
            text-align: center;
            padding: 10px;
            position: fixed;
            width: 100%;
            bottom: 0;
        }
    </style>
</head>
<body>

    <header>
        <h1>Calculateur de Classement Tennis de Table</h1>
    </header>

    <div id="calculateur-container">
        <h2>Entrez vos points pour connaître votre classement</h2>
        <form id="formulaire-classement">
            <label for="points">Entrez vos points :</label>
            <input type="number" id="points" name="points" required placeholder="Par exemple : 600"><br>

            <button type="submit">Calculer votre classement</button>
        </form>

        <div id="classement-result"></div>
    </div>


    <script>
        // Fonction pour calculer le classement basé sur les points
        function calculerClassement(event) {
            event.preventDefault();  // Empêche le formulaire de se soumettre de manière traditionnelle

            // Récupérer le nombre de points de l'utilisateur
            const points = parseInt(document.getElementById('points').value);
            const classementResultat = document.getElementById('classement-result');

            // Définir les seuils de points et les classements associés
            let classement = '';

            if (points >= 875) {
                classement = 'D2';
            } else if (points >= 750) {
                classement = 'D4';
            } else if (points >= 625) {
                classement = 'D6';
            } else if (points >= 500) {
                classement = 'E0';
            } else if (points >= 375) {
                classement = 'E2';
            } else if (points >= 250) {
                classement = 'E4';
            } else {
                classement = 'Non classé (points insuffisants)';
            }

            // Afficher le résultat du classement
            classementResultat.textContent = `Votre classement estimé est : ${classement}`;
        }

        // Ajouter un écouteur d'événement pour le formulaire
        document.getElementById('formulaire-classement').addEventListener('submit', calculerClassement);
    </script>
    
</body>
</html>
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculateur de Points AFTT</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 0; }
        header { background-color: #2c3e50; color: white; padding: 10px 20px; text-align: center; }
        main { padding: 20px; }
        #statistiques { background-color: white; border: 1px solid #ddd; padding: 20px; margin: 10px 0; }
        form { background-color: white; padding: 20px; border: 1px solid #ddd; width: 300px; margin-top: 20px; }
        form label { display: block; margin-bottom: 5px; }
        form input, form select { width: 100%; padding: 8px; margin-bottom: 10px; }
        form button { background-color: #2c3e50; color: white; padding: 10px 15px; border: none; cursor: pointer; }
        form button:hover { background-color: #34495e; }
        .result-list { list-style: none; padding-left: 0; }
        .result-item { background-color: #f9f9f9; padding: 12px; margin: 5px 0; border-radius: 5px; border: 1px solid #ddd; }
    </style>
</head>
<body>

    <header>
        <h1>Calculateur de Points AFTT Interclub</h1>
    </header>

    <main>
        <section id="statistiques">
            <h2>Résultats des Matchs</h2>
            <ul id="resultsList" class="result-list"></ul>
        </section>

        <section id="formulaire">
            <h2>Calculer mes Points</h2>
            <form id="formulaire-calcul">
                <label for="playerPoints">Ton classement :</label>
                <input type="number" id="playerPoints" name="playerPoints" placeholder="Ton classement" value="434" required><br><br>

                <label for="opponentPoints">Classement de l'adversaire :</label>
                <input type="number" id="opponentPoints" name="opponentPoints" placeholder="Classement de l'adversaire" value="609" required><br><br>

                <label for="victory">Résultat du match :</label>
                <select id="victory" name="victory" required>
                    <option value="DEFEAT">Défaite</option>
                    <option value="VICTORY">Victoire</option>
                </select><br><br>

                <button type="submit">Calculer le Gain/Perte</button>
            </form>

            <button id="clearMatchesBtn">Effacer les matchs</button>
        </section>
    </main>

    <script>
        function calculatePoints(playerPoints, opponentPoints, victory) {
            const diff = Math.abs(opponentPoints - playerPoints);
            let pointsChange = 0;
            let expectedPoints = 0;
            let unexpectedPoints = 0;
            const interclubFactor = 0.85;

            if (diff >= 0 && diff <= 25) {
                expectedPoints = 9;
                unexpectedPoints = 10;
            } else if (diff <= 50) {
                expectedPoints = 8;
                unexpectedPoints = 12;
            } else if (diff <= 75) {
                expectedPoints = 7;
                unexpectedPoints = 14;
            } else if (diff <= 100) {
                expectedPoints = 6;
                unexpectedPoints = 16;
            } else if (diff <= 150) {
                expectedPoints = 5;
                unexpectedPoints = 18;
            } else if (diff <= 200) {
                expectedPoints = 4;
                unexpectedPoints = 20;
            } else if (diff <= 250) {
                expectedPoints = 3;
                unexpectedPoints = 24;
            } else if (diff <= 300) {
                expectedPoints = 2;
                unexpectedPoints = 28;
            } else if (diff <= 400) {
                expectedPoints = 1;
                unexpectedPoints = 32;
            } else if (diff > 400) {
                expectedPoints = 0;
                unexpectedPoints = 40;
            }

            if (victory === 'VICTORY') {
                pointsChange = unexpectedPoints * interclubFactor;
            } else if (victory === 'DEFEAT') {
                pointsChange = expectedPoints * 0.8 * interclubFactor * -1;
            }

            return pointsChange;
        }

        function addMatch(event) {
            event.preventDefault();

            const playerPoints = parseInt(document.getElementById('playerPoints').value);
            const opponentPoints = parseInt(document.getElementById('opponentPoints').value);
            const victory = document.getElementById('victory').value;

            if (!playerPoints || !opponentPoints) {
                alert("Veuillez entrer un classement pour vous et votre adversaire.");
                return;
            }

            const pointsChange = calculatePoints(playerPoints, opponentPoints, victory);
            pointsEntries.push({
                playerPoints,
                opponentPoints,
                victory,
                pointsChange
            });

            displayResults();
        }

        function displayResults() {
            const resultsList = document.getElementById('resultsList');
            resultsList.innerHTML = '';

            pointsEntries.forEach((entry, index) => {
                const li = document.createElement('li');
                li.classList.add('result-item');
                li.innerHTML = `
                    <strong>Match ${index + 1}</strong><br>
                    Ton classement: ${entry.playerPoints}<br>
                    Classement de l'adversaire: ${entry.opponentPoints}<br>
                    Résultat: ${entry.victory === 'VICTORY' ? 'Victoire' : 'Défaite'}<br>
                    Points gagnés/perdus: ${entry.pointsChange.toFixed(2)}
                `;
                resultsList.appendChild(li);
            });
        }

        function clearMatches() {
            pointsEntries = [];
            displayResults();
        }

        let pointsEntries = [];

        document.getElementById('formulaire-calcul').addEventListener('submit', addMatch);
        document.getElementById('clearMatchesBtn').addEventListener('click', clearMatches);
    </script>

</body>
</html>
<!DOCTYPE html>
<html lang="fr">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-LSDD8VH0RC"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-LSDD8VH0RC');
</script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mes Statistiques de Match</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 0; }
        header { background-color: #2c3e50; color: white; padding: 10px 20px; text-align: center; }
        main { padding: 20px; }
        #statistiques { background-color: white; border: 1px solid #ddd; padding: 20px; margin: 10px 0; }
        form { background-color: white; padding: 20px; border: 1px solid #ddd; width: 300px; margin-top: 20px; }
        form label { display: block; margin-bottom: 5px; }
        form input { width: 100%; padding: 8px; margin-bottom: 10px; }
        form button { background-color: #2c3e50; color: white; padding: 10px 15px; border: none; cursor: pointer; }
        form button:hover { background-color: #34495e; }
    </style>
</head>
<body>
    <header>
        <h1>Mon Profil de Joueur</h1>
    </header>

    <main>
        <section id="statistiques">
            <h2>Mes Statistiques</h2>
            <p><strong>Points :</strong> <span id="points">434</span></p>
            <p><strong>Matchs gagnés :</strong> <span id="victoires">4</span></p>
            <p><strong>Matchs perdus :</strong> <span id="defaites">32</span></p>
        </section>

        <section id="formulaire">
            <h2>Mettre à jour mes statistiques</h2>
            <form id="formulaire-statistiques">
                <label for="points-input">Points :</label>
                <input type="number" id="points-input" name="points" value="434" required><br><br>

                <label for="victoires-input">Matchs gagnés :</label>
                <input type="number" id="victoires-input" name="victoires" value="4" required><br><br>

                <label for="defaites-input">Matchs perdus :</label>
                <input type="number" id="defaites-input" name="defaites" value="32" required><br><br>

                <button type="submit">Mettre à jour</button>
            </form>
        </section>
    </main>

    <script>
        function afficherStatistiques() {
            const points = localStorage.getItem('points') || 434;
            const victoires = localStorage.getItem('victoires') || 4;
            const defeates = localStorage.getItem('defaites') || 32;

            document.getElementById('points').textContent = points;
            document.getElementById('victoires').textContent = victoires;
            document.getElementById('defaites').textContent = defeates;
        }

        function mettreAJourStatistiques(event) {
            event.preventDefault();

            const points = document.getElementById('points-input').value;
            const victoires = document.getElementById('victoires-input').value;
            const defeates = document.getElementById('defaites-input').value;

            localStorage.setItem('points', points);
            localStorage.setItem('victoires', victoires);
            localStorage.setItem('defaites', defeates);

            afficherStatistiques();
        }

        document.getElementById('formulaire-statistiques').addEventListener('submit', mettreAJourStatistiques);
        window.onload = afficherStatistiques;
    </script>
</body>
</html>
