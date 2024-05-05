def heaps_algorithm(n, A):
    if n == 1:
        yield A
    else:
        for i in range(n - 1):
            yield from heaps_algorithm(n - 1, A)
            if n % 2 == 0:
                A[i], A[n - 1] = A[n - 1], A[i]
            else:
                A[0], A[n - 1] = A[n - 1], A[0]
        yield from heaps_algorithm(n - 1, A)

# Example usage
my_list = [1, 2, 3]
for permutation in heaps_algorithm(len(my_list), my_list):
    print(permutation)
