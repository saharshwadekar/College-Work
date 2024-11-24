def main() -> None:
    N, M = list(map(int, input().split(" ")))
    matrix = {i: [] for i in range(M)}
    for i in range(N):
        inp = list(map(int, input().split(" ")))
        for j in range(M):
            matrix[j].append(inp[j])
    K = int(input())

    visit = set()
    for value in matrix.values():
        while K in value:
            a = value.pop(0)
            if a != K:
                visit.add(a)

    print(len(visit))


if __name__ == "__main__":
    main()
