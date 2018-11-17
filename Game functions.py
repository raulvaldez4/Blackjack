def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except:
            print('Please provide a number')
        else:
            if chips.bet > chips.total:
                print('Sorry you do not have enough chips! You have: {}'.format(chips.total))
            else:
                break


def hit(deck,hand):
    single_card = deck.deal()  # method from Deck class
    hand.add_card(single_card)  # method from Hand class, passing in single_card from Deck class deal() method
    hand.adjust_for_ace()  # method from Hand class


def double_down(deck, hand, chips):
    chips.bet += chips.bet
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


#def split(deck, hand, chips):
    #chips.bet += chips.bet
    #single_card = deck.deal()
    #hand.add_card(single_card)
    #hand.adjust_for_ace()


#def split_hands(hand):
    #hand_1 = []
    #hand_2 = []
    #if hand.value_list[0] == hand.value_list[1] or hand.aces == 2:
        #hand_1.append(hand.value_list[0])
        #hand_2.append(hand.value_list[1])


def hit_or_stand_or(deck,hand,chips):
    global first_turn
    global playing
    is_split_flag = False
    #hand.value_list[0] == hand.value_list[1] or hand.aces == 2

    while first_turn:
        if is_split_flag:
            x = input('\nHit, Stand, Split or Double Down? Enter H, ST, SP or DD: ')
            if x.upper() == 'H':
                hit(deck, hand)
                first_turn = False
                playing = True
            elif x.upper() == 'DD':
                if chips.bet * 2 > chips.total:
                    print('\nPlayer does not have enough chips to double down!')
                    continue
                double_down(deck, hand, chips)
                first_turn = False
                playing = False
            elif x.upper() == 'ST':
                print("Player Stands, Dealer's Turn")
                first_turn = False
                playing = False
            elif x.upper() == 'SP':
                break
            else:
                print("I don't understand, Please enter H, ST, SP or DD only ")
                continue
            break

        else:
            x = input('\nHit, Stand, or Double Down? Enter H, ST, or DD: ')
            if x.upper() == 'H':
                hit(deck, hand)
                first_turn = False
                playing = True
            elif x.upper() == 'DD':
                if chips.bet * 2 > chips.total:
                    print('\nPlayer does not have enough chips to double down!')
                    continue
                double_down(deck, hand, chips)
                first_turn = False
                playing = False
            elif x.upper() == 'ST':
                print("Player Stands, Dealer's Turn")
                first_turn = False
                playing = False
            else:
                print("I don't understand, Please enter H, ST, or DD only ")
                continue
        break


def hit_or_stand(deck,hand,chips=0):
    global playing

    while playing:
        x = input('\nHit or Stand? Enter H or ST: ')
        if x.upper() == 'H':
            hit(deck, hand)
        elif x.upper() == 'ST':
            print("Player Stands, Dealer's Turn")
            playing = False
        else:
            print("I don't understand, Please enter H or ST only ")
            continue
        break


def show_some(player,dealer):
    print("Dealer's Hand:")
    print(' <card hidden>')
    print('',dealer.cards[1])
    print('\n')
    print("Player's Hand:")
    for card in player.cards:
        print(card)
    print(player.value_list)
    print('Player Total:',player.value)


