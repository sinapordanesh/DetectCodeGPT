def texas_holdem_probability():
    import itertools

    def rank_to_val(rank):
        if rank == 'A':
            return 14
        if rank == 'K':
            return 13
        if rank == 'Q':
            return 12
        if rank == 'J':
            return 11
        if rank == 'T':
            return 10
        return int(rank)

    def is_flush(hand):
        return len(set(card[0] for card in hand)) == 1

    def is_straight(hand):
        values = sorted([rank_to_val(card[1]) for card in hand])
        return values == list(range(min(values), max(values)+1))

    def is_straight_flush(hand):
        return is_straight(hand) and is_flush(hand)

    def is_royal_straight_flush(hand):
        return is_straight_flush(hand) and rank_to_val(hand[0][1]) == 10

    def is_four_of_a_kind(hand):
        values = [card[1] for card in hand]
        for val in values:
            if values.count(val) == 4:
                return True
        return False

    def is_full_house(hand):
        values = [card[1] for card in hand]
        for val in values:
            if values.count(val) == 3:
                for other_val in values:
                    if other_val != val and values.count(other_val) >= 2:
                        return True
        return False

    def is_three_of_a_kind(hand):
        values = [card[1] for card in hand]
        for val in values:
            if values.count(val) == 3:
                return True
        return False

    def is_two_pair(hand):
        values = [card[1] for card in hand]
        pairs = set()
        for val in values:
            if values.count(val) == 2:
                pairs.add(val)
        return len(pairs) == 2

    def is_one_pair(hand):
        values = [card[1] for card in hand]
        for val in values:
            if values.count(val) == 2:
                return True
        return False

    def get_hand_rank(hand):
        if is_royal_straight_flush(hand):
            return 10
        if is_straight_flush(hand):
            return 9
        if is_four_of_a_kind(hand):
            return 8
        if is_full_house(hand):
            return 7
        if is_flush(hand):
            return 6
        if is_straight(hand):
            return 5
        if is_three_of_a_kind(hand):
            return 4
        if is_two_pair(hand):
            return 3
        if is_one_pair(hand):
            return 2
        return 1

    def get_best_hand(hand):
        best_hand = []
        for five_cards in itertools.combinations(hand, 5):
            if get_hand_rank(list(five_cards)) > get_hand_rank(best_hand):
                best_hand = list(five_cards)
        return best_hand

    def get_all_possible_hands(your_hand, opponent_hand, community_cards):
        deck = [suit + rank for suit in 'SHDC' for rank in 'AKQJT98765432']
        for card in your_hand + opponent_hand + community_cards:
            deck.remove(card)
        possible_hands = []
        for hand in itertools.combinations(deck, 2):
            possible_hands.append(list(hand) + community_cards)
        return possible_hands

    def calculate_win_probability(your_hand, opponent_hand, community_cards):
        possible_hands = get_all_possible_hands(your_hand, opponent_hand, community_cards)
        wins = 0
        ties = 0
        losses = 0
        for possible_hand in possible_hands:
            your_best_hand = get_best_hand(your_hand + community_cards)
            opponent_best_hand = get_best_hand(opponent_hand + community_cards)
            if possible_hand == your_hand + community_cards:
                continue
            if get_hand_rank(your_best_hand) > get_hand_rank(opponent_best_hand):
                wins += 1
            elif get_hand_rank(your_best_hand) < get_hand_rank(opponent_best_hand):
                losses += 1
            else:
                if your_best_hand > opponent_best_hand:
                    wins += 1
                elif your_best_hand < opponent_best_hand:
                    losses +=1
                else:
                    ties += 1
        return wins / (wins + ties + losses)

    while True:
        your_hand_1, your_hand_2 = input().split()
        if your_hand_1 == '#':
            break
        opponent_hand_1, opponent_hand_2 = input().split()
        community_cards = input().split()
        print('{:.20f}'.format(calculate_win_probability([your_hand_1, your_hand_2], [opponent_hand_1, opponent_hand_2], community_cards)))

texas_holdem_probability()