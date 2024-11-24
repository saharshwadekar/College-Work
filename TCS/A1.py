def main():
    initial_balance= int(input())
    num_operations = int(input())
    history = [initial_balance]
    changes = []
    current_balance_index = 0
    
    for _ in range(num_operations):
        operation = input().strip()
        
        if operation.startswith("read"):
            print(history[current_balance_index])
        
        elif operation.startswith("credit") or operation.startswith("debit"):
            operation, amount = operation.split()
            amount = int(amount)
            if operation == "credit":
                history[current_balance_index] += amount
            else:
                history[current_balance_index] -= amount
            changes.append(amount if operation == "credit" else -amount)
        
        elif operation.startswith("abort"):
            index = int(input()) - 1
            if index < len(changes):
                history[current_balance_index] -= changes[index]
                changes[index] = 0
        
        elif operation.startswith("rollback"):
            rollback_index = int(input()) - 1
            current_balance_index = rollback_index
            history = history[:rollback_index + 1]
        
        elif operation.startswith("commit"):
            history.append(history[current_balance_index])
            current_balance_index += 1


if __name__ == "__main__":
    main()
