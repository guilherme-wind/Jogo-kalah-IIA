from func_aux import *

def func_44(estado,jogador):
    # Define weights for different evaluation factors
    SCORE_WEIGHT = 1.0
    SEEDS_WEIGHT = 0.5
    PROGRESS_WEIGHT = 0.3
    PITS_WEIGHT = 0.2

    # Get the player's score and the opponent's score
    player_score = estado.state[estado.SOUTH_SCORE_PIT] if jogador == 0 else estado.state[estado.NORTH_SCORE_PIT]
    opponent_score = estado.state[estado.NORTH_SCORE_PIT] if jogador == 0 else estado.state[estado.SOUTH_SCORE_PIT]

    # Calculate the number of seeds in the player's pits and the opponent's pits
    player_pits = estado.state[:estado.SOUTH_SCORE_PIT] if jogador == 0 else estado.state[estado.SOUTH_SCORE_PIT:estado.NORTH_SCORE_PIT]
    opponent_pits = estado.state[estado.SOUTH_SCORE_PIT:estado.NORTH_SCORE_PIT] if jogador == 0 else estado.state[:estado.SOUTH_SCORE_PIT]

    # Calculate the difference in scores and seeds
    score_diff = player_score - opponent_score
    seeds_diff = sum(player_pits) - sum(opponent_pits)

    # Consider the game's progress by checking how close each player is to winning
    total_seeds = sum(player_pits) + sum(opponent_pits)
    progress = 2 * (player_score - opponent_score) / total_seeds

    # Encourage capturing opponent's pits and having fewer seeds in own pits
    player_pit_values = [min(pit, 6) for pit in player_pits]
    opponent_pit_values = [min(pit, 6) for pit in opponent_pits]
    pits_diff = sum(opponent_pit_values) - sum(player_pit_values)

    # Penalize moves that lead to the opponent capturing more seeds
    next_states = [estado.real_move(move) for move in estado.get_legal_moves()]
    opponent_capture_penalty = 0
    for state in next_states:
        south_pieces = sum(state.state[:state.SOUTH_SCORE_PIT])
        north_pieces = sum(state.state[state.SOUTH_SCORE_PIT:state.NORTH_SCORE_PIT])
        opponent_capture_penalty += (south_pieces - north_pieces) * 0.05


    # Calculate the final evaluation value
    evaluation = (
        SCORE_WEIGHT * score_diff +
        SEEDS_WEIGHT * seeds_diff +
        PROGRESS_WEIGHT * progress +
        PITS_WEIGHT * pits_diff -
        opponent_capture_penalty
    )

    return evaluation


def chapiteau_algorithm(estado, jogador):
    if estado.is_game_over():
        aux = estado.result()
        return aux*100 if jogador == estado.SOUTH else aux*-100
    
    player_pits = estado.state[:estado.SOUTH_SCORE_PIT] if jogador == 0 else estado.state[estado.SOUTH_SCORE_PIT:estado.NORTH_SCORE_PIT]
    opponent_pits = estado.state[estado.SOUTH_SCORE_PIT:estado.NORTH_SCORE_PIT] if jogador == 0 else estado.state[:estado.SOUTH_SCORE_PIT]
    return sum(player_pits) - sum(opponent_pits)


# ______________________________________________________________________________
# Testes


grupo44 = JogadorAlfaBeta('Grupo 44', 5, func_44)
chapiteau = JogadorAlfaBeta('Chapiteau', 5, chapiteau_algorithm)
jogo=Kalah(10)
print(jogaNpares(jogo,100,grupo44,chapiteau))