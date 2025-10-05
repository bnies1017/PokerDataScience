# Poker Data Science #
A repository dedicated to the analysis and modeling of poker game data using data science techniques.

## Overview ##
This repository contains various scripts and notebooks that aim to explore poker game data, perform statistical analysis, and build predictive models. The goal is to gain insights into player behavior, game dynamics, and strategies that can improve performance in poker games. So far, the notebooks calculate equity estimates based on hand features over Monte-Carlo data.

## Notebooks ##
- **[Section 01: Hand Simulation](notebooks/01_hand_simulation.ipynb)**: Generates synthetic poker game data.
- **[Section 02: Hand Frequency Distribution](notebooks/02_hand_freq_distribution.ipynb)**: Approximates hand likelihood using hand frequencies and demonstrates their distributons.
- **[Section 03: Pre-Flop Equity](notebooks/03_preflop_equity.ipynb)**: Estimates Pre-flop equity using Monte Carlo simulation.
- **[Section 04: Flop Equity](notebooks/04_flop_equity.ipynb)**: Estimates Flop equity using Monte Carlo simulation.
- **[Section 05: Turn and River Equity](notebooks/05_turn_river_equity.ipynb)**: Estimates Turn and River equity using Monte Carlo simulation.

## Procedure ##
1. Simulate 100,000 hands of poker data using the `deuces` library. 
