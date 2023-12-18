''' Day 7 of the 2023 Advent of Code
https://adventofcode.com/2023/day/7
https://adventofcode.com/2023/day/7/input '''
from dataclasses import dataclass
from typing import List
from collections import Counter
from functools import cmp_to_key
DEBUG = False

@dataclass
class Hand:
    cards: str
    bet: int


def load_data(Path):
    '''
        32T3K 765
        T55J5 684
        KK677 28
        KTJJT 220
        QQQJA 483
    '''
    data_list = []
    with open(Path, 'r') as file:
        for line in file:
            cards, bet = line.split()
            bet = int(bet)
            data_list.append(Hand(cards, bet))


    return data_list

def compare_cards(card1, card2):
    order = ["A", "K", "Q", "J", "T", "9", "8",
                    "7", "6", "5", "4", "3", "2"]
    index1 = order.index(card1)
    index2 = order.index(card2)
    if index1 > index2:
        return -1
    if index1 < index2:
        return 1
    return 0
   
   
def compare_hands_highcard(hand1, hand2):
    for i in range(len(hand1.cards)):
        if not hand1.cards[i] == hand2.cards[i]:
            r = compare_cards(hand1.cards[i], hand2.cards[i])
            return r
    else:
        raise RuntimeError(f"Could not compare cards {hand1.cards} {hand2.cards}")
        
def compare_hands(hand1, hand2):
    score1 = hand_score(hand1.cards)
    score2 = hand_score(hand2.cards)
    
    if score1 > score2:
        return 1
    if score1 < score2:
        return -1
    
    return compare_hands_highcard(hand1, hand2)
    

def joker_convert(cards):
    if not "J" in cards:
        return cards
    if cards == "JJJJJ":
        return cards
    replace_this_index = 0
    
    c = Counter(cards)
    c_most_common = c.most_common()
    if c_most_common[0][0] == "J":
        replace_this_index = 1
                
    cards = cards.replace("J", c_most_common[replace_this_index][0])
    
    return cards

def compare_hands_joker(hand1, hand2):
    
    j_hand1 = joker_convert(hand1.cards)
    j_hand2 = joker_convert(hand2.cards)
    
    score1 = hand_score(j_hand1)
    score2 = hand_score(j_hand2)
    
    if score1 > score2:
        return 1
    if score1 < score2:
        return -1
    return compare_hands_highcard(hand1, hand2)
    
   
def hand_score(cards):
    c = Counter(cards)
    c_most_common = c.most_common()
    len_c = len(c)
    first_count = c_most_common[0][1]
    # print(hand.cards, c)
    score = 0
    if   first_count == 5:
        # FIVE OF A KIND
        return 7
    elif first_count == 4:
        # FOUR OF A KIND
        return 6
    elif first_count == 3 and len_c == 2:
        # FULL HOUSE
        return 5
    elif first_count == 3 and len_c == 3:
        # Three of a kind
        return 4
    elif first_count == 2 and len_c == 3:
        return 3
        # Two pair
    elif first_count == 2 and len_c == 4:
        return 2
        # One pair
    elif first_count == 1:
        # High card
        return 1
    else:
        raise RuntimeError(f"Could not find hand score: {cards}")


def part_1(data):
    solution = 0  

    data_sorted = sorted(data, key=cmp_to_key(compare_hands))
    
    for i, hand in enumerate(data_sorted):
        solution += (i+1)*hand.bet

    return solution

    
def part_2(data):
    solution = 0  

    data_sorted = sorted(data, key=cmp_to_key(compare_hands_joker))
    
    for i, hand in enumerate(data_sorted):
        solution += (i+1)*hand.bet

    return solution
    

def main():
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")
    assert part_1(data_test) == 6440
    assert part_1(data) == 250474325
    assert part_2(data_test) == 5905
    assert not part_2(data) == 248814038
    # assert part_2(data) == None
    
    # print(part_1(data_test))
    # print(part_1(data))
    # print(part_2(data_test))
    print(part_2(data))


if __name__ == "__main__":
    main()
