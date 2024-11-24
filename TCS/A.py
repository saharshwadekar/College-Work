def credit(balance, amount) -> int:
    return balance + amount if balance > amount else 0


def debit(balance, amount) -> int:
    return balance - amount if balance > amount else 0


def main() -> None:
    Actualbalance = int(input())
    n_operation = int(input())

    operations = [input() for i in range(n_operation)]
    lastcommit = -1
    tempBalance = Actualbalance
    for index, operation in enumerate(operations):

        if operation.startswith("read"):
            print(Actualbalance)

        elif operation.startswith("commit"):
            lastcommit = index
            Actualbalance = tempBalance

        elif operation.startswith("credit"):
            _, amount = operation.split(" ")
            tempBalance = credit(tempBalance, int(amount))

        elif operation.startswith("debit"):
            _, amount = operation.split(" ")
            tempBalance = debit(tempBalance, int(amount))

        elif operation.startswith("abort"):
            _, idx = operation.split(" ")
            idx = int(idx) - 1
            while (
                operations[idx].startswith("read")
                or operations[idx].startswith("abort")
                or operations[idx].startswith("commit")
            ):
                idx += 1
            if idx > lastcommit:
                if operations[idx].startswith("credit"):
                    _, amount = operations[idx].split(" ")
                    tempBalance = debit(tempBalance, int(amount))
                elif operations[idx].startswith("debit"):
                    _, amount = operations[idx].split(" ")
                    tempBalance = credit(tempBalance, int(amount))

        elif operation.startswith("rollback"):
            tempBalance = Actualbalance


if __name__ == "__main__":
    main()
