from flask import Flask, request, jsonify,render_template
from controllers.linear_solver import linear_solver_bp
from controllers.transport_solver import transport_solver_bp
from controllers.network_solver import network_solver_bp
from models.linear_program import solve_linear_problem  # Importar la función que resuelve el problema lineal

app = Flask(__name__)

# Registrar Blueprints
app.register_blueprint(linear_solver_bp)
app.register_blueprint(transport_solver_bp)
app.register_blueprint(network_solver_bp)

@app.route('/')
def index():
    return render_template('index.html')
# Ruta para resolver el problema de programación lineal
@app.route('/solve_linear', methods=['POST'])
def solve_linear():
    data = request.get_json()  # Obtiene los datos enviados desde el frontend
    # Resolver el problema de programación lineal usando la función importada
    solution = solve_linear_problem(data)  # Llamar a la función que resuelve el problema
    print("Solution:", solution)  # Esto imprime los resultados en la consola

    # Enviar la respuesta como JSON
    return jsonify(solution)


if __name__ == '__main__':
    app.run(debug=True)
