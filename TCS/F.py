from collections import deque


def main():
    # Read the size of the matrix
    N = int(input())
    matrix = []

    # Read the matrix input
    for _ in range(N):
        matrix.append(list(input()))

    # Print the matrix for debugging
    print(matrix)

    # Find the starting and ending terminals (marked as '.')
    start = None
    end = None
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == ".":
                if not start:
                    start = (i, j)  # First terminal
                else:
                    end = (i, j)  # Second terminal

    # Define the possible movement directions for each type of element
    directions = {
        "-": [(0, -1), (0, 1)],  # Horizontal connections
        "|": [(-1, 0), (1, 0)],  # Vertical connections
        "+": [(-1, 0), (1, 0), (0, -1), (0, 1)],  # Junctions connect in all directions
    }

    # Perform BFS to find all possible resistances
    def bfs_resistance():
        queue = deque([(start, 0)])  # Start with the starting terminal
        visited = set()  # Track visited positions
        resistances = []  # Store resistances for all paths to the end

        while queue:
            (x, y), resistance = queue.popleft()

            if (x, y) in visited:
                continue
            visited.add((x, y))

            if (x, y) == end:
                resistances.append(resistance)
                continue

            current = matrix[x][y]

            if current in directions:
                for dx, dy in directions[current]:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                        neighbor = matrix[nx][ny]

                        if neighbor in {"-", "|", "+"}:
                            queue.append(((nx, ny), resistance + 1))
                        elif neighbor == ".":  
                            queue.append(((nx, ny), resistance))

        return resistances

    resistances = bfs_resistance()

    if len(resistances) == 1:
        total_resistance = resistances[0]
    else:
        filtered_resistances = [r for r in resistances if r > 0]

        if not filtered_resistances:
            total_resistance = 0
        else:
            total_resistance = 1 / sum(1 / r for r in filtered_resistances)
    
    print(resistances)


if __name__ == "__main__":
    main()
