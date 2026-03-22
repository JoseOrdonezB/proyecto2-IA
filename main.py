from utils.load_data import load_maze
from algorithms.bfs import breadth_first_search
from algorithms.dfs import depth_first_search
from algorithms.gbfs import greedy_best_first_search
from algorithms.astar import a_star_search
from utils.heuristics import manhattan, euclidean

def print_result(name, result):
    print(f"\n=== {name} ===")

    if result["path"] is None:
        print("No se encontró solución.")
        return

    print(f"Longitud del camino: {result['cost']}")
    print(f"Nodos explorados: {result['nodes_explored']}")
    print(f"Tiempo: {result['time']:.6f} segundos")


def main():
    # 🔹 Cargar laberinto
    maze, start, goals = load_maze("./data/test_maze.txt")

    print("Inicio:", start)
    print("Metas:", goals)

    # 🔹 BFS
    result_bfs = breadth_first_search(maze, start, goals)
    print_result("BFS", result_bfs)

    # 🔹 DFS
    result_dfs = depth_first_search(maze, start, goals)
    print_result("DFS", result_dfs)

    # 🔹 GBFS (Manhattan)
    result_gbfs_manhattan = greedy_best_first_search(
        maze, start, goals, manhattan
    )
    print_result("GBFS (Manhattan)", result_gbfs_manhattan)

    # 🔹 GBFS (Euclidiana)
    result_gbfs_euclidean = greedy_best_first_search(
        maze, start, goals, euclidean
    )
    print_result("GBFS (Euclidiana)", result_gbfs_euclidean)

    # 🔹 A* (Manhattan)
    result_astar_manhattan = a_star_search(
        maze, start, goals, manhattan
    )
    print_result("A* (Manhattan)", result_astar_manhattan)

    # 🔹 A* (Euclidiana)
    result_astar_euclidean = a_star_search(
        maze, start, goals, euclidean
    )
    print_result("A* (Euclidiana)", result_astar_euclidean)


if __name__ == "__main__":
    main()