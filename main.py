import sys

from utils.load_data import load_maze
from experiments.runner import run_all_algorithms, print_results
from experiments.simulator import run_simulation
from experiments.metrics import compare_algorithms, print_comparison

def run_single_maze(file_path):
    print("\n=========== MODO MANUAL ===========")

    maze, start, goals = load_maze(file_path)

    print(f"\nInicio: {start}")
    print(f"Metas: {goals}")

    results = run_all_algorithms(maze, start, goals)

    print_results(results)


def run_experiments(file_path, n_simulations=10):
    print("\n=========== MODO SIMULACIÓN ===========")

    maze, _, goals = load_maze(file_path)

    sim_results = run_simulation(maze, goals, n_starts=n_simulations)

    comparison = compare_algorithms(sim_results)

    print_comparison(comparison)


def main():
    file_path = sys.argv[1] if len(sys.argv) > 1 else "./data/test_maze.txt"

    run_single_maze(file_path)

    run_experiments(file_path, n_simulations=10)


if __name__ == "__main__":
    main()