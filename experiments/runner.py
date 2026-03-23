from algorithms.bfs import breadth_first_search
from algorithms.dfs import depth_first_search
from algorithms.gbfs import greedy_best_first_search
from algorithms.astar import a_star_search
from utils.heuristics import manhattan, euclidean

def run_all_algorithms(maze, start, goals):
    results = {}

    # 🔹 BFS
    results["BFS"] = breadth_first_search(maze, start, goals)

    # 🔹 DFS
    results["DFS"] = depth_first_search(maze, start, goals)

    # 🔹 GBFS
    results["GBFS (Manhattan)"] = greedy_best_first_search(
        maze, start, goals, manhattan
    )

    results["GBFS (Euclidiana)"] = greedy_best_first_search(
        maze, start, goals, euclidean
    )

    # 🔹 A*
    results["A* (Manhattan)"] = a_star_search(
        maze, start, goals, manhattan
    )

    results["A* (Euclidiana)"] = a_star_search(
        maze, start, goals, euclidean
    )

    return results

# runner.py (extensión)
def run_algorithm(algorithm_name, maze, start, goals):
    """
    Ejecuta solo el algoritmo seleccionado y devuelve el resultado.
    """
    results = {}

    if algorithm_name == "BFS":
        results["BFS"] = breadth_first_search(maze, start, goals)

    elif algorithm_name == "DFS":
        results["DFS"] = depth_first_search(maze, start, goals)

    elif algorithm_name == "GBFS (Manhattan)":
        results["GBFS (Manhattan)"] = greedy_best_first_search(
            maze, start, goals, manhattan
        )

    elif algorithm_name == "GBFS (Euclidiana)":
        results["GBFS (Euclidiana)"] = greedy_best_first_search(
            maze, start, goals, euclidean
        )

    elif algorithm_name == "A* (Manhattan)":
        results["A* (Manhattan)"] = a_star_search(
            maze, start, goals, manhattan
        )

    elif algorithm_name == "A* (Euclidiana)":
        results["A* (Euclidiana)"] = a_star_search(
            maze, start, goals, euclidean
        )

    else:
        raise ValueError(f"Algoritmo {algorithm_name} no reconocido")

    return results

def print_results(results):
    print("\n================ RESULTADOS ================\n")

    for name, result in results.items():
        print(f"--- {name} ---")

        if result["path"] is None:
            print("No se encontró solución.\n")
            continue

        print(f"Longitud del camino: {result['cost']}")
        print(f"Nodos explorados: {result['nodes_explored']}")
        print(f"Tiempo: {result['time']:.6f} segundos")

        if "branching_factor" in result:
            print(f"Branching factor: {result['branching_factor']:.4f}")

        print()