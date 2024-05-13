

# def update_information(big_dict):
#     # Perform the necessary updates on big_dict
#     # For example, let's say you want to add a new key 'new_key' with value 'new_value' to each entry
#     for key, value in big_dict.items():
#         value['new_key'] = 'new_value'
    
#     # Return the updated big_dict
#     return big_dict



#corupt rule enforcers = 1
#honest rule enforcer = 0
#cautios participant = 1
#trusting participant = 2
#defecting articipant = 3


# payoffs
b = 1
C0 = 2
a = 3
c = 4
f = 5
B=6



def calculate_participant_payoff(matrices):
    data = matrices

    for key, value in data.items():
        supervisor_state = value['supervisor_state']
        strategy = value['strategy']
        match_strategy = value['match_strategy']

        if supervisor_state == 0:
            if strategy == 1:
                if match_strategy == 1:
                    data[key]['participant_payoff'] = (b-C0-a)
                elif match_strategy == 2:
                    data[key]['participant_payoff'] = (b-C0-a)
                elif match_strategy == 3:
                    data[key]['participant_payoff'] = (-c+f/2-C0-a)
            elif strategy == 2:
                if match_strategy == 1:
                    data[key]['participant_payoff'] = (b-C0)
                elif match_strategy == 2:
                    data[key]['participant_payoff'] = (b-C0)
                elif match_strategy == 3:
                    data[key]['participant_payoff'] = (-c+f/2-C0)
            elif strategy == 3:
                if match_strategy == 1:
                    data[key]['participant_payoff'] = (b+c-C0-f)
                elif match_strategy == 2:
                    data[key]['participant_payoff'] = (b+c-C0-f)
                elif match_strategy == 3:
                    data[key]['participant_payoff'] = (-C0-f)
        elif supervisor_state == 1:
            if strategy == 1:
                if match_strategy == 1:
                    data[key]['participant_payoff'] = (b-C0-a)
                elif match_strategy == 2:
                    data[key]['participant_payoff'] = (b-C0-a)
                elif match_strategy == 3:
                    data[key]['participant_payoff'] = (-c+f/2)
            elif strategy == 2:
                if match_strategy == 1:
                    data[key]['participant_payoff'] = (b-C0)
                elif match_strategy == 2:
                    data[key]['participant_payoff'] = (b-C0)
                elif match_strategy == 3:
                    data[key]['participant_payoff'] = (-c-C0)
            elif strategy == 3:
                if match_strategy == 1:
                    data[key]['participant_payoff'] = (b+c-C0-f-B)
                elif match_strategy == 2:
                    data[key]['participant_payoff'] = (b+c-C0-B)
                elif match_strategy == 3:
                    data[key]['participant_payoff'] = (-C0-B)

    return data




def calculate_rule_enforcer_payoff(matrices):
    data = matrices

    for key, value in data.items():
        supervisor_state = value['supervisor_state']
        strategy = value['strategy']
        match_strategy = value['match_strategy']

        if supervisor_state == 0:
            data[key]['supervisor_payoff'] = (2*C0)
        elif supervisor_state == 1:
            if strategy == 1:
                if match_strategy == 1:
                    data[key]['supervisor_payoff'] = (2*C0)
                elif match_strategy == 2:
                    data[key]['supervisor_payoff'] = (2*C0)
                elif match_strategy == 3:
                    data[key]['supervisor_payoff'] = (C0+B-a)
            elif strategy == 2:
                if match_strategy == 1:
                    data[key]['supervisor_payoff'] = (2*C0)
                elif match_strategy == 2:
                    data[key]['supervisor_payoff'] = (2*C0)
                elif match_strategy == 3:
                    data[key]['supervisor_payoff'] = (2*C0+B)
            elif strategy == 3:
                if match_strategy == 1:
                    data[key]['supervisor_payoff'] = (2*C0)
                elif match_strategy == 2:
                    data[key]['supervisor_payoff'] = (2*C0)
                elif match_strategy == 3:
                    data[key]['supervisor_payoff'] = (2*C0+2*B)

    return data


def reindex_dictionary(matrices):
    new_dict = {}
    counter = 1
    for key in matrices:
        new_dict[counter] = matrices[key]
        counter += 1
    return new_dict
