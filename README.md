# Poker Data Science #
A repository dedicated to the analysis and modeling of poker game data using data science techniques.
## Overview ##
This repository contains various scripts and notebooks that aim to explore poker game data, perform statistical analysis, and build predictive models. The goal is to gain insights into player behavior, game dynamics, and strategies that can improve performance in poker games. So far, the notebooks calculate equity estimates based on hand features over Monte-Carlo data.
## Contents ##
- **[Section 01: Data Generation](notebooks/01_hand_simulation.ipynb)**: Notebook for generating synthetic poker game data.
- **[Section 02: Pre-Flop Equity](notebooks/03_preflop_equity.ipynb)**: Notebook for estimating pre-flop equity using Monte Carlo simulations.
- **[Section 03: Flop Equity](notebooks/04_flop_equity.ipynb)**: Notebook for estimating flop equity using Monte Carlo simulations.
- **[Section 04: Turn and River Equity](notebooks/05_turn_river_equity.ipynb)**: Notebook for estimating turn and river equity using Monte Carlo simulations.

[Pre-flop Equity Matrices](https://public.tableau.com/shared/5HX3QMJ2D?:display_count=n&:origin=viz_share_link)

# My Tableau Embed

<div class='tableauPlaceholder' id='viz1758924121422' style='position: relative'><noscript><a href='#'><img alt='Estimated 2-Player Pre-flop Equity' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5X&#47;5XD6RX98J&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;5XD6RX98J' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;5X&#47;5XD6RX98J&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1758924121422');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>

