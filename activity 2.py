def multiply_with_one_iteration(N, M):
    # Single iteration using the built-in multiplication operator
    return N * M

def multiply_with_n_iterations(N, M):
    # Multiplay by adding N a total of M times
    result = 0
    for _ in range(M):
        result += N
    return result

#example usage
N = 5
M = 3

print("Multiplication with one iteration:", multiply_with_one_iteration)
print("Multiplication with n iterations:", multiply_with_n_iterations)