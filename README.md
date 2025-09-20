# Rock Paper Scissors

A Python implementation of the classic Rock, Paper, Scissors game tailored for the [freeCodeCamp Machine Learning with Python certification project](https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/rock-paper-scissors). The repository contains an adaptive bot (`player`) that learns how to counter several pre-built opponents.

## Project Structure

| File | Description |
| --- | --- |
| `RPS.py` | Contains the `player` function – an adaptive strategy that detects the opponent type and selects counter moves. |
| `RPS_game.py` | Game engine and opponent implementations (`quincy`, `abbey`, `kris`, `mrugesh`, `human`, and `random_player`). |
| `main.py` | Entry point used during development. Runs sample games and the unit test suite. |
| `test_module.py` | Unit tests that verify the `player` function can defeat each built-in opponent at least 60% of the time. |

## Requirements

- Python 3.8 or higher (standard library only)

## Getting Started

1. **Clone** the repository and `cd` into the project directory.
2. (Optional) **Create a virtual environment**: `python -m venv .venv && source .venv/bin/activate`.
3. **Install dependencies**: none required beyond the Python standard library.

## Running the Project

### Run the default simulations and tests

```bash
python main.py
```

`main.py` pits the adaptive player against each built-in opponent for 1,000 rounds and runs the unit test suite. You can comment or uncomment the `play(...)` calls inside `main.py` to focus on specific matchups during development.

### Run the unit tests directly

```bash
python -m unittest test_module
```

The tests ensure that the adaptive `player` wins at least 60% of games against every provided bot.

### Play manually against a bot

Uncomment the interactive line in `main.py`:

```python
# play(human, abbey, 20, verbose=True)
```

Then run `python main.py`. The console will prompt for your move each round.

## Strategy Overview

The `player` function keeps track of its own move history as well as the opponent's. After observing several rounds it attempts to detect which built-in bot it is facing by analyzing common patterns:

- **Quincy** plays a repeating five-move pattern.
- **Kris** counters your previous move.
- **Mrugesh** counters the most frequent move in your recent history.
- **Abbey** favors transitions between move pairs.

Once a bot is detected, the strategy switches to a tailored counter approach. When no clear pattern emerges, the fallback strategy mixes balanced play with light randomization to stay unpredictable.

## Customizing the Player

You are encouraged to tweak the logic in `RPS.py` or implement a completely new strategy. Use the helper opponents in `RPS_game.py` and the tests in `test_module.py` to validate improvements before submitting your solution to freeCodeCamp.

## License

This project is provided as part of the freeCodeCamp curriculum. Refer to the freeCodeCamp terms of use for details on distribution and usage.
