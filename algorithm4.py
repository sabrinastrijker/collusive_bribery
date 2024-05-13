import random
import sys

def get_match_dict(R):
    N = int(R)

    def get_empty_grid():
        grid = dict()
        for i in range(N):
            for j in range(N):
                grid[(i, j)] = "_"
        return grid

    def is_correct_grid(grid):
        if "_" in grid.values():
            return False

        for i in range(N):
            row = [grid[(i, j)] for j in range(N)]
            while len(row) > 0:
                if row[0] == "H":
                    if len(row) == 1:
                        return False
                    first, second = row[:2]
                    row = row[2:]
                    if second == "V":
                        return False
                else:
                    row = row[1:]
                    
        for j in range(N):
            col = [grid[(i, j)] for i in range(N)]
            while len(col) > 0:
                if col[0] == "V":
                    if len(col) == 1:
                        return False
                    first, second = col[:2]
                    col = col[2:]
                    if second == "H":
                        return False
                else:
                    col = col[1:]
        return True

    def get_filled_grid():
        grid = get_empty_grid()
        match_dict = dict()  # Dictionary to store matches per location
        for i in range(N): 
            for j in range(N):
                if grid[(i, j)]  == "_":
                    next_row_str = ""
                    if i == N - 2:
                        for k in range(j):
                            next_row_str += grid[(N - 1, k)]

                    if i == N - 1: # last row, must be horizontal
                        if grid[(i, j + 1)] != "_":
                            return match_dict
                        grid[(i, j)], grid[(i, j + 1)] = "H", "H"
                        match_dict.setdefault((i, j), []).append(((i, j), (i, j + 1)))  # Store match in dictionary
                        match_dict.setdefault((i, j + 1), []).append(((i, j), (i, j + 1)))  # Store match in dictionary
                    elif j == N - 1: # last column, must be vertical
                        if grid[(i + 1, j)] != "_":
                            return match_dict
                        grid[(i, j)], grid[(i + 1, j)] = "V", "V"
                        match_dict.setdefault((i, j), []).append(((i, j), (i + 1, j)))  # Store match in dictionary
                        match_dict.setdefault((i + 1, j), []).append(((i, j), (i + 1, j)))  # Store match in dictionary
                    elif grid[(i, j + 1)] != "_": # right filled, must be vertical
                        if grid[(i + 1, j)] != "_":
                            return match_dict
                        grid[(i, j)] , grid[(i + 1, j)] = "V", "V"
                        match_dict.setdefault((i, j), []).append(((i, j), (i + 1, j)))  # Store match in dictionary
                        match_dict.setdefault((i + 1, j), []).append(((i, j), (i + 1, j)))  # Store match in dictionary
                    elif next_row_str != "" and next_row_str.count("_") % 2 == 1: # odd empty spots to the left if you go vertical now
                        grid[(i, j)] , grid[(i, j + 1)] = "H", "H"
                        match_dict.setdefault((i, j), []).append(((i, j), (i, j + 1)))  # Store match in dictionary
                        match_dict.setdefault((i, j + 1), []).append(((i, j), (i, j + 1)))  # Store match in dictionary
                    elif grid[(i + 1, j)] != "_": # below filled, must be horizontal (SHOULD NOT HAPPEN?!)
                        raise Exception("This should not happen because you iterate over i and then j?")
                    else:
                        ch = "H" if random.random() < 0.5 else "V"
                        if ch == "H":
                            grid[(i, j)]  = ch
                            grid[(i, j + 1)] = ch
                            match_dict.setdefault((i, j), []).append(((i, j), (i, j + 1)))  # Store match in dictionary
                            match_dict.setdefault((i, j + 1), []).append(((i, j), (i, j + 1)))  # Store match in dictionary
                        else:
                            grid[(i, j)]  = ch
                            grid[(i + 1, j)] = ch
                            match_dict.setdefault((i, j), []).append(((i, j), (i + 1, j)))  # Store match in dictionary
                            match_dict.setdefault((i + 1, j), []).append(((i, j), (i + 1, j)))  # Store match in dictionary

        if is_correct_grid(grid):
            return match_dict
        else:
            return None

    return get_filled_grid()
