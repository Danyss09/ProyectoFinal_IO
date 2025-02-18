from flask import Blueprint, request, jsonify
from models.transport_problem import solve_transport_problem
from utils.validations import validate_transport_problem

transport_solver_bp = Blueprint('transport_solver', __name__)

@transport_solver_bp.route('/solve_transport', methods=['POST'])
def solve_transport():
    data = request.json

    errors = validate_transport_problem(data)
    if errors:
        return jsonify({"error": errors}), 400

    solution = solve_transport_problem(data)
    return jsonify({"solution": solution})
