import random, sys
from time import sleep
from colors import *

# player's sum amount which can be bet
money = 5000
# create card characters
HEARTS   = chr(9829)
DIAMONDS = chr(9830)
SPADES   = chr(9824)
CLUBS    = chr(9827)

CARDS    = [HEARTS, DIAMONDS, SPADES, CLUBS]
BACKSIDE = 'backside'

def adorn():
    print("=" * 70)
    print("\t\t= B L A C K = J A C K = G A M E =")
    print("=" * 70)
    
def get_bet(max_bet):
    """ ask the player how much they want to bet this round.""" 
    while True:
        print("\t >>> How much do you want to bet? \n\t    (1-{}, or QUIT)".format(max_bet))
        print("\t  --> Your bet: ", end="")
        bet = input().upper().strip()
        print("\n")
        if bet == "QUIT":
            print("\t\t Thanks for playing!")
            sys.exit()
        
        if not bet.isdecimal():
            continue # if the player didn't enter a number, ask again
        
        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet # player has entered a valid bet


def get_deck():
    """ returns a list of (rank, suit) tuples for all 52 cards """
    global CARDS
    deck = []
    for suit in CARDS:
        for rank in range(2, 11):
            deck.append((str(rank), suit)) # add the numbered card
        for rank in ("J", "Q", "K", "A"):
            deck.append((rank, suit)) # add the face and ace cards
    random.shuffle(deck)
    return deck


def display_hands(player_hand, dealer_hand, show_dealer_hand):
    """ Displays the player's and dealer's cards.
        Hide the dealer's first card if show_dealer variable is False."""
    print("\n")
    if show_dealer_hand:
        print("\t :::: DEALER: ", get_hand_vals(dealer_hand))
        display_cards(dealer_hand)
    else:
        print("\t :::: DEALER: ???")
        # hide the dealer's first card
        display_cards([BACKSIDE] + dealer_hand[1:])
    
    # show the player's cards
    print("\t ::::: PLAYER: ", get_hand_vals(player_hand))
    display_cards(player_hand)


def get_hand_vals(cards):
    """ Returns the value of the cards. Face cards are with 10, aces are
    worth 11 or 1 (this function picks the most suitable ace value). """
    value = 0
    num_of_aces = 0
    # add the value for the non-ace cards
    for card in cards:
        rank = card[0]  # card is a tuple like (rank, suit)
        if rank == "A":
            num_of_aces += 1
        elif rank in ("K", "Q", "J"): # face cards are worth 10 points
            value += 10
        else:
            value += int(rank)  # numbered cards are woth their own number
    # add the values for the aces
    value += num_of_aces # add per ace
    for x in range(num_of_aces):
        # if another 10 can be added with busting, do so
        if value + 10 <= 21:
            value += 10
    return value


def display_cards(cards):
    rows = ["", "", "", "", ""] # the text to display on each row
    for i, card in enumerate(cards):
        if card == BACKSIDE:
            # print a card's back
            rows[0] += purple+"\t ____"+e  # print the top line of the card
            rows[1] += purple+"\t|### | "+e
            rows[2] += purple+"\t|####| "+e
            rows[3] += purple+"\t|_###| "+e
        else:
            # print the card's front
            rank, suit = card # the card is a tuple data structure
            rows[0] += green+"\t ____"+e  # print the top line of the card
            rows[1] += green+"\t|{}  | ".format(rank.ljust(2))+e
            rows[2] += green+"\t| {}  | ".format(suit)+e
            rows[3] += green+"\t|__{}| ".format(rank.rjust(2, "_"))+e
    # print each row on the screen
    for row in rows:
        print(row)
        
        
def get_move(player_hand, money):
    """ Asks the player for their move, and returns 'H' for hit, 'S'
    for stand, and 'D' for double down. """
    while True: # keep looping until the player enters a correct move
        # determine what moves the player can make:
        moves = ["(H)it", "(S)tand"]
        # the player can double down on their first move, which we can
        # tell because they will have exactly two cards:
        if len(player_hand) == 2 and money > 0:
            moves.append("(D)ouble down")
        
        # get the player's move:
        move_prompt = ", ".join(moves) + "> "
        move = input(move_prompt).upper()
        if move in ("H", "S"):
            return move # player has entered a valid move
        if move == "D" and "(D)ouble down" in moves:
            return move # player has entered a valid move

