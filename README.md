# Rock Paper Scissors Bot

This project contains a Python bot designed to play Rock Paper Scissors against four different AI opponents: Quincy, Abbey, Kris, and Mrugesh. The goal is to achieve a win rate of at least 60% against each opponent.

## Strategy

The bot uses an **ensemble strategy** that simultaneously simulates multiple prediction models:
1.  **Quincy Counter**: Detects Quincy's fixed 5-move pattern.
2.  **Kris Counter**: Predicts Kris will play the counter to our last move.
3.  **Mrugesh Counter**: Predicts Mrugesh will counter our most frequent move in the last 10 turns.
4.  **Abbey Counter**: Simulates Abbey's Markov Chain model to predict her next move and counters it.

The bot tracks the success rate of each strategy in real-time and dynamically switches to the most effective one for the current opponent.