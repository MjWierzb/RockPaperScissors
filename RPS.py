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
    
    # Bot detection after enough moves
    if player.bot_type is None and len(opponent_history) >= 15:
        
        # Check for Quincy pattern first: R, P, P, S, R (repeating)
        quincy_pattern = ["R", "P", "P", "S", "R"]
        quincy_matches = 0
        for i in range(min(15, len(opponent_history))):
            expected = quincy_pattern[i % 5]
            if opponent_history[i] == expected:
                quincy_matches += 1
        
        if quincy_matches >= 12:  # At least 80% match
            player.bot_type = "quincy"
        
        # Check for Kris pattern: P, P, R, R, P, S, S, R, R, P (10-move cycle based on debug output)
        else:
            kris_pattern = ["P", "P", "R", "R", "P", "S", "S", "R", "R", "P"]
            kris_matches = 0
            for i in range(min(15, len(opponent_history))):
                expected = kris_pattern[i % 10]
                if opponent_history[i] == expected:
                    kris_matches += 1
            
            if kris_matches >= 12:  # At least 80% match
                player.bot_type = "kris"
        
        # Check for Mrugesh - he uses frequency analysis against us
        if player.bot_type is None and len(player.my_history) >= 10:
            # Mrugesh counters our most frequent overall move
            my_total_counts = {"R": player.my_history.count("R"), 
                             "P": player.my_history.count("P"), 
                             "S": player.my_history.count("S")}
            most_frequent_overall = max(my_total_counts, key=my_total_counts.get)
            mrugesh_should_play = {"R": "P", "P": "S", "S": "R"}[most_frequent_overall]
            
            recent_opp = opponent_history[-5:]
            mrugesh_counter_count = recent_opp.count(mrugesh_should_play)
            
            if mrugesh_counter_count >= 3:
                player.bot_type = "mrugesh"
        
        # If no clear pattern, assume Abbey (the adaptive one)
        if player.bot_type is None:
            player.bot_type = "abbey"
        
        # Debug print once per game
        if not player.debug_printed:
            print(f"Detected bot type: {player.bot_type}")
            print(f"First 15 opponent moves: {opponent_history[:15]}")
            player.debug_printed = True
    
    # Strategy based on detected bot type
    counter = {"R": "P", "P": "S", "S": "R"}

    if player.bot_type == "quincy":
        # Quincy plays: R, P, P, S, R (5-move cycle)
        quincy_cycle = ["R", "P", "P", "S", "R"]
        next_move = quincy_cycle[len(opponent_history) % 5]
        guess = counter[next_move]

    elif player.bot_type == "kris":
        # Kris plays: P, P, R, R, P, S, S, R, R, P (10-move cycle)
        kris_cycle = ["P", "P", "R", "R", "P", "S", "S", "R", "R", "P"]
        next_move = kris_cycle[len(opponent_history) % 10]
        guess = counter[next_move]

    elif player.bot_type == "abbey":
        # Abbey adapts to our last move, so play the move that beats Abbey's previous move
        if len(opponent_history) > 0:
            abbey_last = opponent_history[-1]
            guess = counter[abbey_last]
        else:
            guess = "R"

    elif player.bot_type == "mrugesh":
        # Against Mrugesh: Keep frequencies balanced
        if len(player.my_history) >= 5:
            my_counts = {"R": player.my_history.count("R"), 
                        "P": player.my_history.count("P"), 
                        "S": player.my_history.count("S")}
            # Play the least frequent move
            min_count = min(my_counts.values())
            options = [move for move, count in my_counts.items() if count == min_count]
            guess = random.choice(options) if options else "R"
        else:
            guess = random.choice(["R", "P", "S"])

    else:
        # Fallback: assume Quincy
        quincy_cycle = ["R", "P", "P", "S", "R"]
        next_move = quincy_cycle[len(opponent_history) % 5]
        guess = counter[next_move]

    # Record our move
    player.my_history.append(guess)
    return guess