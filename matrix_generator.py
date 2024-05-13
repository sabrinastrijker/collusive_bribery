import random


def generate_matrix(participant_id, supervisor_number, R):
    matrix = {}
    current_participant = 1
    supervisor_state = round(random.random())
    for i in range(R):
        for j in range(R):
            matrix[(i, j)] = {
                "participant_id": participant_id,
                "participant_location": None,
                "strategy": random.randint(1, 3),
                "participant_payoff": 0,
                "supervisor_number": supervisor_number,
                "supervisor_state": supervisor_state, 
                "supervisor_payoff": 0,
                "match_id": None,
                "match_strategy": None,
                "average_payoff_neighbours_strat1": 0,
                "average_payoff_neighbours_strat2": 0,
                "average_payoff_neighbours_strat3": 0,
                "new_strategy": None,

            }
            participant_id += 1  # Increment participant ID for each cell
        current_participant += R
    return matrix
