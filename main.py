import json
from creditcard import best_card

with open('./cards.json', 'r') as cardObj:
    cards = json.load(cardObj)['cards']

feature_weights = {
    'cashback_amount': 0.1,
    'cashback_percentage': 0.3,
    'discount_amount': 0.1,
    'discount_percentage': 0.2,
    'points_earn': 0.3,
}


def main():
    category = 'miles'
    transaction_amount = 203.75
    selected_card = best_card(cards, category, feature_weights, transaction_amount)
    print(f'Best card: {selected_card}')


if __name__ == "__main__":
    main()
