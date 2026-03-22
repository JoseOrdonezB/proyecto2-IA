def extract_metrics(result):
    if result["path"] is None:
        return None

    return {
        "cost": result["cost"],
        "nodes": result["nodes_explored"],
        "time": result["time"],
        "branching_factor": result.get("branching_factor", 0)
    }


def aggregate_metrics(results_list):
    valid_results = [r for r in results_list if r is not None]

    if not valid_results:
        return None

    n = len(valid_results)

    return {
        "avg_cost": sum(r["cost"] for r in valid_results) / n,
        "avg_nodes": sum(r["nodes"] for r in valid_results) / n,
        "avg_time": sum(r["time"] for r in valid_results) / n,
        "avg_branching": sum(r["branching_factor"] for r in valid_results) / n
    }


def compare_algorithms(simulation_results):
    grouped = {}

    for sim in simulation_results:
        for algo, result in sim["results"].items():

            metrics = extract_metrics(result)

            if metrics is None:
                continue

            if algo not in grouped:
                grouped[algo] = []

            grouped[algo].append(metrics)

    comparison = {}

    for algo, metrics_list in grouped.items():
        comparison[algo] = aggregate_metrics(metrics_list)

    return comparison


def print_comparison(comparison):
    print("\n=========== COMPARACIÓN DE ALGORITMOS ===========\n")

    for algo, metrics in comparison.items():
        if metrics is None:
            continue

        print(f"--- {algo} ---")
        print(f"Costo promedio: {metrics['avg_cost']:.2f}")
        print(f"Nodos promedio: {metrics['avg_nodes']:.2f}")
        print(f"Tiempo promedio: {metrics['avg_time']:.6f} s")
        print(f"Branching factor promedio: {metrics['avg_branching']:.4f}")
        print()