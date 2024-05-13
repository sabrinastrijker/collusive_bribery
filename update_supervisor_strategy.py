result = {1: {'average_payoff_neighbours_strat0': 16.0,
     'average_payoff_neighbours_strat1': 40.0,
     'supervisor_strategy': 1,
     'total_payoff_supervisor': 40},
 2: {'average_payoff_neighbours_strat0': 16.0,
     'average_payoff_neighbours_strat1': 40.0,
     'supervisor_strategy': 0,
     'total_payoff_supervisor': 16},
 3: {'average_payoff_neighbours_strat0': 16.0,
     'average_payoff_neighbours_strat1': 40.0,
     'supervisor_strategy': 1,
     'total_payoff_supervisor': 40},
 4: {'average_payoff_neighbours_strat0': 16.0,
     'average_payoff_neighbours_strat1': 40.0,
     'supervisor_strategy': 0,
     'total_payoff_supervisor': 16}}

import math
import numpy as np

def add_new_strategy_2(data):

    def transition_probability(pi_si, pi_sj):
        exp_term = math.exp((pi_si - pi_sj))
        probability = (1 + exp_term) **(-1)
        return probability

    def values_to_probabilities(values):
        # Convert values to numpy array
        arr = np.array(values)
        
        # Calculate the sum of all values
        total = np.sum(arr)
        
        # Calculate probabilities
        probabilities = np.divide(arr, total)
        
        return probabilities
        
    def get_range(random_number, result):
        if random_number < result[0]:
            return 0
        else:
            return 1

    for key, value in data.items():

        strategy = value['supervisor_strategy']
        strat_key = 'average_payoff_neighbours_strat{}'.format(strategy)

        list_result = []
        pi_1=value[strat_key]
        # print("p1:", pi_1)
        for i in range(2):

            strat_key_1 = 'average_payoff_neighbours_strat{}'.format(i)

            pi_2 = value[strat_key_1]
            # print(pi_2)

            result = transition_probability(pi_1,pi_2)
            


            
            list_result.append(result)

        result = values_to_probabilities(list_result)

        random_number = np.random.rand()
        # print(result)
        # Get the range
        result_range = get_range(random_number,result)

        # print(f"The random number {random_number} falls in the range: {result_range}")

        data[key]['new_strategy'] = result_range

       # pprint.pprint(result_range)

    return data
        
        
#result = add_new_strategy_2(result)

import pprint
#pprint.pprint(result)