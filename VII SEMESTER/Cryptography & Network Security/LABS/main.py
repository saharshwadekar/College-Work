
__map: dict[int, list[str]] = {i: [chr(i+65), chr(i+97)] for i in range(26)}
print(__map[1][0])

_ : int = 9