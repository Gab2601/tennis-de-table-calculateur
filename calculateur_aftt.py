def calculate_points(player_points, opponent_points, victory):
    """
    Calcule les points gagnés ou perdus selon le classement et le résultat du match.
    """
    diff = abs(opponent_points - player_points)
    interclub_factor = 0.85

    if diff <= 25:
        expected_points, unexpected_points = 9, 10
    elif diff <= 50:
        expected_points, unexpected_points = 8, 12
    elif diff <= 75:
        expected_points, unexpected_points = 7, 14
    elif diff <= 100:
        expected_points, unexpected_points = 6, 16
    elif diff <= 150:
        expected_points, unexpected_points = 5, 18
    elif diff <= 200:
        expected_points, unexpected_points = 4, 20
    elif diff <= 250:
        expected_points, unexpected_points = 3, 24
    elif diff <= 300:
        expected_points, unexpected_points = 2, 28
    elif diff <= 400:
        expected_points, unexpected_points = 1, 32
    else:
        expected_points, unexpected_points = 0, 40

    if victory == 'VICTORY':
        return unexpected_points * interclub_factor
    elif victory == 'DEFEAT':
        return expected_points * 0.8 * interclub_factor * -1
    else:
        return None

def main():
    """
    Interface en ligne de commande pour entrer les données du match.
    """
    print("\n🔵 Calculateur de Points AFTT 🔵\n")

    try:
        player_points = int(input("🏓 Ton classement : "))
        opponent_points = int(input("🏓 Classement de l'adversaire : "))
        victory = input("🎯 Résultat du match (VICTORY/DEFEAT) : ").strip().upper()

        points_change = calculate_points(player_points, opponent_points, victory)

        if points_change is None:
            print("\n⚠️ Erreur : entre 'VICTORY' ou 'DEFEAT'.")
            return

        print(f"\n✅ Points gagnés/perdus : {points_change:.2f} points\n")
    
    except ValueError:
        print("\n⚠️ Erreur : Veuillez entrer des nombres valides pour les classements.")

if __name__ == "__main__":
    main()

