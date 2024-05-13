
import pprint
#loop over je geaakte grid. 
# pak de omliggende dingen
#haal daar de dict waardes van op
# sum de juiste per catogorie
# update de dict waarden. 


# 1: 5
# 2: 7
# 3: -3


# Example dictionary
data_values = {
    1: {'average_payoff_neighbours_strat1': None,
     'average_payoff_neighbours_strat2': None,
     'average_payoff_neighbours_strat3': None,
     'match_id': [(0, 1)],
     'match_strategy': 2,
     'participant_location': (0, 0),
     'participant_payoff': -4,
     'strategy': 1,
     'supervisor_number': 1,
     'supervisor_payoff': 4,
     'supervisor_state': 0},
 2: {'average_payoff_neighbours_strat1': None,
     'average_payoff_neighbours_strat2': None,
     'average_payoff_neighbours_strat3': None,
     'match_id': [(0, 0)],
     'match_strategy': 1,
     'participant_location': (0, 1),
     'participant_payoff': -1,
     'strategy': 2,
     'supervisor_number': 1,
     'supervisor_payoff': 4,
     'supervisor_state': 0},
 3: {'average_payoff_neighbours_strat1': None,
     'average_payoff_neighbours_strat2': None,
     'average_payoff_neighbours_strat3': None,
     'match_id': [(1, 1)],
     'match_strategy': 3,
     'participant_location': (1, 0),
     'participant_payoff': -1,
     'strategy': 2,
     'supervisor_number': 1,
     'supervisor_payoff': 4,
     'supervisor_state': 0},
 4: {'average_payoff_neighbours_strat1': None,
     'average_payoff_neighbours_strat2': None,
     'average_payoff_neighbours_strat3': None,
     'match_id': [(1, 0)],
     'match_strategy': 2,
     'participant_location': (1, 1),
     'participant_payoff': -2,
     'strategy': 3,
     'supervisor_number': 1,
     'supervisor_payoff': 4,
     'supervisor_state': 0},
 5: {'average_payoff_neighbours_strat1': None,
     'average_payoff_neighbours_strat2': None,
     'average_payoff_neighbours_strat3': None,
     'match_id': [(0, 1)],
     'match_strategy': 1,
     'participant_location': (0, 0),
     'participant_payoff': -2,
     'strategy': 3,
     'supervisor_number': 2,
     'supervisor_payoff': 4,
     'supervisor_state': 0},
 6: {'average_payoff_neighbours_strat1': None,
     'average_payoff_neighbours_strat2': None,
     'average_payoff_neighbours_strat3': None,
     'match_id': [(0, 0)],
     'match_strategy': 3,
     'participant_location': (0, 1),
     'participant_payoff': -6.5,
     'strategy': 1,
     'supervisor_number': 2,
     'supervisor_payoff': 4,
     'supervisor_state': 0},
 7: {'average_payoff_neighbours_strat1': None,
     'average_payoff_neighbours_strat2': None,
     'average_payoff_neighbours_strat3': None,
     'match_id': [(1, 1)],
     'match_strategy': 2,
     'participant_location': (1, 0),
     'participant_payoff': -2,
     'strategy': 3,
     'supervisor_number': 2,
     'supervisor_payoff': 4,
     'supervisor_state': 0},
 8: {'average_payoff_neighbours_strat1': None,
     'average_payoff_neighbours_strat2': None,
     'average_payoff_neighbours_strat3': None,
     'match_id': [(1, 0)],
     'match_strategy': 3,
     'participant_location': (1, 1),
     'participant_payoff': -3.5,
     'strategy': 2,
     'supervisor_number': 2,
     'supervisor_payoff': 4,
     'supervisor_state': 0}
}

numbers_list = [2,3,4]
numbers_dict = {1: [2, 3, 4]}

numbers_dict = {1: [2, 3, 4],
    2: [1, 5, 3, 4, 7]}
