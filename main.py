import playsound
import random
import time

def winner_sound():
    """Sound Play when you win the Game"""
    winner_sound_list = ["Winner1.mp3", "Winner2.mp3"]
    sound_winner = random.choice(winner_sound_list)
    playsound.playsound(sound_winner)

def loser_sound():
    """ Sound Play when you lose the Game """
    loser_sound_list = ["Loser1.mp3", "Loser2.mp3"]
    sound_loser = random.choice(loser_sound_list)
    playsound.playsound(sound_loser)

def hit_sound():
    """Sound Play when you Hit the Pack"""
    sound_hit = "Hit.mp3"
    playsound.playsound(sound_hit)

def stand_sound():
    """Sound Play when you Stand"""
    sound_stand = "Stand.mp3"
    playsound.playsound(sound_stand)

def bet_chips_check(a, b):
    """Check the amount of chips you enter is correct or not"""
    if a>b:
        print(f"You Bet {b} Chips left chips are {a-b}.")
        return False
    elif a<b:
        print("Sorry! You don't have enough chips!")
        return True
    else:
        print("Sorry! Please provide correct Input!")
        return True


def suits():
    """Return any one Suit"""
    suits_list = ["Club", "Diamond", "Heart", "Spade"]
    suit_selected = random.choice(suits_list)
    return suit_selected

def cards():
    """Return any one Card"""
    cards_list = [(1, "A"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6"), (7, "7"), (8, "8"), (9, "9"), (10, "10"),
                  (10, "J"), (10, "Q"), (10, "K")]
    card_selected = random.choice(cards_list)
    return card_selected


def hit_pack():
    """Return Card after Hitting the Pack"""
    s = suits()
    c = cards()
    hit_card = []
    hit_card.append(s)
    hit_card.append(c)
    return hit_card

def human_hit(hc, hs):
    """Player Card"""
    human_card_hit = hit_pack()
    hc.append(human_card_hit[0])
    hc.append(human_card_hit[1][1])
    hs = hs + human_card_hit[1][0]
    return hc, hs

def computer_hit(cc, cs):
    """Player Card"""
    computer_card_hit = hit_pack()
    cc.append(computer_card_hit[0])
    cc.append(computer_card_hit[1][1])
    cs = cs + computer_card_hit[1][0]
    return cc, cs

def start_game(q, hc, hs, cc, cs):
    """Starting Game"""

    time.sleep(2)
    while not q:
        """First Card given to Player"""
        hc, hs = human_hit(hc, hs)
        print(f"Your Card's: {hc}")

        """First Card given to Computer"""
        cc, cs = computer_hit(cc, cs)

        l = True
        while l:

            human_next_card = input("Press:\n\tH: Hit\n\tP: Pass\n\tS: Show ").lower()
            computer_next_card_list = ["h", "p"]
            computer_next_card = random.choice(computer_next_card_list)
            if human_next_card == "s":
                q = True
                l = False
            elif human_next_card == "p":
                print(f"Your Card's: {hc}")
                if computer_next_card == "p":
                    pass
                else:
                    cc, cs = computer_hit(cc, cs)
            elif human_next_card == "h":
                hc, hs = human_hit(hc, hs)
                print(f"Your Card's: {hc}")
                if computer_next_card == "p":
                    pass
                else:
                    cc, cs = computer_hit(cc, cs)
            else:
                print("Sorry! You provide incorrect input!")

    return hc, hs, cc, cs



print("##############################################################################################################")
print("\n\t\t\t\t\t\tWelcome to the Card Game\n\t@\tRule's:\n*\tYou have to Bet the chips!"
      "\n*\tTo take the new card you have to Hit the Pack!\n*\tIf you don't want to take the card you can just Pass!"
      "\n*\tYour card Score total must be Equal to or less then 21 !\n*\tThe closer score to 21 will win the game!"
      "\n*\tYou can call Show to finish the game and see who win's!\n*\tComputer can Hit or Pass only!\n\n\t\t**\tYou have to press:\n\t\t\t-\tH: Hit"
      "\n\t\t\t-\tP: Pass\n\t\t\t-\tS: Show")

card_score_list = [(1, "A"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6"), (7, "7"), (8, "8"), (9, "9"), (10, "10"),
                  (10, "J"), (10, "Q"), (10, "K")]
print("\n*\tList of Score of the Card!")
for item in card_score_list:
    print(item)

print("\n\n")
betting_chips = 10000
a = False
while not a:
    x = input("Do you want to Continue?\n*\tY: Yes\n*\tN: No\nPress Y/N :___").lower()
    if x=="n":
        print("Thanks for Playing!")
        a = True
    elif x=="y":
        """Starting Game"""
        print("Starting Game")

        print(f"You have {betting_chips} chips!")
        betting_chips_amount = int(input("Enter the amount of chips you want to bet:"))
        bet = bet_chips_check(betting_chips, betting_chips_amount)
        human_score = 0             # Score of the player
        human_cards = []            # Cards of the player
        computer_score = 0          # Score of the Computer
        computer_cards = []         # Cards of the Computer
        human_cards, human_score, computer_cards, computer_score = start_game(bet, human_cards, human_score, computer_cards, computer_score)
        if human_score > 21:
            betting_chips -=betting_chips_amount
            print(f"Your card's {human_cards}\nYour Score: {human_score}"
                  f"\nAs your score is more then 21.\n*\t*\t*\tYou Lose!\t*\t*\t*"
                  f"Betting Chips = {betting_chips}")
            loser_sound()
        elif human_score < 21 and computer_score > 21:
            betting_chips +=betting_chips_amount
            print(f"Your card's {human_cards}\nYour Score: {human_score}"
                  f"\nComputer card's {computer_cards}\nComputer Score: {computer_score}"
                  f"\n*\t*\t*\tYou Win!\t*\t*\t*\nBetting Chips = {betting_chips}")
            winner_sound()
        elif human_score < 21 and computer_score < 21 and human_score > computer_score:
            betting_chips += betting_chips_amount
            print(f"Your card's {human_cards}\nYour Score: {human_score}"
                  f"\nComputer card's {computer_cards}\nComputer Score: {computer_score}"
                  f"\n*\t*\t*\tYou Win!\t*\t*\t*\nBetting Chips = {betting_chips}")
            winner_sound()
        elif human_score == 21:
            betting_chips += betting_chips_amount
            print(f"Your card's {human_cards}\nYour Score: {human_score}"
                  f"\nComputer card's {computer_cards}\nComputer Score: {computer_score}"
                  f"\n*\t*\t*\tYou Win!\t*\t*\t*\nBetting Chips = {betting_chips}")
            winner_sound()
        else:
            betting_chips -= betting_chips_amount
            print(f"Your card's {human_cards}\nYour Score: {human_score}"
                  f"\nComputer card's {computer_cards}\nComputer Score: {computer_score}"
                  f"\n*\t*\t*\tYou Lose!\t*\t*\t*\nBetting Chips = {betting_chips}")
            loser_sound()

    else:
        print("Sorry! You provide incorrect input!")