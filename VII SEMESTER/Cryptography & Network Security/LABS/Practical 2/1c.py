def main() -> None:
    key: list[int] = map(int, input("Enter Your key: ").split(" ")) 
    key: list[list[int]] = list(map(list, enumerate(key, start= 1)))
    key.sort(key= lambda x: x[1])
    key:list[int] = [x[0] for x in key]
    print(f'{key=}')

if __name__ == '__main__':
    main()