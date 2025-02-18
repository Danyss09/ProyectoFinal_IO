import networkx as nx

def solve_network_problem(data):
    G = nx.DiGraph()

    # Agregar las aristas al grafo
    for edge in data["edges"]:
        G.add_edge(edge["from"], edge["to"], capacity=edge["capacity"], weight=edge["cost"])

    # Imprimir el grafo para verificar las aristas y sus atributos
    print("Grafo creado:", G.edges(data=True))  # Imprimir las aristas y sus atributos (capacidad y costo)

    # Resolver el problema de flujo mínimo de costo
    flow_cost, flow_dict = nx.network_simplex(G)

    # Devolver el costo total y los flujos
    return {"total_cost": flow_cost, "flows": flow_dict}
