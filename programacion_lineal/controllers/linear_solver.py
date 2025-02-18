from flask import Blueprint, request, render_template,jsonify
from models.linear_program import solve_linear_problem
from utils.validations import validate_linear_problem
from utils.sensitivity_analysis import analyze_sensitivity

linear_solver_bp = Blueprint('linear_solver', __name__)

@linear_solver_bp.route('/solve_linear', methods=['POST'])
def solve_linear():
    data = request.json  # Obtenemos los datos enviados desde el formulario
    
    errors = validate_linear_problem(data)
    if errors:
        return jsonify({"error": errors}), 400
    
    solution = solve_linear_problem(data)
    sensitivity = analyze_sensitivity(data, solution)

    # Pasamos la solución y el análisis de sensibilidad al template
   # return render_template('index.html', solution=solution, sensitivity=sensitivity)

    return jsonify({"solution": solution, "sensitivity": sensitivity})
