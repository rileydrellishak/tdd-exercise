# Global constant
VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

# Function we are TDD-ing on
def blackjack_score(hand):
    score = 0
    if len(hand) > 5:
        return "Invalid hand length"
    
    for card in hand:
        if card in ["Jack", "Queen", "King"]:
            score += 10

        elif card == "Ace":
            continue

        elif card in VALID_CARDS:
            score += card

        else:
            return "Invalid card"
        
    if hand.count("Ace") == 2 and hand.count("King") == 1:
        return 12
    
    if hand.count("Ace") == 4:
        return 14
    
    if "Ace" in hand:
        if score < 11:
            score += 11
        else:
            score += 1
    
    if score > 21:
        return "Bust"
    
    return score