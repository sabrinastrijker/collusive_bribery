# def restructure_list(numbers):
#     result_matrix = []
#     for i in range(0, len(numbers), 8):
#         block = numbers[i:i+8]
#         matrix_block = []
#         for j in range(0, 4, 2):
#             matrix_row = block[j:j+2] + block[j+4:j+6]
#             matrix_block.append(matrix_row)
#         result_matrix.extend(matrix_block)
#     return result_matrix

# numbers = list(range(1, 17))
# result = restructure_list(numbers)

# for row in result:
#     print(row)

########################################################################################
# # Define the function to restructure a list into a matrix
# def restructure_list(numbers):
#     result_matrix = []  # Initialize an empty list to store the resulting matrix
#     # Iterate over the input list in steps of 8
#     for i in range(0, len(numbers), 8):
#         block = numbers[i:i+8]  # Extract a block of 8 elements from the input list
#         matrix_block = []  # Initialize an empty list to store the matrix blocks
#         # Iterate over the block in steps of 2
#         for j in range(0, 4, 2):
#             # Extract two elements from the current position and two elements from position j+4
#             matrix_row = block[j:j+2] + block[j+4:j+6]
#             matrix_block.append(matrix_row)  # Append the row to the matrix block
#         result_matrix.extend(matrix_block)  # Extend the result matrix with the matrix block
#     return result_matrix

# # Define the input list of numbers
# numbers = list(range(1, 17))

# # Call the function to restructure the list into a matrix
# result = restructure_list(numbers)

# # Print each row of the resulting matrix
# for row in result:
#     print(row)
# ###########################################################################################################


# # Define the function to restructure a list into a matrix
# def restructure_list(numbers):
#     result_matrix = []  # Initialize an empty list to store the resulting matrix
#     # Iterate over the input list in steps of 8
#     for i in range(0, len(numbers), BLOCK_SIZE*2):
#         block = numbers[i:i+BLOCK_SIZE*2]  # Extract a block of elements from the input list
#         matrix_block = []  # Initialize an empty list to store the matrix blocks
#         # Iterate over the block in steps of 2
#         for j in range(0, BLOCK_SIZE, 2):
#             # Extract two elements from the current position and two elements from position j+HALF_BLOCK_SIZE
#             matrix_row = block[j:j+4] + block[j+HALF_BLOCK_SIZE:j+HALF_BLOCK_SIZE+4]
#             matrix_block.append(matrix_row)  # Append the row to the matrix block
#         result_matrix.extend(matrix_block)  # Extend the result matrix with the matrix block
#     return result_matrix

# # Define the start and end numbers for the input list
# START_NUMBER = 1
# END_NUMBER = 64



# # Define constants for the block size and half block size
# BLOCK_SIZE = 8
# HALF_BLOCK_SIZE = BLOCK_SIZE // 2

# # # Define the input list of numbers
# numbers = list(range(START_NUMBER, END_NUMBER + 1))


# # Call the function to restructure the list into a matrix
# result = restructure_list(numbers)
# print(result)
# Print each row of the resulting matrix
# for row in result:
#     print(row)

import math as mt

def maak_matrix(R, M):
    numbers = list(range(R**2*M))
    result_matrix = []
    sqrt = int(mt.sqrt(M))
    begin_getal = 0
    for i in range(R*sqrt):
        # Hij maakt hier het begingetal, dus het eerste getalletje in de lijst. Het probleem is alleen dat na R^2 moet ie weer resetten, dat doet ie niet goed
        #  dat moet nog gebouwd worden
        # if begin_getal % R = 0:

        if (i*R) % (R**2) == 0 and i != 0:
            begin_getal = i * R * sqrt +1 # Increment the starting number by R*M
        elif i == 0:
            begin_getal = 1
        else:
            begin_getal += R  # Increment the starting number by R
        # print(begin_getal)
        block = numbers[i:i+(R*M)]  # Extract a block of elements from the input list
        matrix_block = []
        # print(begin_getal)
        matrix_row = []
        values_list = []
        for j in range(sqrt):
            # ik heb nog geen manier gevonden om dynamisch de matrix rows aan elkaar te plakken. Het beginnetje is er want de eerste rij maakt ie 
            #  al bijna goed, hij gaat alleen maar tot " het goede aantal " - 1... 
            # hij zet nu soort van de getallen goed in de rijen, maar hij maakt lists in lists in plaats van een enkele lijst met alle getallen
            matrix_row_part =block[begin_getal+(j*R**2):begin_getal+(j*R**2)+R]
            matrix_row.append(matrix_row_part)
            for value in range(begin_getal + (j * R ** 2), begin_getal + (j * R ** 2) + R):
                values_list.append(value)  # Append each value to the list
        # print(values_list)
        matrix_block.append(values_list)
        # print(matrix_block)
        result_matrix.extend(matrix_block)
    return result_matrix

#result = maak_matrix(2, 9)
# print(result)
#for row in result:
    print(row)
    
#data = result

def get_neighbors_dict(data):

    # Function to get neighbors of a value in the list
    def get_neighbors(data, row, col):
        neighbors = []
        for r in range(max(0, row - 1), min(row + 2, len(data))):
            for c in range(max(0, col - 1), min(col + 2, len(data[0]))):
                if (r, c) != (row, col):
                    neighbors.append(data[r][c])
        return neighbors

    # Dictionary to store neighbors
    neighbor_dict = {}

    # Loop through the list and store neighbors in the dictionary
    for i, sublist in enumerate(data):
        for j, value in enumerate(sublist):
            neighbor_dict[value] = get_neighbors(data, i, j)

    return neighbor_dict

#print(get_neighbors_dict(data))