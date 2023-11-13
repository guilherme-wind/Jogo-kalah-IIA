def calculate_player_opponent_scores_44(state, player):
    player_score = state[state.SOUTH_SCORE_PIT] if player == 0 else state[state.NORTH_SCORE_PIT]
    opponent_score = state[state.NORTH_SCORE_PIT] if player == 0 else state[state.SOUTH_SCORE_PIT]
    return player_score, opponent_score

def calculate_score_difference_44(state, player):
    player_score, opponent_score = calculate_player_opponent_scores_44(state, player)
    return player_score - opponent_score

def calculate_progress_44(state, player):
    player_score, opponent_score = calculate_player_opponent_scores_44(state, player)
    total_seeds = sum(state[:state.NORTH_SCORE_PIT])
    return 2 * (player_score - opponent_score) / total_seeds

def calculate_seeds_difference_44(state, player):
    player_pits = state[:state.SOUTH_SCORE_PIT] if player == 0 else state[state.SOUTH_SCORE_PIT:state.NORTH_SCORE_PIT]
    opponent_pits = state[state.SOUTH_SCORE_PIT:state.NORTH_SCORE_PIT] if player == 0 else state[:state.SOUTH_SCORE_PIT]
    return sum(player_pits) - sum(opponent_pits)

def calculate_pits_difference_44(state, player):
    player_pits = state[:state.SOUTH_SCORE_PIT] if player == 0 else state[state.SOUTH_SCORE_PIT:state.NORTH_SCORE_PIT]
    opponent_pits = state[state.SOUTH_SCORE_PIT:state.NORTH_SCORE_PIT] if player == 0 else state[:state.SOUTH_SCORE_PIT]

    player_pit_values = [min(pit, 6) for pit in player_pits]
    opponent_pit_values = [min(pit, 6) for pit in opponent_pits]

    return sum(opponent_pit_values) - sum(player_pit_values)

def calculate_opponent_capture_penalty_44(state, player):
    next_states = [state.real_move(move) for move in state.get_legal_moves()]
    opponent_capture_penalty = sum((sum(s[:state.SOUTH_SCORE_PIT]) - sum(s[state.SOUTH_SCORE_PIT:state.NORTH_SCORE_PIT])) * 0.05 for s in next_states)
    return opponent_capture_penalty

def func_44(state, player):
    SCORE_WEIGHT = 4
    SEEDS_WEIGHT = 1
    PROGRESS_WEIGHT = 2
    PITS_WEIGHT = 3

    evaluation = (
        SCORE_WEIGHT * calculate_score_difference_44(state, player) +
        SEEDS_WEIGHT * calculate_seeds_difference_44(state, player) +
        PROGRESS_WEIGHT * calculate_progress_44(state, player) +
        PITS_WEIGHT * calculate_pits_difference_44(state, player) -
        calculate_opponent_capture_penalty_44(state, player)
    )

    return evaluation
