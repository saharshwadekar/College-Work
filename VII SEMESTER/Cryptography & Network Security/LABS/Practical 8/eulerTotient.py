def gcd(a: int, b: int) -> bool:
    if b == 0:
        return a == 1
    else:
        return gcd(b, a % b)


def ETF(number: int) -> int:
    count = 0
    for i in range(1, number):
        if gcd(number, i):
            count += 1
    return count


def FLT(a, p):
    if gcd(a, p) == 1:
        return pow(a, p - 1, p)
    return None


def ET(num, mod):
    if gcd(num, mod):
        return pow(num, ETF(mod), mod)
    return None


while True:
    choice = int(
        input(
            """
Press:
  1 -> Euler Totient Function
  2 -> Fermat Little Theorem
  3 -> Euler Theorem
Enter your choice: """
        )
    )

    match choice:
        case 1:
            number = int(input("Enter a Number: "))
            print(f"Euler Totient of Φ({number}) :", ETF(number))

        case 2:
            a = int(input("Enter a: "))
            p = int(input("Enter p (a prime number): "))
            result = FLT(a, p)
            if result == 1:
                print(f"Fermat Little Theorem holds True for a={a} p={p}")
            else:
                print(f"NOT FOLLOW: Fermat Little Theorem for a={a} p={p}")

        case 3:
            num = int(input("Enter Number: "))
            mod = int(input("Enter moduli (a prime number): "))
            result = ET(num, mod)
            if result is not None:
                print(f"Euler Theorem result for {num}^Φ({mod}) % {mod} :", result)
            else:
                print(f"Euler Theorem does not hold as gcd({num}, {mod}) != 1")

        case _:
            break
