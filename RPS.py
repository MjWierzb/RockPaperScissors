def player(prev_play, opponent_history=[]):
    import random

    # Add opponent's move to history
    if prev_play != "":
        opponent_history.append(prev_play)

    # Initialize persistent variables
    if not hasattr(player, "my_history"):
        player.my_history = []
    if not hasattr(player, "bot_type"):
        player.bot_type = None
    if not hasattr(player, "debug_printed"):
        player.debug_printed = False

    # Reset for new match
    if prev_play == "":
        player.my_history = []
        player.bot_type = None
        player.debug_printed = False
        opponent_history.clear()
        return "R"

    # Bot detection - more robust approach
    if player.bot_type is None and len(opponent_history) >= 8:

        # Check for Quincy first - most distinctive pattern
        # Quincy: R, P, P, S, R (exact 5-move cycle)
        quincy_pattern = ["R", "P", "P", "S", "R"]
        quincy_matches = 0
        total_quincy_checks = min(len(opponent_history), 20)
        for i in range(total_quincy_checks):
            expected = quincy_pattern[i % 5]
            if opponent_history[i] == expected:
                quincy_matches += 1

        quincy_accuracy = quincy_matches / total_quincy_checks
        if quincy_accuracy >= 0.85:
            player.bot_type = "quincy"

        # Check for Kris - he counters our previous move
        elif len(player.my_history) >= 4:
            kris_counter = {"R": "P", "P": "S", "S": "R"}
            kris_matches = 0
            total_kris_checks = 0

            # Check last several moves for Kris pattern
            for i in range(
                    1, min(len(player.my_history), len(opponent_history), 10)):
                if i < len(player.my_history) and i <= len(opponent_history):
                    my_prev = player.my_history[-i - 1]
                    opp_current = opponent_history[-i]
                    expected_kris = kris_counter.get(my_prev, "R")
                    if opp_current == expected_kris:
                        kris_matches += 1
                    total_kris_checks += 1

            if total_kris_checks > 0 and kris_matches / total_kris_checks >= 0.8:
                player.bot_type = "kris"

        # Check for Mrugesh - more thorough detection
        if player.bot_type is None and len(player.my_history) >= 6:
            # Mrugesh counters our most frequent move from last 10
            recent_my_moves = player.my_history[-10:]
            my_counts = {
                "R": recent_my_moves.count("R"),
                "P": recent_my_moves.count("P"),
                "S": recent_my_moves.count("S")
            }

            if max(my_counts.values()) > 0:  # Avoid division by zero
                most_frequent = max(my_counts, key=my_counts.get)
                mrugesh_counter = {"R": "P", "P": "S", "S": "R"}
                expected_move = mrugesh_counter[most_frequent]

                # Check recent opponent moves for this pattern
                recent_opp = opponent_history[-6:]
                mrugesh_frequency = recent_opp.count(expected_move) / len(
                    recent_opp)

                # Also check if opponent is consistently playing the counter
                if mrugesh_frequency >= 0.65:
                    player.bot_type = "mrugesh"

        # Default to Abbey if no clear pattern detected
        if player.bot_type is None:
            player.bot_type = "abbey"

        # Debug print once per game
        if not player.debug_printed:
            print(f"Detected bot type: {player.bot_type}")
            print(f"First 10 opponent moves: {opponent_history[:10]}")
            player.debug_printed = True

    # Strategy based on detected bot type
    counter = {"R": "P", "P": "S", "S": "R"}

    if player.bot_type == "quincy":
        # Quincy plays: R, P, P, S, R (5-move cycle)
        quincy_cycle = ["R", "P", "P", "S", "R"]
        next_move = quincy_cycle[len(opponent_history) % 5]
        guess = counter[next_move]

    elif player.bot_type == "kris":
        # Kris counters our previous move
        if len(player.my_history) > 0:
            my_last = player.my_history[-1]
            kris_will_play = counter[my_last]  # Kris counters our last move
            guess = counter[kris_will_play]  # We counter Kris's counter
        else:
            guess = "R"

    elif player.bot_type == "abbey":
        # Abbey uses enhanced unpredictability while avoiding common patterns

        if len(player.my_history) >= 1:
            move_num = len(player.my_history)

            # Use a more extensive prime-based sequence
            prime_sequence = [
                "R", "P", "S", "R", "R", "S", "P", "S", "R", "P", "P", "S",
                "R", "S", "R", "P"
            ]

            # Randomization adjustment based on history length
            if len(player.my_history) >= 2:
                last_two = player.my_history[-2:]

                if last_two.count("R") >= 2:
                    guess = random.choice(["P", "S"])  # Avoid R
                elif last_two.count("P") >= 2:
                    guess = random.choice(["R", "S"])  # Avoid P
                elif last_two.count("S") >= 2:
                    guess = random.choice(["R", "P"])  # Avoid S
                else:
                    # Choose based on the prime sequence with added randomness
                    guess = prime_sequence[move_num % len(prime_sequence)]
                    if move_num % 5 == 0:  # Introduce randomness every 5th move
                        guess = random.choice(["R", "P", "S"])
            else:
                guess = prime_sequence[move_num % len(prime_sequence)]
        else:
            guess = "R"

    elif player.bot_type == "mrugesh":
        # Mrugesh counters our most frequent move from last 10
        # Strategy: Keep moves balanced and use anti-frequency analysis
        if len(player.my_history) >= 3:
            # Look at what Mrugesh is tracking (our last 10 moves)
            recent_moves = player.my_history[-10:] if len(
                player.my_history) >= 10 else player.my_history
            my_counts = {
                "R": recent_moves.count("R"),
                "P": recent_moves.count("P"),
                "S": recent_moves.count("S")
            }

            # Find least used move to keep balanced
            min_count = min(my_counts.values())
            least_used = [
                move for move, count in my_counts.items() if count == min_count
            ]

            # Use a predictable sequence that stays balanced
            balanced_sequence = ["R", "P", "S", "P", "S", "R", "S", "R", "P"]
            sequence_move = balanced_sequence[len(player.my_history) %
                                              len(balanced_sequence)]

            # Prefer the sequence move if it's among the least used
            if sequence_move in least_used:
                guess = sequence_move
            else:
                guess = random.choice(least_used)
        else:
            # Early game - start with balanced sequence
            guess = ["R", "P", "S"][len(player.my_history) % 3]

    else:
        # Enhanced fallback strategy
        if len(opponent_history) >= 5:
            # Try to detect pattern in real-time and counter it
            if len(opponent_history) >= 5:
                # Check if it might be Quincy after all
                quincy_test = ["R", "P", "P", "S", "R"]
                recent_quincy_matches = sum(
                    1 for i in range(-5, 0)
                    if opponent_history[i] == quincy_test[i % 5])
                if recent_quincy_matches >= 4:
                    next_move = quincy_test[len(opponent_history) % 5]
                    guess = counter[next_move]
                else:
                    # Default anti-pattern strategy
                    guess = random.choice(["R", "P", "S"])
            else:
                guess = "R"
        else:
            guess = "R"

    # Record our move
    player.my_history.append(guess)
    return guess