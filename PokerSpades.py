cards = ('S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK','SA')

card_dict = {'S2':2,'S3':3,'S4':4,'S5':5,'S6':6,'S7':7,'S8':8,'S9':9,'S10':10,'SJ':11,'SQ':12,'SK':13,'SA':14}



#If the cards passed in are three cards in a sequence, this function returns the greatest value.
#Otherwise it returns 0. For example, check_straight('S5','S6','S7') would return 7.
# check_straight('S6', 'S5', 'S7') would also return 7.  check_straight('S3','SQ','SK') would return 0.
# Come up with several tests.

def check_straight(card1, card2, card3):
    card1_value = card_dict[card1]
    card2_value = card_dict[card2]
    card3_value = card_dict[card3]

    hand = [card1_value,card2_value,card3_value]
    hand.sort()
    if hand[1] - hand[0] == 1 and hand[2] - hand[1] == 1:
        return hand[2]
    else:
        return 0










#If the three cards passed in are all the same, return the value.
#Otherwise return 0. For example, check_3ofa_kind('S9', 'S9', 'S9') would return 9.
# check_3ofa_kind('S2', 'S4', 'S2') would return 0.

def check_3ofa_kind(card1, card2, card3):
    if card1 == card2 and card2 == card3:
        return card_dict[card1]
    else:
        return 0

#If the cards passed in are a straight with the value of 14,
# then this function returns 14. Otherwise it returns 0.
# For this one, you only need maybe three tests.


def check_royal_flush(card1, card2, card3):
    x = check_straight(card1,card2,card3)
    if x == 14:
        return 14
    else:
        return 0


#This method takes three cards for the left player (left1, left2, left3)
# and three cards for the right player (right1, right2, right3) and determines who wins.
#If left wins, it returns -1.
#If neither win (a draw), it returns 0.
#If right wins, it returns 1.

def play_cards(left1, left2, left3, right1, right2, right3):
    left_flush = check_royal_flush(left1,left2,left3)
    right_flush = check_royal_flush(right1, right2, right3)

    if left_flush == 14 and right_flush == 14:
        return 0
    elif left_flush == 14 and right_flush == 0:
        return -1
    elif left_flush == 0 and right_flush == 14:
        return 1
    else:
        left_straight = check_straight(left1,left2,left3)
        right_straight = check_straight(right1, right2, right3)
        if left_straight > right_straight:
            return -1
        elif right_straight > left_straight:
            return 1
        elif left_straight > 0 and right_straight > 0 and left_straight == right_straight:
            return 0
        else:
            left_3kind = check_3ofa_kind(left1,left2,left3)
            right_3kind = check_3ofa_kind(right1,right2,right3)

            if left_3kind > right_3kind:
                return -1
            elif right_3kind > left_3kind:
                return 1
            elif left_3kind == right_3kind:
                return 0



