def dfs(maze, start, end):
    stack = [(start, [start])]  # Store position + path taken so far
    visited = set()  # Track visited positions

    while stack:
        (x, y), path = stack.pop()  # Current position + path till now

        # Print the current position
        print("Visiting:", (x, y))

        # Check if we've reached the end
        if (x, y) == end:
            print("Path found:", path)
            return True

        # Mark the current cell as visited
        visited.add((x, y))

        # Explore neighbors (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy

            # Check bounds and if the cell is already visited or is a wall
            if (0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and
                    maze[new_x][new_y] == 0 and (new_x, new_y) not in visited):
                stack.append(((new_x, new_y), path + [(new_x, new_y)]))

    print("No path found")
    return False


# Example maze: 0 -> open path, 1 -> wall
maze = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 0, 0],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0]
]

# Start and end positions
start = (0, 0)
end = (4, 4)

# Solve the maze
dfs(maze, start, end)

