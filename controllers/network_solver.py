from flask import Blueprint, request, jsonify
from models.network_flow import solve_network_problem

network_solver_bp = Blueprint('network_solver', __name__)

@network_solver_bp.route('/solve_network', methods=['POST'])
def solve_network():
    data = request.json
    solution = solve_network_problem(data)
    return jsonify({"solution": solution})
