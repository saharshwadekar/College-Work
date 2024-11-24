def main():
    Q = int(input())
    queries = [input().split() for _ in range(Q)]

    directions = {
        "top": (0, 1),
        "down": (0, -1),
        "left": (-1, 0),
        "right": (1, 0)
    }

    grid = {}
    grid[1] = (0, 0)

    cube_positions = {1: (0, 0)}

    for cubeA, cubeB, direction in queries:
        cubeA, cubeB = int(cubeA), int(cubeB)
        dx, dy = directions[direction]
        xA, yA = cube_positions[cubeA]
        xB, yB = xA + dx, yA + dy
        cube_positions[cubeB] = (xB, yB)
        grid[cubeB] = (xB, yB)

    shared_sides = 0
    for x, y in grid.values():
        for dx, dy in directions.values():
            neighbor = (x + dx, y + dy)
            if neighbor in grid.values():
                shared_sides += 1

    print(shared_sides // 2)  


if __name__ == "__main__":
    main()
