import pulp

def solve_linear_problem(data):
    problem = pulp.LpProblem("Linear_Problem", pulp.LpMaximize if data["objective"] == "max" else pulp.LpMinimize)
    
    variables = {var: pulp.LpVariable(var, lowBound=0) for var in data["variables"]}
    problem += pulp.lpSum(data["objective_coeffs"][i] * variables[var] for i, var in enumerate(data["variables"])), "Objective"

    for constraint in data["constraints"]:
        lhs = pulp.lpSum(constraint["coeffs"][i] * variables[var] for i, var in enumerate(data["variables"]))
        if constraint["sign"] == "<=":
            problem += lhs <= constraint["rhs"]
        elif constraint["sign"] == ">=":
            problem += lhs >= constraint["rhs"]
        elif constraint["sign"] == "=":
            problem += lhs == constraint["rhs"]

    problem.solve()
    return {"status": pulp.LpStatus[problem.status], "objective_value": pulp.value(problem.objective),
            "variable_values": {var: pulp.value(variables[var]) for var in data["variables"]}}
