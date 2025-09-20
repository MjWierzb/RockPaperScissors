# Rock Paper Scissors

A Python implementation of the classic Rock, Paper, Scissors game tailored for the [freeCodeCamp Machine Learning with Python certification project](https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/rock-paper-scissors). The repository contains an adaptive bot (`player`) that learns how to counter several pre-built opponents while giving you a sandbox for experimenting with alternative strategies.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Running the Project](#running-the-project)
- [Strategy Overview](#strategy-overview)
- [Customizing the Player](#customizing-the-player)
- [Project Goals & Learning Outcomes](#project-goals--learning-outcomes)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Related Resources](#related-resources)
- [License](#license)

## Features

- ✅ **Adaptive opponent detection** – automatically infers which built-in bot is being faced and shifts tactics accordingly.
- 🧪 **Comprehensive unit tests** – verifies that your strategy beats each supplied opponent at least 60% of the time.
- 🕹️ **Interactive play mode** – challenge any bot manually to observe behavior in real time.
- 🧠 **Learning playground** – cleanly separated modules make it easy to prototype and compare new approaches.

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

### Run a quick benchmark against one opponent

```bash
python - <<'PY'
from RPS_game import play, abbey, player

print(play(player, abbey, 1000))
PY
```

The snippet above bypasses `main.py` so that you can iterate quickly on a single matchup while tuning your strategy.

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

You are encouraged to tweak the logic in `RPS.py` or implement a completely new strategy. The following workflow keeps iterations quick and verifiable:

1. **Fork or branch** from the current solution (if working in your own repository).
2. **Modify** the `player` function in `RPS.py`. Keep the signature `def player(prev_play, opponent_history=[])` intact so the tests continue to run.
3. **Instrument** your strategy with temporary `print` statements or logging while experimenting. Remove them before final submission.
4. **Benchmark** frequently against specific bots (see the [quick benchmark](#run-a-quick-benchmark-against-one-opponent) snippet above).
5. **Validate** using `python -m unittest test_module` to ensure you still meet the 60% win requirement across all opponents.

If you devise a novel opponent, add it to `RPS_game.py` and expand the tests accordingly to evaluate your approach under new conditions.

## Project Goals & Learning Outcomes

Working through this project will help you:

- Practice designing heuristics that respond to noisy, adversarial input data.
- Explore state tracking and pattern recognition techniques without relying on external libraries.
- Gain confidence writing and running Python unit tests.
- Understand how simple rule-based systems can mimic reinforcement-learning style adaptation.

## Troubleshooting

- **Python not found** – ensure you are running Python 3.8+ (`python --version`). Adjust the commands to use `python3` if necessary.
- **Tests still fail after improvements** – double-check that the `player` function maintains state between calls by using a mutable default argument or another shared mechanism.
- **Interactive mode exits immediately** – confirm the `play` call is uncommented and that `verbose=True` is passed if you want to see each round printed.

## Contributing

Issues and pull requests that improve the strategy, documentation, or testing workflow are welcome. Please include a brief description of the change, why it is beneficial, and any relevant test output.

## Related Resources

- [Original freeCodeCamp project description](https://www.freecodecamp.org/learn/machine-learning-with-python/machine-learning-with-python-projects/rock-paper-scissors)
- [Python `random` module documentation](https://docs.python.org/3/library/random.html)
- [unittest module documentation](https://docs.python.org/3/library/unittest.html)

## License

This project is provided as part of the freeCodeCamp curriculum. Refer to the freeCodeCamp terms of use for details on distribution and usage.
