"""Choose Your Own Adventure PJ00"""

__author__ = "730369129"
from random import randint

CAULDRON="\U0001F375"
DEVIL="\U0001F608"
CIGARETTE="\U0001F6AC"
DRAGON="\U0001F432"
SKULL="\U00002620"

points: int = 0
player: str = ""

def main() -> None:
    global points
    greet()
    while points > 0:
        choice: int = int(input(f"\nHere are your choices: \n1. Deadly Blackjack\n2. Play the slots!\n3. Head to the bar for a drink\n4. Risk it all with Russian Roulette\n5. Leave Death Casino\nWhich do you choose? "))
        if choice == 5:
            print("Oops! Sorry, you can't leave the Death Casino yet!\nIf you REALLY want to leave, Russian Roulette is the game for you!")
            choice = int(input("Pick another choice: "))
        if choice == 1:
            blackjack()
        if choice == 2:
            points = slots(points)
        if choice == 3:
            bar()
        if choice == 4:
            roulette()

        if points>0:
            print(f"Your current balance is {points}.")
        else:
            print(f"Well {player}, you seem to either be out of money or dead. \nEither way, you now get to go on a boat ride... across the River Styx. \nGoodbye {SKULL}")



def greet() -> None:
    global player
    player = input("Welcome to Death Casino!\nWhat is your name? ")
    print(f"Welcome, {player}!\nWe're thrilled to be in control of your life!")
    print(f"You will make a series of choices within the casino to determine your fate.\nGood luck and godspeed!")
    global points
    points = int(input("One more thing before you go... What is your net worth? Only use digits. "))
    print("Great, that's quite a lot ... to lose!")

def blackjack() -> None:
    global points
    print(f"Welcome to Death Blackjack, {player}! \n This game is a simple version of Blackjack. Each card has a value between 1 and 10. If you go over 21, you will die.")
    wager = int(input("How much do you want to bet on Blackjack? "))
    total=randint(1,10)
    print(f"Your first card was {total}.")
    hit=True
    while hit==True:
        choice=input("Would you like to hit or stay? Answer by typing the word in lowercase. ")
        if choice=="stay":
            hit=False
        if choice=="hit":
            card=randint(1,10)
            total=total+card
            print(f"Your next card was {card}. Your new total is {total}.")
            if total>21:
                hit=False
    if total>21:
        print(f"Muahahaha! You went over 21. Time to die {player}. {SKULL}")
        points=0
    else:
        if total>=randint(0,21):
            print("Bummer. You were the closest to 21, so you win.")
            points = points + wager
        else:
            print("HA! You lose! We shall take your money now!")
            points = points - wager




def slots(points) -> int:
    print("Welcome to the slot machines! If all three match, you win your bet, otherwise you lose it. ")
    wager = int(input("How much do you want to bet on the slot machine? "))

    i: int =0
    slot_outcome: str = ""
    while i < 3:
        slot = randint(1,5)   
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
    print("The slot machine has spoken.  The result is:")
    print(f"{slot_outcome}")
    if same_symbol == 0:
        print("HAHAHA!!! You lose! We shall take your money now!")
        return points - wager 
    else:
        print("Darn.  You won. I guess you have earned more money.")
        return points + wager    

def bar() -> None:
    pass
def roulette() -> None:
    pass
#ask them how many bullets they want in the gun 0-6
#using that, draw a random number (0,6) if draw <= number of bullets, got shot!
#if you're shot, you die (use {SKULL} here), and points == 0
#Do you want to keep playing? or play something different? (if still alive)

if __name__ == "__main__":
    main()