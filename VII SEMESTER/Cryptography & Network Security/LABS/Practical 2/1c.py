def main() -> None:
    print(f'{'start':-^40}')
    enkey: list[int] = map(int, input("Enter Your key: ").strip().split(" "))
   
    
    enkey: list[list[int]] = list(map(list, enumerate(enkey, start=1)))
    dekey: list[list[int]] = sorted(enkey, key=lambda x: x[1])
    
    enkey: list[int] = [x[1] for x in enkey]
    dekey: list[int] = [x[0] for x in dekey]
    
    print('-' * 40)
    print(f'Encryption Key: ',*enkey)
    
    print(f'Decryption Key: ',*dekey)
    print(f'{'end':-^40}')

if __name__ == '__main__':
    main()