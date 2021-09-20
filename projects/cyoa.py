"""Choose Your Own Adventure PJ00."""

__author__ = "730369129"
from random import randint

CAULDRON = "\U0001F375"
DEVIL = "\U0001F608"
CIGARETTE = "\U0001F6AC"
DRAGON = "\U0001F432"
SKULL = "\U00002620"

points: int = 0
player: str = ""


def main() -> None:
    """Program's Main Function."""
    global points
    greet()
    points = int(input("One more thing before you go... How much are you willing to spend? Only use digits. "))
    print("Great, that's quite a lot ... to lose!")
    while points > 0:
        choice: int = int(input("\nHere are your choices: \n1. Deadly Blackjack\n2. Play the slots!\n3. Head to the bar for a drink\n4. Risk it all with Russian Roulette\n5. Leave Death Casino\nWhich do you choose? "))
        if choice == 5:
            print("Oops! Sorry, you can't leave the Death Casino yet!\nIf you REALLY want to leave, Russian Roulette is the game for you!")
            choice = int(input("Pick another choice: "))
        if choice == 1:
            blackjack()
        if choice == 2:
            points = slots()
        if choice == 3:
            bar()
        if choice == 4:
            roulette()
            
        if points > 0:
            print(f"Your current balance is {points}.")
        else:
            print(f"Well {player}, you seem to either be out of money or dead. \nEither way, you now get to go on a boat ride... across the River Styx. \nGoodbye {SKULL}")


def greet() -> None:
    """Welcome message."""
    global player
    print("Welcome to Death Casino!")
    player = input("What is your name? ")
    print(f"Welcome, {player}!\nWe're thrilled to be in control of your life!")
    print("You will make a series of choices within the casino to determine your fate.\nGood luck and godspeed!")


def blackjack() -> int:
    """Play Simple Blackjack."""
    global points
    print(f"Welcome to Death Blackjack, {player}! \n This game is a simple version of Blackjack. Each card has a value between 1 and 10. If you go over 21, you will die.")
    wager = int(input("How much do you want to bet on Blackjack? "))
    total = randint(1, 10)
    print(f"Your first card was {total}.")
    hit: int = 1
    while hit == 1:
        choice = input("Would you like to hit or stay? Answer by typing the word in lowercase. ")
        if choice == "stay":
            hit = 0
        if choice == "hit":
            card = randint(1, 10)
            total = total + card
            print(f"Your next card was {card}. Your new total is {total}.")
            if total > 21:
                hit = 0
    if total > 21:
        print(f"\nMuahahaha! You went over 21. Time to die, {player}. {SKULL}")
        points = 0
    else:
        if total >= randint(0, 21):
            print("\nBummer. You were the closest to 21, so you win.")
            points = points + wager
        else:
            print("\nHA! You lose! We shall take your money now!")
            points = points - wager
    return points


def slots() -> int:
    """Play the Slot Machine."""
    print("Welcome to the slot machines! If all three match, you win your bet, otherwise you lose it.")
    wager: int = int(input("How much do you want to bet on the slot machine? "))
    global points 

    i: int = 0
    slot_outcome: str = ""
    while i < 3:
        slot = randint(1, 5)   
        if i == 0:
            same_symbol: int = slot
        else:
            if slot != same_symbol:
                same_symbol = 0
        if slot == 1:
            slot_outcome = slot_outcome + CAULDRON
        if slot == 2:
            slot_outcome = slot_outcome + DEVIL
        if slot == 3:
            slot_outcome = slot_outcome + CIGARETTE
        if slot == 4:
            slot_outcome = slot_outcome + DRAGON
        if slot == 5:
            slot_outcome = slot_outcome + SKULL
        i = i + 1
        slot_outcome = slot_outcome + "  "
    print("The slot machine has spoken. The result is:")
    print(f"{slot_outcome}")
    if same_symbol == 0:
        print("HAHAHA!!! You lose! We shall take your money now!")
        points = points - wager
        return points
    else:
        print("Darn. You won. I guess you have earned more money.")
        points = points + wager
        return points


def bar() -> int:
    """Get a drink."""
    global points
    global player
    drink: int = int(input("\nGood choice! You definitely need something to take the edge off.\nHere are your choices:\n1. Vodka Martini $25\n2. White Girl Hard Seltzer $45\n3. Busch Lite $4\n4. Bartender's Choice $35\nWhich would you like? "))
    if drink == 1:
        points = points - 25
    if drink == 2:
        points = points - 45
    if drink == 3:
        points = points - 4
    if drink == 4:
        points = points - 35
    print(f"Great choice. We hope you enjoy your drink, {player}!")
    return points


def roulette() -> None:
    """Play Russian Roulette."""
    global player
    global points
    global SKULL
    bullets: int = int(input(f"\nWelcome to Russian Roulette, {player}! We're so excited to have you!\nYou will pick how many bullets you want in your gun. If the gun goes off with the bullet in the barrel, you will die!\nHow many bullets would you like in your gun? "))
    draw: int = randint(1, 6)
    again: int = 1
    while again == 1:
        if draw <= bullets:
            print(f"\n{SKULL} Bummer! You got shot! Time to die, {player}")
            points = 0
            again = 0
        else:
            print("Ah man, you made it through.")
            again = int(input("Would you like to play again? Press 1 for yes, 0 for no. "))


if __name__ == "__main__":
    main()