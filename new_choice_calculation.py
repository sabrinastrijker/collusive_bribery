

import pprint
import math
import numpy as np


def add_new_strategy(data):

    def transition_probability(pi_si, pi_sj):
        exp_term = math.exp((pi_si - pi_sj))
        probability = (1 + exp_term) **(-1)
        return probability
    # # A = None
    # # B = None
    # C = None

    def values_to_probabilities(values):
        # Convert values to numpy array
        arr = np.array(values)
        
        # Calculate the sum of all values
        total = np.sum(arr)
        
        # Calculate probabilities
        probabilities = np.divide(arr, total)
        
        return probabilities
        


    # def get_range(random_number,result):
    #     for row in result:
    #         for i in range(len(row)-1):
    #             if row[i] >= random_number < row[i+1]:
    #                 return f"Value falls in range {i}: [{row[i]}, {row[i+1]})"
    #             # elif row[i] <= random_number < row[i+1]:
    #             #     return f"Value falls in range {i}: [0, {row[i]})"
    #             # else:

    def get_range(random_number, result):
        if random_number < result[0]:
            return 1
        if random_number >= result[0] and random_number < result[1]:
            return 2
        else:
            return 3


        # for row in result:

        #     for i in range(len(row)-1):
        #         if row[i] <= random_number < row[i+1]:
        #             return f"Value falls in range {i+1}: [{row[i]}, {row[i+1]}]"
        #     if random_number >= row[-1]:  # Check if random_number is greater than or equal to the last value
        #         return f"Value falls in range {len(row)}: [{row[-1]}, 1.0]"
        # # If random number falls outside of all defined ranges
        # return f"Value falls in range {1}: [0, {row[0]}]"




    for key, value in data.items():

        strategy = value['strategy']
        strat_key = 'average_payoff_neighbours_strat{}'.format(strategy)

        list_result = []
        pi_1=value[strat_key]
        # print("p1:", pi_1)
        for i in range(3):

            strat_key_1 = 'average_payoff_neighbours_strat{}'.format(i+1)

            pi_2 = value[strat_key_1]
            # print(pi_2)

            result = transition_probability(pi_1,pi_2)
            


            
            list_result.append(result)

        result = values_to_probabilities(list_result)
        # result = np.array([result])
        # list_result = np.cumsum(result, axis=1)
        # print(list_result)

        # print(cumulative_probabilities)   

        # Generate a random number between 0 and 1
        random_number = np.random.rand()
        # print(result)
        # Get the range
        result_range = get_range(random_number,result)

        # print(f"The random number {random_number} falls in the range: {result_range}")

        data[key]['new_strategy'] = result_range

       # pprint.pprint(result_range)

    return data
        
    
        



    #transfer matrix:
    #Si = de payoff van de oude strategie
    # Sj = de payoff van swichen naar strat 2





    # result = transition_probability(4,2)
    # print(result)

    # # # Example usage:
    # # pi_si = 0.6  # Policy value for state Si
    # # pi_sj = 0.8  # Policy value for state Sj
    # # probability_2 = transition_probability(pi_si, pi_sj)
    # # print("Transition Probability:", probability_2)


    # # def new_choice():

    # #     #pak average payoff neighbours
    # #     # bereken de functie
    # #     # update de new strategy van de participants
    # #     pass



    # # #result = new_choice(data)
    # # #print(result)