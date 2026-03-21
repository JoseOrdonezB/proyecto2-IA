def load_maze(file_path):
    maze = []
    start_positions = []
    goal_positions = []

    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            row = list(line.strip())
            maze.append(row)

            for j, value in enumerate(row):
                if value == '2':
                    start_positions.append((i, j))
                elif value == '3':
                    goal_positions.append((i, j))

    return maze, start_positions, goal_positions