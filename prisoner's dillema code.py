import numpy as np
import random
import matplotlib.pyplot as plt

class cell:
    B = 0
    Pb = ["", 0]
    Ps = ["", 0]
    R = ["D", 24]
    M = ["", 0]

    # def __init__():
    #     pass

def PD(i, j):
    if i == "D" and j == "D":
        return 1, 1
    elif i == "D" and j == "C":
        return 3, 0
    elif i == "C" and j == "D":
        return 0, 3
    elif i == "C" and j == "C":
        return 2, 2
    
def play():
    play_coop = 1
    play_def = 1
    for i in range(40):
        for j in range(40):
            point_counter = 0
            defect_prob = 0
            cooperate_prob = 0
            if counter == 0:
                # defect_prob = (40*40)/2
                # cooperate_prob = defect_prob - 1
                defect_probablity = alpha
                cooperate_probablity = 1 - alpha
                answer_i = random.choices(["C", "D"], weights=[cooperate_probablity, defect_probablity])
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if x == 0 and y == 0:
                            continue
                        if i + x > 39:
                            x = -39
                        if j + y > 39:
                            y = -39
                        answer_j = random.choices(["C", "D"], weights=[cooperate_probablity, defect_probablity])
                        point_i, point_j = PD(answer_i[0], answer_j[0])
                        point_counter += point_i
                        # print(f"i: {i}, j: {j}, x: {x}, y: {y}")
                        # print(f"dtype: {type(temp_grid[i + x][j + y])}")
                        temp_grid[i + x][j + y].B += point_j
                temp_grid[i][j].B += point_counter
                if point_counter > temp_grid[i][j].Pb[1]:
                    temp_grid[i][j].Pb = [answer_i, point_counter]
                temp_grid[i][j].M = [answer_i, point_counter]

            else:
                defect_prob += temp_grid[i][j].R[1]
                if temp_grid[i][j].Pb[0] == "D":
                    defect_prob += temp_grid[i][j].Pb[1]
                else:
                    cooperate_prob += temp_grid[i][j].Pb[1]
                if temp_grid[i][j].Ps[0] == "D":
                    defect_prob += temp_grid[i][j].Ps[1]
                else:
                    cooperate_prob += temp_grid[i][j].Ps[1]
                if temp_grid[i][j].M[0] == "D":
                    defect_prob += temp_grid[i][j].M[1]
                else:
                    cooperate_prob += temp_grid[i][j].M[1]
                defect_probablity = defect_prob/(defect_prob + cooperate_prob)
                cooperate_probablity = cooperate_prob/(defect_prob + cooperate_prob)
                # print(f"defect_probability: {defect_probablity}, cooperate_probability: {cooperate_probablity}")
                answer_i = random.choices(["C", "D"], weights=[cooperate_probablity, defect_probablity])
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        defect_prob_j = 0
                        cooperate_prob_j = 0
                        if x == 0 and y == 0:
                            continue
                        if i + x > 39:
                            x = -39
                        if j + y > 39:
                            y = -39

                        defect_prob_j += temp_grid[i + x][j + y].R[1]
                        if temp_grid[i + x][j + y].Pb[0] == "D":
                            defect_prob_j += temp_grid[i + x][j + y].Pb[1]
                        else:
                            cooperate_prob_j += temp_grid[i + x][j + y].Pb[1]
                        if temp_grid[i + x][j + y].Ps[0] == "D":
                            defect_prob_j += temp_grid[i + x][j + y].Ps[1]
                        else:
                            cooperate_prob_j += temp_grid[i + x][j + y].Ps[1]
                        if temp_grid[i + x][j + y].M[0] == "D":
                            defect_prob_j += temp_grid[i + x][j + y].M[1]
                        else:
                            cooperate_prob_j += temp_grid[i + x][j + y].M[1]
                        defect_probablity_j = defect_prob_j/(defect_prob_j + cooperate_prob_j)
                        cooperate_probablity_j = cooperate_prob_j/(defect_prob_j + cooperate_prob_j)
                        answer_j = random.choices(["C", "D"], weights=[cooperate_probablity_j, defect_probablity_j])
                        point_i, point_j = PD(answer_i[0], answer_j[0])
                        point_counter += point_i
                        # print(f"i: {i}, j: {j}, x: {x}, y: {y}")
                        # print(f"dtype: {type(temp_grid[i + x][j + y])}")
                        temp_grid[i + x][j + y].B += point_j
                temp_grid[i][j].B += point_counter
                if point_counter > temp_grid[i][j].Pb[1]:
                    temp_grid[i][j].Pb = [answer_i, point_counter]
                temp_grid[i][j].M = [answer_i, point_counter]
                
    for i in range(40):
        for j in range(40):
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if i + x > 39:
                        x = -39
                    if j + y > 39:
                        y = -39
                    neighbors = []
                    neighbors_best_points = []
                    neighbors.append(temp_grid[i + x][j + y].Pb)
                    neighbors_best_points.append(temp_grid[i + x][j + y].Pb[1])
            best_neighbors_index = neighbors_best_points.index(max(neighbors_best_points))
            temp_grid[i][j].Ps = neighbors[best_neighbors_index]
    for i in range(40):
        for j in range(40):
            if temp_grid[i][j].M[0] == ["C"]:
                play_coop += 1
            elif temp_grid[i][j].M[0] == ["D"]:
                play_def += 1
    # print(f"play_coop: {play_coop}, play_def: {play_def}")
    play_cooperate = play_coop/(play_coop + play_def)
    play_defect = play_def/(play_coop + play_def)
    return temp_grid, play_cooperate, play_defect

counter = 0

grid = np.empty((40,40), dtype=cell)
for i in range(40):
    for j in range(40):
        grid[i][j] = cell()

temp_grid = np.empty((40,40), dtype=cell)
for i in range(40):
    for j in range(40):
        temp_grid[i][j] = cell()

alpha = 1.0
cooperate_list = []
defect_list = []

iterations = 500
for i in range(iterations):
    grid, cooperate, defect = play()
    counter += 1
    cooperate_list.append(cooperate)
    defect_list.append(defect)
    temp_grid = grid
    if i % 10 == 0:
        print(f"i: {i}")
    # print(f"i: {i}")

sum_budget = 0
for i in range(40):
    for j in range(40):
        print(f"i: {i}, j: {j}, B: {grid[i][j].B}, Pb: {grid[i][j].Pb}, Ps: {grid[i][j].Ps}, R: {grid[i][j].R}, M: {grid[i][j].M}")
        sum_budget += grid[i][j].B
print(f"average budget: {sum_budget/(40*40)}")

probs = np.linspace(0.0, 1.0, iterations)
plt.plot(probs, cooperate_list, color='orange', label="Cooperate")
plt.plot(probs, defect_list, color='blue', label="Defect")
plt.ylabel("Probability")
plt.xlabel("Choice")
plt.title(f"alpha = {alpha}")
plt.legend()
plt.show()