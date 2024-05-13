data_values = {1: {'supervisor_strategy': 1, 'total_payoff_supervisor': 40},
 2: {'supervisor_strategy': 0, 'total_payoff_supervisor': 16},
 3: {'supervisor_strategy': 1, 'total_payoff_supervisor': 40},
 4: {'supervisor_strategy': 0, 'total_payoff_supervisor': 16}}



numbers_dict = {1: [2, 3, 4], 2: [1, 3, 4], 3: [1, 2, 4], 4: [1, 2, 3]}







def overview_1(data_values, numbers_dict):
    def calculate_average_payoff_per_strategy(extracted_values):
        payoffs_per_strategy = {}
        strategy_count = {}

        for item in extracted_values:
            strategy = item['supervisor_strategy']
            payoff = item['total_payoff_supervisor']
            if strategy in payoffs_per_strategy:
                payoffs_per_strategy[strategy] += payoff
                strategy_count[strategy] += 1
            else:
                payoffs_per_strategy[strategy] = payoff
                strategy_count[strategy] = 1

        average_payoff_per_strategy = {}
        for strategy, total_payoff in payoffs_per_strategy.items():
            count = strategy_count[strategy]
            average_payoff_per_strategy[strategy] = total_payoff / count

        return average_payoff_per_strategy

    # def extract_values_by_numbers(data_values, numbers_dict):
    #     extracted_values = []
    #     for key, value in numbers_dict.items():
    #         extracted_values.extend([data_values[num] for num in value if num in data_values])
    #     return extracted_values

    def extract_values_by_numbers_updated(data_values, numbers_dict_updated):
        extracted_values = []
        for value in numbers_dict_updated:
            # print(value)
            extracted_values.extend([data_values[num] for num in numbers_dict_updated if num in data_values])
        return extracted_values

    # Extract relevant values from data_values based on numbers_dict
    # extracted_values = extract_values_by_numbers(data_values, numbers_dict)

    # # Calculate average payoffs per strategy using the extracted values
    # average_payoff_per_strategy = calculate_average_payoff_per_strategy(extracted_values)

    # print(average_payoff_per_strategy)
    # print(numbers_dict.items())
    # pprint.pprint(extracted_values)

    # Update data_values with average payoffs for the first entry in numbers_dict

    for dict_key, dict_value in numbers_dict.items():
        # print(dict_value)
        extracted_values = extract_values_by_numbers_updated(data_values, dict_value)
        # pprint.pprint(extracted_values)
        average_payoff_per_strategy = calculate_average_payoff_per_strategy(extracted_values)
        # print(average_payoff_per_strategy)
        for key in dict_value:
            # print(key)

            strategy = data_values[key]['supervisor_strategy']
            avg_payoff = average_payoff_per_strategy[strategy]
            data_values[dict_key][f'average_payoff_neighbours_strat{strategy}'] = avg_payoff

    #pprint.pprint(data_values)

    return(data_values)

import pprint

result = overview_1(data_values, numbers_dict)
#pprint.pprint(result)