def handle_dealer(player_hand, dealer_hand, bet, deck):
    global money
    #handle the dealer's actions
    if get_hand_vals(player_hand) <= 21:
        while get_hand_vals(dealer_hand) < 17:
            # the dealer hits
            print('\t  Dealer hits now...')
            dealer_hand.append(deck.pop())
            display_hands(player_hand, dealer_hand, False)
                
            if get_hand_vals(dealer_hand) > 21:
                break # the dealer has busted
            input('\t\t Press'+green+' ENTER '+e+'to continue...')
            print('\n\n')
        # show final hands        
        display_hands(player_hand, dealer_hand, True)
        
        player_val = get_hand_vals(player_hand)
        dealer_val = get_hand_vals(dealer_hand)
        # handle whether the player won, lost or tied
        if dealer_val > 21:
            print(blue+'\n\t\t Dealer busts!'+e+' You win '+yellow+'${}!'.format(bet)+e)
            money += bet
        elif (player_val > 21) or (player_val < dealer_val):
            print(red+'\n\t\t You LOST!'+e)
            money -= bet
        elif player_val > dealer_val:
            print(green+'\n\t\t You won '+yellow+'${} '.format(bet)+e+' this turn.')
            money += bet
        elif player_val == dealer_val:
            print(purple+'\n\t\t It\'s a '+purple+'tie'+e+', the bet is returned to you.'+e)
                
        input('\t\t Press '+green+'ENTER '+e+'to continue...\n')
        adorn()
        print('\n')

def game_intro():
    adorn()
    print('''                                                
                         Blackjack Game
        
        Rules:
        
          Try to get as close to 21 without going over.
           ---> Kings, Queens, and Jacks are worth 10 points.
           ---> Aces are, on the other hand, worth 1 or 11 points.
           ---> Cards 2 through 10 are worth their face value.
          
          (H)it to take another card.
          (S)tand to stop taking cards.
          On your first play, you can (D)ouble down to increase
             your bet, but you must hit exactly one more time
             before standing.
        
          In case of a tie, the bet is returned to the player.
             The dealer stops hitting at 17.
''')

def play_game():
    global money
    while True:
        if money <= 0:
            print("\t You\'re "+red+"broke"+e+"!")
            sleep(0.7)
            print("\t Good thing you weren\'t playing with real money...!")
            sleep(0.7)
            print("\t   Thank for playing!\n")
            adorn()
            sleep(0.5)
            sys.exit()
        #let the player enter their bet for this round
        print("\t Total money amount: ", money)
        bet = get_bet(money)
        #give the dealer and player two cards from the deck each
        deck = get_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]
        
        # handle player actions
        print("\t >>> Your bet: ", bet)
        while True: #keep looping until player stands or busts
            display_hands(player_hand, dealer_hand, False)
            print()
            #check if the player has bust
            if get_hand_vals(player_hand) > 21:
                break
            #get the player's move
            move = get_move(player_hand, money-bet)
            if move == 'D':
                # player is doubling down, they can increase their bet
                addition_bet = get_bet(min(bet, (money-bet)))
                bet += addition_bet
                print('\t :::: Bet increased to {}'.format(bet))
                print('\t  ---> Bet = ', bet)
            
            if move in ('H', 'D'):
                # hit/doubling down takes another card
                new_card = deck.pop()
                rank, suit = new_card
                print('\n\t You drew a {} of {}.'.format(rank, suit))
                player_hand.append(new_card)
                
                if get_hand_vals(player_hand) > 21:
                    # the player has busted
                    continue
                
            if move in ('S', 'D'):
                # stand/doubling down stops the player's turn
                break
        handle_dealer(player_hand, dealer_hand, bet, deck)
                
def start_app():
    game_intro()
    play_game()
    

if __name__ == '__main__':
    try:
        start_app()
    
    except (KeyboardInterrupt, SystemExit):
        print("\n\t  User has stopped the program execution.")
