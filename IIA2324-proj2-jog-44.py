def calculate_score_difference_44(estado, jogador):
    player_score = estado.state[estado.SOUTH_SCORE_PIT] if jogador == 0 else estado.state[estado.NORTH_SCORE_PIT]
    opponent_score = estado.state[estado.NORTH_SCORE_PIT] if jogador == 0 else estado.state[estado.SOUTH_SCORE_PIT]
    return player_score - opponent_score

def calculate_seeds_difference_44(estado, jogador):
    player_pits = estado.state[:estado.SOUTH_SCORE_PIT] if jogador == 0 else estado.state[estado.SOUTH_SCORE_PIT:estado.NORTH_SCORE_PIT]
    opponent_pits = estado.state[estado.SOUTH_SCORE_PIT:estado.NORTH_SCORE_PIT] if jogador == 0 else estado.state[:estado.SOUTH_SCORE_PIT]
    return sum(player_pits) - sum(opponent_pits)

def calculate_progress_44(estado, jogador):
    player_score = estado.state[estado.SOUTH_SCORE_PIT] if jogador == 0 else estado.state[estado.NORTH_SCORE_PIT]
    opponent_score = estado.state[estado.NORTH_SCORE_PIT] if jogador == 0 else estado.state[estado.SOUTH_SCORE_PIT]
    total_seeds = sum(estado.state[:estado.NORTH_SCORE_PIT])
    return 2 * (player_score - opponent_score) / total_seeds

def calculate_pits_difference_44(estado, jogador):
    player_pits = estado.state[:estado.SOUTH_SCORE_PIT] if jogador == 0 else estado.state[estado.SOUTH_SCORE_PIT:estado.NORTH_SCORE_PIT]
    opponent_pits = estado.state[estado.SOUTH_SCORE_PIT:estado.NORTH_SCORE_PIT] if jogador == 0 else estado.state[:estado.SOUTH_SCORE_PIT]
    
    player_pit_values = [min(pit, 6) for pit in player_pits]
    opponent_pit_values = [min(pit, 6) for pit in opponent_pits]
    
    return sum(opponent_pit_values) - sum(player_pit_values)

def calculate_opponent_capture_penalty_44(estado, jogador):
    next_states = [estado.real_move(move) for move in estado.get_legal_moves()]
    opponent_capture_penalty = 0
    
    for state in next_states:
        south_pieces = sum(state.state[:state.SOUTH_SCORE_PIT])
        north_pieces = sum(state.state[state.SOUTH_SCORE_PIT:state.NORTH_SCORE_PIT])
        opponent_capture_penalty += (south_pieces - north_pieces) * 0.05
    
    return opponent_capture_penalty

def func_44(estado, jogador):
    SCORE_WEIGHT = 4
    SEEDS_WEIGHT = 1
    PROGRESS_WEIGHT = 2
    PITS_WEIGHT = 3

    evaluation = (
        SCORE_WEIGHT * calculate_score_difference_44(estado, jogador) +
        SEEDS_WEIGHT * calculate_seeds_difference_44(estado, jogador) +
        PROGRESS_WEIGHT * calculate_progress_44(estado, jogador) +
        PITS_WEIGHT * calculate_pits_difference_44(estado, jogador) -
        calculate_opponent_capture_penalty_44(estado, jogador)
    )

    return evaluation
