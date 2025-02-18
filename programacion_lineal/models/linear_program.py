import pulp
import re

def sanitize_variable_name(name):
    """Corrige los nombres de variables para que sean válidos en PuLP."""
    return re.sub(r'[^a-zA-Z0-9_]', '_', name)  # Reemplaza caracteres inválidos

def solve_linear_problem(data):
    method = data.get("method", "simplex")  # Método por defecto: Simplex

    # Crear problema de programación lineal
    problem = pulp.LpProblem("Linear_Problem", pulp.LpMaximize if data["objective"] == "max" else pulp.LpMinimize)

    # Definir variables de decisión con nombres corregidos
    variables = {var: pulp.LpVariable(sanitize_variable_name(var), lowBound=0) for var in data["variables"]}

    # Agregar función objetivo
    problem += pulp.lpSum(data["objective_coeffs"][i] * variables[var] for i, var in enumerate(data["variables"])), "Objective"

    # Agregar restricciones
    for constraint in data["constraints"]:
        lhs = pulp.lpSum(constraint["coeffs"][i] * variables[var] for i, var in enumerate(data["variables"]))
        if constraint["sign"] == "<=":
            problem += lhs <= constraint["rhs"]
        elif constraint["sign"] == ">=":
            problem += lhs >= constraint["rhs"]
        elif constraint["sign"] == "=":
            problem += lhs == constraint["rhs"]

    # Selección del solver
    solver = None

    if method in ["simplex", "two_phase", "big_m", "dual"]:
        solver = pulp.PULP_CBC_CMD(msg=False)  # No usamos path aquí

    # Resolver el problema
    problem.solve(solver)

    # Retornar resultados
    return {
        "status": pulp.LpStatus[problem.status],
        "objective_value": pulp.value(problem.objective),
        "variable_values": {var: pulp.value(variables[var]) for var in data["variables"]}
    }