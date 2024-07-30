from typing import Self
class Node:
    def __init__(self, data: int, next_node: Self | None = None) -> None:
        self._data = data
        self._next = next_node


def main() -> None:
    n1: Node = Node(1)
    n2: Node = Node(2)
    n3: Node = Node(3)
    

if __name__ == '__main__':
    main()