def basic_strategy(player, dealer):
    print("Dealer shows {}".format(dealer.value_list[1]))
    if player.soft:
        if player.value in range(19,22):
            print('Player should stay, soft {}'.format(player.value))
        if player.value == 18 and len(player.value_list) == 2 and dealer.value_list[1] in [2,7,8]:
            print('Player should stay, soft {}'.format(player.value))
        if player.value == 18 and len(player.value_list) == 2 and dealer.value_list[1] in [3,4,5,6]:
            print('Player should double down, soft {}'.format(player.value))
        if player.value == 18 and len(player.value_list) == 2 and dealer.value_list[1] in [9,10,11]:
            print('Player should hit, soft {}'.format(player.value))
        if player.value == 18 and len(player.value_list) > 2:
            print('Player should stay, soft {}'.format(player.value))
        if player.value in range(13,18) and dealer.value_list[1] in [7,8,9,10,11]:
            print('Player should hit, soft {}'.format(player.value))
        if player.value == 17 and dealer.value_list[1] == 2:
            print('Player should hit, soft {}'.format(player.value))
        if player.value == 17 and dealer.value_list[1] in [3,4,5,6]:
            print('Player should double down, soft {}'.format(player.value))
        if player.value in [15,16] and dealer.value_list[1] in [2,3]:
            print('Player should hit, soft {}'.format(player.value))
        if player.value in [15,16] and dealer.value_list[1] in [4,5,6]:
            print('Player should double down, soft {}'.format(player.value))
        if player.value in [13,14] and dealer.value_list[1] in [2,3,4]:
            print('Player should hit, soft {}'.format(player.value))
        if player.value in [13,14] and dealer.value_list[1] in [5,6]:
            print('Player should double down, soft {}'.format(player.value))
        if player.value == 12 and len(player.value_list) == 2:
            print('Player should always split aces')
    if not player.soft:
        if player.value in range(17,22) and dealer.value_list[1] in range(2,12) and player.value_list != [8,8] and \
                player.value_list != [9,9]:
            print("Player should stay, hard {}".format(player.value))
        if player.value in [13,14,15,16] and dealer.value_list[1] in [2,3,4,5,6] and player.value_list != [7,7] and \
                player.value_list != [8,8]:
            print('Player should stay, hard {}'.format(player.value))
        if player.value in [13,14,15,16] and dealer.value_list[1] in [7,8,9,10,11] and player.value_list != [7,7] and \
                player.value_list != [8,8]:
            print('Player should hit, hard {}'.format(player.value))
        if player.value == 12 and dealer.value_list[1] in [2,3,7,8,9,10,11] and player.value_list != [6,6]:
            print('Player should hit, hard {}'.format(player.value))
        if player.value == 12 and dealer.value_list[1] in [4,5,6] and player.value_list != [6,6]:
            print('Player should stay, hard {}'.format(player.value))
        if player.value == 11 and dealer.value_list[1] != 11:
            print('Player should double down, hard {}'.format(player.value))
        if player.value == 11 and dealer.value_list[1] == 11:
            print('Player should hit, hard {}'.format(player.value))
        if player.value == 10 and dealer.value_list[1] not in [10,11]:
            print('Player should double down, hard {}'.format(player.value))
        if player.value == 10 and dealer.value_list[1] in [10,11]:
            print('Player should hit, hard {}'.format(player.value))
        if player.value == 9 and dealer.value_list[1] in [2,6,7,8,9,10,11]:
            print('Player should hit, hard {}'.format(player.value))
        if player.value == 9 and dealer.value_list[1] in [3,4,5]:
            print('Player should double down, hard {}'.format(player.value))
        if player.value in [5,6,7,8] and player.value_list != [3,3] and player.value_list != [4,4]:
            print('Player should hit, hard {}'.format(player.value))
        if player.value_list == [2,2] and dealer.value_list[1] in [2,3,4,5,6,7]:
            print('Player should split 2s')
        if player.value_list == [2,2] and dealer.value_list[1] in [8,9,10,11]:
            print('Player should hit with two 2s')
        if player.value_list == [3,3] and dealer.value_list[1] in [2,3,4,5,6,7]:
            print('Player should split 3s')
        if player.value_list == [3,3] and dealer.value_list[1] in [8, 9, 10, 11]:
            print('Player should hit with two 3s')
        if player.value_list == [4,4] and dealer.value_list[1] in [2,3,4,7,8,9,10,11]:
            print('Player should hit, two 4s')
        if player.value_list == [4,4] and dealer.value_list[1] in [5,6]:
            print('Player should split 4s')
        if player.value_list == [6,6] and dealer.value_list[1] in [2,3,4,5,6]:
            print('Player should split 6s')
        if player.value_list == [6,6] and dealer.value_list[1] in [7,8,9,10,11]:
            print('Player should hit, two 6s')
        if player.value_list == [7,7] and dealer.value_list[1] in [2,3,4,5,6,7]:
            print('Player should split 7s')
        if player.value_list == [7,7] and dealer.value_list[1] in [8,9,10,11]:
            print('Player should hit with two 7s')
        if player.value_list == [8,8]:
            print('Player should split 8s')
        if player.value_list == [9,9] and dealer.value_list[1] in [2,3,4,5,6,8,9]:
            print('Player should split 9s')
        if player.value_list == [9,9] and dealer.value_list[1] in [7,10,11]:
            print('Player should stay with two 9s')


def show_all(player,dealer):
    print("Dealer's Hand:")
    for card in dealer.cards:
        print(card)
    print('\n')
    print("Player's Hand:")
    for card in player.cards:
        print(card)


def player_busts(player,dealer,chips):
    print('Player busts!')
    chips.lose_bet()


def player_wins(player,dealer,chips):
    print('Player wins!')
    chips.win_bet()


def dealer_busts(player,dealer,chips):
    print('Dealer busts! Player wins!')
    chips.win_bet()


def dealer_wins(player,dealer,chips):
    print('Dealer wins!')
    chips.lose_bet()


def push(player,dealer):
    print('Dealer and Player tie!')