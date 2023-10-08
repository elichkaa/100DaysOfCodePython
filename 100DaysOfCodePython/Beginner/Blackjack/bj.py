import messages
import art
import cards
import random

ACE = 'A'
ACE_VALUE = 11
SEPARATOR = ', '
BJ_SCORE = 21
ENOUGH_FOR_DEALER = 17


def get_card():
    return random.choice(list(cards.cards.keys()))


def get_player_score(dealt_cards):
    score = 0
    for card in dealt_cards:
        if card != ACE:
            score += cards.cards[card]
        else:
            if score + ACE_VALUE > BJ_SCORE:
                score += cards.cards[card]
            else:
                score += ACE_VALUE
    return score


def get_dealer_score(dealt_cards):
    score = 0
    for card in dealt_cards:
        if card == ACE and ENOUGH_FOR_DEALER < score + ACE_VALUE <= BJ_SCORE:
            score += ACE_VALUE
        else:
            score += cards.cards[card]
    return score


if __name__ == '__main__':
    play = input(messages.prompt)
    while play == messages.play:
        print(art.logo)
        my_cards = [get_card(), get_card()]
        print(messages.cards + SEPARATOR.join(my_cards))
        dealers_cards = [get_card(), get_card()]
        print(messages.dealer + str(dealers_cards[0]))
        move = input(messages.move)
        player_score = get_player_score(my_cards)
        dealers_score = get_dealer_score(dealers_cards)
        if move == messages.play:
            my_cards.append(get_card())
            player_score = get_player_score(my_cards)
        else:
            while dealers_score < ENOUGH_FOR_DEALER:
                dealers_cards.append(get_card())
                dealers_score = get_dealer_score(dealers_cards)
        print(messages.player_final + SEPARATOR.join(my_cards))
        print(messages.dealer_final + SEPARATOR.join(dealers_cards))
        if player_score == BJ_SCORE:
            print(messages.bj)
        if player_score == dealers_score:
            print(messages.draw)
        elif player_score > BJ_SCORE:
            print(messages.bust)
        elif player_score > dealers_score or dealers_score > BJ_SCORE:
            print(messages.win)
        else:
            print(messages.lose)
        play = input(messages.prompt)
