from collections import defaultdict


def DFS(node, graph, visited, parent):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if DFS(neighbor, graph, visited, node):
                return True
        elif neighbor != parent:
            return True
    return False


def numberOfFigures(lines):
    graph = defaultdict(list)
    points = set()

    for x1, y1, x2, y2 in lines:
        p1, p2 = (x1, y1), (x2, y2)
        graph[p1].append(p2)
        graph[p2].append(p1)
        points.update([p1, p2])

    visited = {point: False for point in points}
    NoOfFigs = 0

    for point in points:
        if not visited[point]:
            if DFS(point, graph, visited, None):
                NoOfFigs += 1

    return NoOfFigs


def main():
    N = int(input())
    lines = [tuple(map(int, input().split())) for _ in range(N)]
    NoOfFigs = numberOfFigures(lines)
    print(NoOfFigs)


if __name__ == "__main__":
    main()
