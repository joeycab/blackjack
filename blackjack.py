from random import choice
from os import system

cards = {"A":11, "K":10, "Q":10, "J":10, "10":10, "9":9, "8":8, "7":7, "6":6, "5":5, "4":4, "3":3, "2":2}

######## Deal Cards ########

playerhand = []
dealerhand = []

def dealcard():
    """chooses a card from the deck"""
    card = choice(list(cards))
    return card

#deals the first hand#
for i in range(2):
    playerhand.append(dealcard())
    dealerhand.append(dealcard())

def handtotal(hand):
    """gets value of the sum of cards"""
    values = []
    for i in hand:
        values.append(cards[i])
    if sum(values) == 21 and len(values) == 2:
        return 0
    if sum(values) > 21:
        values = [1 if x == 11 else x for x in values]
    return sum(values)

def comparetotals(playertotal, dealertotal):
    """compares the player and user totals"""
    if playertotal == 0:
        return "You got BlackJack! You win!"
    elif dealertotal == 0:
        return "The dealer got BlackJack. You lose."
    elif playertotal > 21:
        return "You went over 21. You lose."
    elif dealertotal > 21:
        return "The dealer went over 21! You win!"


    elif playertotal > 21 < dealertotal:
        return "You went over 21. You lose."
    elif playertotal == dealertotal:
        return "It's a draw!"
    elif playertotal > dealertotal:
        return "You win!"
    else:
        return "You lose."

gameover = False

while not gameover:
    playertotal = handtotal(playerhand)
    dealertotal = handtotal(dealerhand)

    print(f"Your cards: {playerhand}\nDealer's first card: {dealerhand[0]}")
    if playertotal == 0 or playertotal > 21:
        gameover = True
    else:
        another_card = input("Do you want another card? (Y/N)\n")
        if another_card.lower() == "y":
            playerhand.append(dealcard())
            system("clear")
        else:
            gameover = True
            system("clear")

while 17 > dealertotal != 0:
    dealerhand.append(dealcard())
    dealertotal = handtotal(dealerhand)

comparetotals(playertotal, dealertotal)

if playertotal == 0:
    print(f"Your cards: {playerhand}\nDealer's cards: {dealerhand}\nDealer's total: {dealertotal}")
elif dealertotal == 0:
    print(f"Your cards: {playerhand}\nDealer's cards: {dealerhand}\nYour total: {playertotal}\nDealer's total: 21")
else:
    print(f"Your cards: {playerhand}\nDealer's cards: {dealerhand}\nYour total: {playertotal}\nDealer's total: {dealertotal}")

print(comparetotals(playertotal, dealertotal))
