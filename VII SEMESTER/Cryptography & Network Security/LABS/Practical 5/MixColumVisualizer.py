import numpy as np

# Galois Field multiplication
def galois_multiply(a, b):
    p = 0
    for i in range(8):
        if b & 1:
            p ^= a
        carry = a & 0x80
        a <<= 1
        if carry:
            a ^= 0x1B  # AES's irreducible polynomial
        b >>= 1
    return p & 0xFF

# MixColumns matrix in AES
mix_column_matrix = np.array([[2, 3, 1, 1],
                              [1, 2, 3, 1],
                              [1, 1, 2, 3],
                              [3, 1, 1, 2]])

# Input matrix (as given)
state = np.array([[0xAD, 0x67, 0x56, 0xD5],
                  [0x45, 0x02, 0x0F, 0x43],
                  [0x0E, 0xB6, 0xBE, 0xDF],
                  [0x48, 0x19, 0x37, 0xCA]])

# Function to perform MixColumns on a single column
def mix_single_column(col):
    result = np.zeros(4, dtype=int)
    for i in range(4):
        result[i] = (galois_multiply(mix_column_matrix[i][0], col[0]) ^
                     galois_multiply(mix_column_matrix[i][1], col[1]) ^
                     galois_multiply(mix_column_matrix[i][2], col[2]) ^
                     galois_multiply(mix_column_matrix[i][3], col[3]))
    return result

# Function to apply MixColumns on the entire state matrix
def mix_columns(state):
    state_mixed = np.zeros((4, 4), dtype=int)
    for i in range(4):
        state_mixed[:, i] = mix_single_column(state[:, i])
    return state_mixed

# Visualize each step
def visualize_mix_columns(state):
    print("Initial State:")
    print(state)
    print("\nStarting MixColumns process...\n")
    
    for col_idx in range(4):
        col = state[:, col_idx]
        print(f"\nProcessing Column {col_idx + 1}: {col}")
        intermediate_results = []
        for row_idx in range(4):
            row_mults = [
                f"{mix_column_matrix[row_idx][j]}*{hex(col[j])}" 
                for j in range(4)
            ]
            print(f"\nMultiplying row {row_idx + 1} of mix matrix with column: {' + '.join(row_mults)}")
            
            row_result = (
                galois_multiply(mix_column_matrix[row_idx][0], col[0]) ^
                galois_multiply(mix_column_matrix[row_idx][1], col[1]) ^
                galois_multiply(mix_column_matrix[row_idx][2], col[2]) ^
                galois_multiply(mix_column_matrix[row_idx][3], col[3])
            )
            
            intermediate_results.append(row_result)
            print(f"Resulting value (XOR of products) for row {row_idx + 1}: {hex(row_result)}")

        print(f"\nColumn {col_idx + 1} after MixColumns: {list(map(hex, intermediate_results))}")

    mixed_state = mix_columns(state)
    print("\nFinal State after MixColumns:")
    print(np.vectorize(hex)(mixed_state))

# Run the visualizer
visualize_mix_columns(state)
