def EEA(a: int ,b: int) -> tuple:
    r1: int = a
    r2: int = b
    t1: int = 0
    t2: int = 1
    s1: int = 1
    s2: int = 0
    print('-'*70)
    print(f'|{'q':^6}|',end="")
    print(f'{'r1':^6}|',end="")
    print(f'{'r2':^6}|',end="")
    print(f'{'r':^6}|',end="")
    print(f'{'t1':^6}|',end="")
    print(f'{'t2':^6}|',end="")
    print(f'{'t':^6}|',end="")
    print(f'{'s1':^6}|',end="")
    print(f'{'s2':^6}|',end="")
    print(f'{'s':^6}|')
    print('-'*70)

    while(r2 > 0):
        q: int = r1 // r2
        print(f'|{q:^6}|',end="")
        print(f'{r1:^6}|',end="")
        print(f'{r2:^6}|',end="")
        r: int = r1 - q * r2
        r1, r2 = r2, r
        print(f'{r:^6}|',end="")
        
        print(f'{t1:^6}|',end="")
        print(f'{t2:^6}|',end="")
        t: int = t1 - q * t2
        t1, t2 = t2, t
        print(f'{t:^6}|',end="")
        
        print(f'{s1:^6}|',end="")
        print(f'{s2:^6}|',end="")
        s: int = s1 - q * s2
        s1, s2 = s2, s
        print(f'{s:^6}|')
    print(f'|{"":^6}|',end="")
    print(f'{r1:^6}|',end="")
    print(f'{r2:^6}|',end="")
    print(f'{"":^6}|',end="")
    print(f'{t1:^6}|',end="")
    print(f'{t2:^6}|',end="")
    print(f'{"":^6}|',end="")     
    print(f'{s1:^6}|',end="")
    print(f'{s2:^6}|',end="")
    print(f'{"":^6}|')
        
    print('-'*70)
    
    return (r1, t1, s1)
    
def main() -> None:
    print(f'{'start':-^40}')
    a: int = int(input("Enter A: "))
    b: int = int(input("Enter B: "))
    
    result = list(EEA(a=a,b=b))
    print(f"GCD({a},{b}) = {result[0]}")
    print("coefficients of Bezout's")
    print("t:",result[1])
    print("s:",result[2])
    print(f'{'end':-^40}')   

if __name__ == '__main__':
    main()