import random
from experiments.runner import run_all_algorithms, run_algorithm


def get_free_positions(maze):
    free_positions = []

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == '0':
                free_positions.append((i, j))

    return free_positions


def generate_random_starts(maze, n=10):
    free_positions = get_free_positions(maze)

    if n > len(free_positions):
        n = len(free_positions)

    return random.sample(free_positions, n)


def run_simulation(maze, goals, n_starts=10, algorithm_name=None):
    """
    Ejecuta simulaciones desde n_starts aleatorios.
    Si se proporciona algorithm_name, ejecuta solo ese algoritmo.
    """
    starts = generate_random_starts(maze, n_starts)
    simulation_results = []

    for idx, start in enumerate(starts):
        print(f"\n🔹 Simulación {idx + 1} | Inicio: {start}")

        if algorithm_name:
            results = run_algorithm(algorithm_name, maze, start, goals)
        else:
            results = run_all_algorithms(maze, start, goals)

        simulation_results.append({
            "start": start,
            "results": results
        })

    return simulation_results


def summarize_simulation(simulation_results):
    summary = {}

    for sim in simulation_results:
        for algo, result in sim["results"].items():
            if result["path"] is None:
                continue

            if algo not in summary:
                summary[algo] = {
                    "cost": [],
                    "nodes": [],
                    "time": []
                }

            summary[algo]["cost"].append(result["cost"])
            summary[algo]["nodes"].append(result["nodes_explored"])
            summary[algo]["time"].append(result["time"])

    # 🔹 Promedios
    averages = {}

    for algo, data in summary.items():
        averages[algo] = {
            "avg_cost": sum(data["cost"]) / len(data["cost"]),
            "avg_nodes": sum(data["nodes"]) / len(data["nodes"]),
            "avg_time": sum(data["time"]) / len(data["time"])
        }

    return averages


def print_summary(averages):
    print("\n=========== RESUMEN DE SIMULACIÓN ===========\n")

    for algo, metrics in averages.items():
        print(f"--- {algo} ---")
        print(f"Costo promedio: {metrics['avg_cost']:.2f}")
        print(f"Nodos promedio: {metrics['avg_nodes']:.2f}")
        print(f"Tiempo promedio: {metrics['avg_time']:.6f} s")
        print()