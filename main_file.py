import pprint

from matrix_generator import generate_matrix # type: ignore
from algorithm4 import get_match_dict # type: ignore
from payoff_functions_participants import calculate_participant_payoff, calculate_rule_enforcer_payoff,reindex_dictionary #type: ignore
from restructure_matrix import maak_matrix, get_neighbors_dict #type: ignore
from test import overview #type: ignore
from new_choice_calculation import add_new_strategy #type: ignore
from payoff_rule_enforcer import calculate_total_payoff, get_neighbors_dict_1, create_number_grid #type: ignore
from supervisor_neighbour_calculation import overview_1 #type: ignore
from update_supervisor_strategy import add_new_strategy_2 #type: ignore
from combine_new_strategy_supervisor import create_final_dict #type: ignore
from reset_game import update_strategies_and_states #type: ignore

# Get the match dictionary from algorithm2.py

def generate_matrices(M, R):
    matrices = []
    big_dict = {}  # Define big_dict as a dictionary instead of a list
    current_participant = 1
    participant_id = 1  # Initialize participant ID for each matrix

    for index in range(M):
        match_dict = get_match_dict(R)
        match_dict = filter_values(match_dict)

        gen_matrix = generate_matrix(participant_id, index + 1, R)

        for key, value in match_dict.items():
            gen_matrix[key]['match_id'] = value

        original_dict = gen_matrix

        updated_dict = {}

        for key, value in original_dict.items():
            participant_id = value.pop('participant_id')
            value['participant_location'] = key
            updated_dict[participant_id] = value

        data = updated_dict

        # Create a dictionary to map match_id to strategy
        match_strategy_map = {}
        for participant_id, participant_data in data.items():
            match_id = participant_data['match_id'][0]  # Assuming match_id contains only one tuple
            for match_participant_id, match_participant_data in data.items():
                if match_participant_data['participant_location'] == match_id:
                    match_strategy_map[match_id] = match_participant_data['strategy']
                    break  # Stop searching once a match is found

        # Update 'match_strategy' based on 'match_id'
        for participant_id, participant_data in data.items():
            match_id = participant_data['match_id'][0]  # Assuming match_id contains only one tuple
            participant_data['match_strategy'] = match_strategy_map.get(match_id, None)

        # Merge data into big_dict
        big_dict.update(data)

        # Increment participant ID for each matrix
        participant_id += R * R

    return big_dict

def filter_values(dictionary):
    filtered_dict = {}
    for key, values in dictionary.items():
        filtered_values = [value[1] if value[0] == key else value[0] for value in values]
        filtered_dict[key] = filtered_values
    return filtered_dict

def combineer():
    pass

def main():
    while True:
        M = int(input("Enter the number of rule enforcers (M): "))
        if M in [4, 9, 16, 25, 36]:
            break
        else:
            print("Invalid input. Please enter one of the allowed numbers: 4, 9, 16, 25, 36.")

    #M = int(input("Enter the number of rule enforcers (M): "))
    R = int(input("Enter the participant rate (2X2, 4X4, or 6X6): "))
    matrices = generate_matrices(M, R)
    matrix_including_participant_payoff = calculate_participant_payoff(matrices)
    matrix_including_payoff = calculate_rule_enforcer_payoff(matrices)
    reindexed_matrix= reindex_dictionary(matrices)
    maak_matrix_functie = maak_matrix(M,R)
    pprint.pprint(maak_matrix_functie)
    find_neighbour_value = get_neighbors_dict(maak_matrix_functie)
    pprint.pprint(find_neighbour_value)
    everything = overview(reindexed_matrix,find_neighbour_value)


    with_new_strategy = add_new_strategy(everything)

    new_dict_with_payoff_supervisor = calculate_total_payoff(everything)
    create_grid_for_supervisor = create_number_grid(M)
    make_neighbour_dict_for_supervisor = get_neighbors_dict_1(create_grid_for_supervisor)

    average_payoff_per_strategy_for_supervisor = overview_1(new_dict_with_payoff_supervisor,make_neighbour_dict_for_supervisor)

    #pprint.pprint(average_payoff_per_strategy_for_supervisor)
    print("########################")
    found_updated_supervisor_strategy = add_new_strategy_2(average_payoff_per_strategy_for_supervisor)

    final_dictionary = create_final_dict(found_updated_supervisor_strategy,with_new_strategy)

    resetted_game_dict = update_strategies_and_states(final_dictionary)


    # pprint.pprint(matrices)
    #pprint.pprint(reindexed_matrix)
   # pprint.pprint(find_neighbour_value)
    
    pprint.pprint(resetted_game_dict)


if __name__ == "__main__":
    main()
