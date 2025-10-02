from math import comb
from deuces import Card, Evaluator
import pandas as pd

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

evaluator = Evaluator()

def hand_classification(hand_eval):
    """
    Get the hand classification (e.g., Pair, High Card, etc.) for given hole and board cards.
    :param hand_eval: Integer representing the hand evaluation from deuces Evaluator.
    1 <= hand_eval <= 7462
    :return: Integer representing the hand classification.
    """
    return evaluator.get_rank_class(hand_eval)

def is_pocket_pair(hole):
    """
    Check if the hole cards are a pocket pair.
    :param hole: List of deuces card integers representing the hole cards.
    :return: Boolean indicating if the hole cards are a pocket pair.
    """
    return Card.get_rank_int(hole[0]) == Card.get_rank_int(hole[1])

def is_suited(hole):
    """
    Check if the hole cards are suited.
    :param hole: List of deuces card integers representing the hole cards.
    :return: Boolean indicating if the hole cards are suited.
    """
    return Card.get_suit_int(hole[0]) == Card.get_suit_int(hole[1])

def flush_potential(hole, board):
    """
    Determine the flush potential given hole and board cards.
    :param hole: List of deuces card integers representing the hole cards.
    :param board: List of deuces card integers representing the board cards.
    :return: String indicating flush potential: 'Complete', 'Open', 'Backdoor', or 'None'.
    """
    suits = [Card.get_suit_int(card) for card in hole + board]
    suit_counts = pd.Series(suits).value_counts()
    max_suit_count = suit_counts.max()
    if max_suit_count >= 5:
        return 'Complete'
    elif max_suit_count == 4:
        return 'Open'
    elif max_suit_count == 3:
        return 'Backdoor'
    else:
        return 'None'


from deuces import Card
from itertools import combinations


def straight_potential(hole, board):
    all_cards = hole + board
    ranks = [Card.get_rank_int(c) for c in all_cards]

    # Add Ace as low (-1)
    if 12 in ranks:
        ranks.append(-1)

    unique_ranks = sorted(set(ranks))

    # Check for Complete Straight
    for combo in combinations(unique_ranks, 5):
        sorted_combo = sorted(combo)
        if sorted_combo[-1] - sorted_combo[0] == 4:
            return 'Complete'

    # Check for 4-card straight draw (Open-ended or Gutshot)
    for combo in combinations(unique_ranks, 4):
        sorted_combo = sorted(combo)
        if sorted_combo[-1] - sorted_combo[0] == 3:
            return 'Open'
        elif sorted_combo[-1] - sorted_combo[0] == 4:
            return 'Gut-shot'

    # Check for Backdoor (3-card sequences)
    for combo in combinations(unique_ranks, 3):
        sorted_combo = sorted(combo)
        if sorted_combo[-1] - sorted_combo[0] <= 4:
            return 'Backdoor'

    return 'None'


def overcards(hole, board):
    """
    Count how many hole cards are higher than the highest card on the board.
    Assumes hole and board are lists of Card objects or strings compatible with Card.get_rank_int().
    """
    if not board:  # edge case: no board yet
        return len(hole)

    max_board_rank = max(Card.get_rank_int(card) for card in board)
    return sum(1 for card in hole if Card.get_rank_int(card) > max_board_rank)


def suit_texture(board):
    """
    Determine the board texture based on the number of unique suits on the board.
    :param board: List of deuces card integers representing the board cards.
    :return: Integer representing the number of unique suits on the board.
    """
    suits = [Card.get_suit_int(card) for card in board]
    return len(set(suits))

def rank_texture(board):
    """
    Determine the board texture based on the number of unique ranks on the board.
    :param board: List of deuces card integers representing the board cards.
    :return: Integer representing the number of unique ranks on the board.
    """
    ranks = [Card.get_rank_int(card) for card in board]
    return len(set(ranks))

def board_connectivity(board):
    """
    Determine the board connectivity based on the number of cards required to complete a straight on the board.
    :param board: List of deuces card integers representing the board cards.
    :return: String indicating board connectivity: 'High', 'Medium', or 'Low'.
    """
    ranks = [Card.get_rank_int(card) for card in board]
    unique_ranks = sorted(set(ranks))
    # Add Ace as both high (12) and low (-1) for straight calculations
    if 12 in unique_ranks:
        unique_ranks.append(-1)
    unique_ranks = sorted(set(unique_ranks))
    max_seq_len = 1
    current_seq_len = 1
    for i in range(1, len(unique_ranks)):
        if unique_ranks[i] == unique_ranks[i-1] + 1:
            current_seq_len += 1
        else:
            if current_seq_len > max_seq_len:
                max_seq_len = current_seq_len
            current_seq_len = 1
    if current_seq_len > max_seq_len:
        max_seq_len = current_seq_len
    if max_seq_len >= 4:
        return 'High'
    elif max_seq_len == 3:
        return 'Medium'
    else:
        return 'Low'

