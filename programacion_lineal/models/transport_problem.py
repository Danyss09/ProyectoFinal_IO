import numpy as np
from scipy.optimize import linprog

def solve_transport_problem(data):
    cost_matrix = np.array(data["costs"])
    supply = np.array(data["supply"])
    demand = np.array(data["demand"])

    num_sources, num_destinations = cost_matrix.shape
    c = cost_matrix.flatten()
    A_eq = []
    b_eq = []

    for i in range(num_sources):
        row = np.zeros(num_sources * num_destinations)
        row[i * num_destinations:(i + 1) * num_destinations] = 1
        A_eq.append(row)
        b_eq.append(supply[i])

    for j in range(num_destinations):
        row = np.zeros(num_sources * num_destinations)
        row[j::num_destinations] = 1
        A_eq.append(row)
        b_eq.append(demand[j])

    res = linprog(c, A_eq=A_eq, b_eq=b_eq, method="highs")
    return {"status": res.success, "objective_value": res.fun, "solution": res.x.reshape(num_sources, num_destinations).tolist()}
