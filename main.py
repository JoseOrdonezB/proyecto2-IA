from algorithms import dfs
from utils.load_data import load_costs, load_heuristics
from algorithms.bfs import breadth_first_search
from algorithms.dfs import depth_first_search
from algorithms.ucs import uniform_cost_search
from algorithms.gbfs import greedy_best_first_search
from algorithms.astar import a_star_search

costos = load_costs('./data/funcion_de_costo.xlsx')
heuristica = load_heuristics('./data/heuristica.xlsx')

opcion = int(input('Selecciona una opción: (1-5): '))

match opcion:
    case 1:
        solucion = breadth_first_search(costos, "Warm-up activities", "Stretching")
        print('Breadth-First Search')

    case 2:
        solucion = depth_first_search(costos, "Warm-up activities", "Stretching")
        print('Depth-First Search')

    case 3:
        solucion = uniform_cost_search(costos, "Warm-up activities", "Stretching")
        print('Uniform-Cost Search')

    case 4:
        solucion = greedy_best_first_search(costos, heuristica, "Warm-up activities", "Stretching")
        print('Greedy-Best-First Search')

    case 5:
        solucion = a_star_search(costos, heuristica, "Warm-up activities", "Stretching")
        print('A* Search')

    case _:
        print('Opción inválida')
        exit()

if solucion:
    print('Camino encontrado:')
    print(solucion.path())
    print('Costo acumulado:', solucion.cost)
    print('Acciones:')
    print(solucion.solution())
else:
    print('No se encontró solución.')