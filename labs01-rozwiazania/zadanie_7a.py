"""
1. Napisz rekurencyjną funkcję, która zwróci n-ty wyraz ciągu Fibonacciego.
2. Napisz funkcję, która obliczy n-ty wyroz ciągu Fibonacciego nie korzystając z rekurencji.
Np. możesz wykorzystać listę do obliczania kolejnych wartości ciągu.

Ciąg Fibonacciego:
a[0] = 1, a[1] = 1, a[n] = a[n-1] + a[n-2] dla n>=2

"""

# 1. Napisz rekurencyjną funkcję, która zwróci n-ty wyraz ciągu Fibonacciego.
def fib_rekurencyjnie(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fib_rekurencyjnie(n-2) + fib_rekurencyjnie(n-1)

print(fib_rekurencyjnie(5))


# 2. Napisz funkcję, która obliczy n-ty wyroz ciągu Fibonacciego nie korzystając z rekurencji.
def fib_nierekurencyjnie(n):
    fib_numbers = [1, 1]
    for i in range(n):
        fib_numbers.append(fib_numbers[-2] + fib_numbers[-1])
    return fib_numbers[n]

print(fib_nierekurencyjnie(5))
