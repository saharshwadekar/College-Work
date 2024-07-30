class Stack:
    def __init__(self) -> None:
        self._data: list[int] = list()

    def push(self, element: int) -> None:
        self._data.append(element)

    def pop(self) -> int:
        return self._data.pop()

    def peak(self) -> None:
        print(self._data[-1])

    def __str__(self) -> None:
        print(*self._data)


stack: Stack = Stack()
stack.push(3)
stack.peak()