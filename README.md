# Texas Holdem Monte Carlo #
A repository dedicated to generating poker game data using Monte Carlo style simulation.

## Overview ##
This repository contains various scripts and notebooks that aim to simulate poker game data and estimate equity in a 
number of situations, which ultimately could be useful to gain insights into player behavior, game dynamics, and 
strategies that can improve performance in poker games. Equity estimates are based on hand features for winning hands 
as they appear over Monte-Carlo simulation data.

## [Section 01: Hand Simulation](./notebooks/01_hand_simulation.ipynb) ##

First, 100,000 hands of Texas Holdem poker are simulated, each with 9 players. For each hand, two hole cards are dealt 
to each player, as well as 5 community cards. The strength of each player's hand at each street is measured using a 
`deuces.evaluator` object. Then, each player is given a "showdown order", which represents the ranking of that player's 
hand among the 9 total hands per row. 

Secondly, the wide-form data is converted to a long-form, where each row corresponds to an individual player. This 
method of conversion preserved the relationship between different players and their showdown orders from the wide 
dataframe. Since the wide dataset had 100,000 hands and 9 players, the resulting long data should have 900,000 rows,
which represent each player individually over every hand. The use of the `deuces` library ensures efficient hand 
evaluation, making this dataset a valuable resource for estimating equity, for example. 
The `showdown_order_` feature of the long-form dataset will be essential in estimating hand equity.

## [Section 02: Hand Frequency Distribution](./notebooks/02_hand_freq_distribution.ipynb) ##

Now that the long-form dataset has been generated, its validity can be verifying partially by comparing the frequencies
of different types of hands with their known likelihoods. Subsequently, the RMSE between frequencies and likelihoods can
be used as an approximation for accuracy. The following visualization demonstrates the distribution of frequencies:

![Hand Frequency Distribution](./figures/Hand%20Freq%20Distribution.png)

 In conclusion, the RMSE between frequencies and likelihoods was quite low, which is a good sanity check before equity 
 estimation.
 
## [Section 03: Pre-flop Equity](./notebooks/03_preflop_equity.ipynb) ##

Using the long-form dataset, features meant to aggregate for equity estimation can be engineered. Pre-flop, the most 
valuable information for determining equity will be the rank of each hole card, whether the cards are suited or not, and 
the total number of players. 

Using the showdown order a certain hand is the winner against 9 players only if its showdown order is 1. However, 
combinatorics allows for the calculation of a number of possible subsets of hands given a number of players, as well as
a number of those hands which the current hand wins with a certain showdown order.

To calculate the number of times a hand would win at showdown given its showdown order $O \in [1,9]$ and number of 
players $P \in [2,9]$, as well as the total number of hands to consider for $P$ players, we can use combinatorial
mathematics.

When trying to determine how many hands we need to consider for $P$ players, we can think of it as choosing $P-1$ 
opponents from the 8 total opponents (since one player is the target). Thus, the total number of hands to consider for 
$P$ players is given by:
$$
\text{total hands} = \binom{8}{P-1}
$$
When trying to determine how many times a hand would win at showdown given its showdown order $O$ and number of players 
$P$, there are $9-O$ players with worse showdown order (9 total players - O players with less than or equal showdown 
order). We need to choose $P-1$ opponents from these $9-O$ players. Thus, the number of times a hand would win at 
showdown is given by:
$$
\text{wins} = \binom{9 - O}{P-1}
$$

When the resulting dataframe is grouped by Pre-flop features, and the total wins and hands are aggregated by summation, 
the equity estimation can be calculated given a fixed set of features as:
$$
\text{equity} = \frac{\text{sum(wins)}}{\text{sum(total hands)}} 
$$

In result, a heads-up Pre-flop equity matrix can be visualized, providing insight into which holes have the best winning 
odds:

![Preflop Equity Matrix](./figures/Preflop%20Equity.png)

