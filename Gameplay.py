while True:
    # Print an opening statement
    print('Welcome to BlackJack!')

    # Create and shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()  # assign Hand class to player_hand
    player_hand.add_card(deck.deal())  # draws one card
    player_hand.add_card(deck.deal())  # draws one card

    dealer_hand = Hand()  # assign Hand class to dealer_hand
    dealer_hand.add_card(deck.deal())  # draws one card
    dealer_hand.add_card(deck.deal())  # draws one card

    # Setup the Player's chips
    player_chips = Chips()

    # Prompt the player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)

    # Basic strategy advice
    basic_strategy(player_hand,dealer_hand)

    while first_turn:

        # Prompt player to hit, stand, double down
        hit_or_stand_or(deck,player_hand,player_chips)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)

        # Basic strategy advice
        basic_strategy(player_hand, dealer_hand)

        # If Player hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            playing = False

        break

    while playing:
        hit_or_stand(deck,player_hand,player_chips)

        show_some(player_hand,dealer_hand)

        basic_strategy(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    # If player hasn't busted, play Dealer's hand until dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

        # Show all cards
        show_all(player_hand,dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif player_hand.value > dealer_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)

    print('\n Player total chips are at: {}'.format(player_chips.total))


    # Ask to play again
    new_game = input('Would you like to play another hand? Y/N ')
    if new_game[0].upper() == 'Y':
        first_turn = True
        continue
    else:
        print('Thanks for playing')
        break