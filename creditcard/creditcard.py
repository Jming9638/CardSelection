def card_score(card_details, feature_weights, transaction_amount):
    score = 0.0
    score += card_details['cashback_amount'] * feature_weights['cashback_amount']
    score += (card_details['cashback_percentage'] * transaction_amount) * feature_weights['cashback_percentage']
    score += card_details['discount_amount'] * feature_weights['discount_amount']
    score += (card_details['discount_percentage'] * transaction_amount) * feature_weights['discount_percentage']
    score += (card_details['points_earn'] * transaction_amount * 0.01) * feature_weights['points_earn']
    return round(score, 4)


def best_card(cards, category, feature_weights, transaction_amount):
    optimal_card = None
    max_score = 0.0
    if sum(feature_weights.values()) == 1.0:
        print('Calculation Results:')
        for card, details in cards.items():
            card_details = details[category]
            score = card_score(card_details, feature_weights, transaction_amount)
            print(f'{card}: {score}')
            if score > max_score:
                max_score = score
                optimal_card = card
    else:
        print('Weights must sum to 1.0')
    return optimal_card
