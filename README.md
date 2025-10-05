# Poker Data Science #
A repository dedicated to the analysis and modeling of poker game data using data science techniques.

## Overview ##
This repository contains various scripts and notebooks that aim to explore poker game data, perform statistical 
analysis, and build predictive models. The goal is to gain insights into player behavior, game dynamics, and strategies 
that can improve performance in poker games. So far, the notebooks calculate equity estimates based on hand features
over Monte-Carlo data.

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