#  3: [1, 2, 4, 9, 10],
#  4: [1, 2, 5, 3, 7, 9, 10, 13],
#  5: [2, 6, 4, 7, 8],
#  6: [5, 7, 8],
#  7: [2, 5, 6, 4, 8, 10, 13, 14],
#  8: [5, 6, 7, 13, 14],
#  9: [3, 4, 10, 11, 12],
#  10: [3, 4, 7, 9, 13, 11, 12, 15],
#  11: [9, 10, 12],
#  12: [9, 10, 13, 11, 15],
#  13: [4, 7, 8, 10, 14, 12, 15, 16],
#  14: [7, 8, 13, 15, 16],
#  15: [10, 13, 14, 12, 16],
#  16: [13, 14, 15]}

# def extract_values_by_numbers(data_values, numbers_list):
#     extracted_values = [data_values[num] for num in numbers_list if num in data_values]
#     return extracted_values

# def calculate_average_payoff_per_strategy(data_values):
#     # Dictionary to store sum of payoffs per strategy
#     payoffs_per_strategy = {}
#     # Dictionary to store count of occurrences per strategy
#     strategy_count = {}

#     # Iterate over each item in the dictionary
#     for item in data_values.values():
#         strategy = item['strategy']
#         payoff = item['participant_payoff']  # Or 'supervisor_payoff' if you want supervisor's payoff
#         # If the strategy is already in the dictionaries, add the payoff and count to its total
#         if strategy in payoffs_per_strategy:
#             payoffs_per_strategy[strategy] += payoff
#             strategy_count[strategy] += 1
#         else:
#             # Otherwise, initialize the total payoff and count for this strategy
#             payoffs_per_strategy[strategy] = payoff
#             strategy_count[strategy] = 1

#     # Calculate the average payoff per strategy

#     average_payoff_per_strategy = {}
#     for strategy, total_payoff in payoffs_per_strategy.items():
#         count = strategy_count[strategy]
#         average_payoff_per_strategy[strategy] = total_payoff / count

#     return average_payoff_per_strategy

# # Calculate average payoffs per strategy
# average_payoff_per_strategy = calculate_average_payoff_per_strategy(data_values)

# # Update data_values with average payoffs for the first entry in numbers_dict
# for dict_key, dict_value in numbers_dict.items():
#     print(dict_key)
#     print(dict_value)
#     #first_entry_key, first_entry_values = next(dict_value)
#     for key in dict_value:
#         strategy = data_values[key]['strategy']
#         avg_payoff = average_payoff_per_strategy[strategy]
#         data_values[dict_key][f'average_payoff_neighbours_strat{strategy}'] = avg_payoff

# pprint.pprint(data_values)

def extract_values_by_numbers(data_values, numbers_list):
    extracted_values = [data_values[num] for num in numbers_list if num in data_values]
    return extracted_values

result = extract_values_by_numbers(data_values, numbers_list)
pprint.pprint(result)

# Dictionary to store sum of payoffs per strategy
payoffs_per_strategy = {}
# Dictionary to store count of occurrences per strategy
strategy_count = {}

# Iterate over each item in the dictionary
for item in result:
    strategy = item['strategy']
    payoff = item['participant_payoff']  # Or 'supervisor_payoff' if you want supervisor's payoff
    # If the strategy is already in the dictionaries, add the payoff and count to its total
    if strategy in payoffs_per_strategy:
        payoffs_per_strategy[strategy] += payoff
        strategy_count[strategy] += 1
    # If the strategy is already in the dictionaries, add the payoff and count to its total
    if strategy in payoffs_per_strategy:
        payoffs_per_strategy[strategy] += payoff
        strategy_count[strategy] += 1
    # Otherwise, initialize the total payoff and count for this strategy
    else:
        payoffs_per_strategy[strategy] = payoff
        strategy_count[strategy] = 1

# Calculate the average payoff per strategy
average_payoff_per_strategy = {}
for strategy, total_payoff in payoffs_per_strategy.items():
    count = strategy_count[strategy]
    average_payoff_per_strategy[strategy] = total_payoff / count

print("Average payoff per strategy:", average_payoff_per_strategy)