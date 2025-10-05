from math import comb

# total_hands is the number of ways to choose (players-1) opponents from 8 possible opponents
def total_hands(players):
    """
    Calculate the total number of possible hands given the number of players.
    8 choose (players-1)
    8 possible opponents (excluding the player)
    :param players: Integer representing the number of players (including the player).
    2 <= players <= 9
    :return: Integer representing the total number of possible hands.
    """
    return comb(8, players - 1)

# wins is the number of ways to choose (players-1) opponents from (9-showdown_order) possible opponents
def wins(showdown_order, players):
    """
    Calculate the number of winning hands given the showdown order and number of players.
    (9 - showdown_order) choose (players - 1)
    9 - showdown_order possible opponents (excluding the player and those who have already shown down
    :param showdown_order: Integer representing the order in which the player's hand was ranked among 9 other hands
     (1-based).
    1 <= showdown_order <= 9
    :param players: Integer representing the number of players (including the player).
    2 <= players <= 9
    :return: Integer representing the number of winning hands.
    0 <= wins <= total_hands
    """
    return comb(9 - showdown_order, players - 1)