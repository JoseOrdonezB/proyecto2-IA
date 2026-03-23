import sys

from utils.load_data import load_maze
from experiments.runner import run_algorithm, print_results
from experiments.simulator import run_simulation
from experiments.metrics import compare_algorithms, print_comparison

def choose_algorithm():
    algorithms = [
        "BFS",
        "DFS",
        "GBFS (Manhattan)",
        "GBFS (Euclidiana)",
        "A* (Manhattan)",
        "A* (Euclidiana)"
    ]

    print("\nAlgoritmos disponibles:")
    for i, alg in enumerate(algorithms, 1):
        print(f"{i}. {alg}")

    choice = input("Elige un algoritmo a ejecutar (número o nombre): ").strip()

    # Selección por número
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(algorithms):
            return algorithms[idx]
        else:
            print("Opción inválida, se ejecutará BFS por defecto")
            return "BFS"

    # Selección por nombre
    if choice in algorithms:
        return choice

    print("Algoritmo no reconocido, se ejecutará BFS por defecto")
    return "BFS"


def run_single_maze(file_path, algorithm_name):
    print("\n=========== MODO MANUAL ===========")

    maze, start, goals = load_maze(file_path)

    print(f"\nInicio: {start}")
    print(f"Metas: {goals}")

    results = run_algorithm(algorithm_name, maze, start, goals)
    print_results(results)


def run_experiments(file_path, algorithm_name, n_simulations=10):
    print("\n=========== MODO SIMULACIÓN ===========")

    maze, _, goals = load_maze(file_path)

    # En la simulación, pasar solo el algoritmo seleccionado
    sim_results = run_simulation(
        maze, goals, n_starts=n_simulations, algorithm_name=algorithm_name
    )

    comparison = compare_algorithms(sim_results)
    print_comparison(comparison)


def main():
    file_path = sys.argv[1] if len(sys.argv) > 1 else "./data/test_maze.txt"

    algorithm_name = choose_algorithm()

    # Ejecutar modo manual
    run_single_maze(file_path, algorithm_name)

    # Ejecutar simulación desde múltiples puntos
    run_experiments(file_path, algorithm_name, n_simulations=10)


if __name__ == "__main__":
    main()