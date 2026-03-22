def load_maze(file_path):
    maze = []
    start_positions = []
    goal_positions = []

    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            line = line.strip()

            if not line:
                continue

            row = list(line)
            maze.append(row)

            for j, value in enumerate(row):
                if value == '2':
                    start_positions.append((i, j))
                elif value == '3':
                    goal_positions.append((i, j))

    if len(start_positions) == 0:
        raise ValueError("El laberinto no tiene punto de inicio (2)")

    if len(goal_positions) == 0:
        raise ValueError("El laberinto no tiene meta (3)")

    start = start_positions[0]

    return maze, start, goal_positions