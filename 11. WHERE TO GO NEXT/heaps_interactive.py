import itertools
import sys

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

def main():
    try:
        input_list = input("Enter elements separated by spaces: ").split()
        input_list = [int(x) for x in input_list]
    except ValueError:
        print("Please enter valid integers separated by spaces.")
        return

    if len(input_list) == 0:
        print("Empty list provided.")
        return

    for permutation in heaps_algorithm(len(input_list), input_list):
        print(permutation)

if __name__ == "__main__":
    main()
