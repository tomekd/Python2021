
def has_the_same_letters(str_1, str_2):
    return ''.join(sorted(str_1)) == ''.join(sorted(str_2))

def sum_div35(n):
    num_sum = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            num_sum += i
    return num_sum

def fib_rekurencyjnie(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fib_rekurencyjnie(n-2) + fib_rekurencyjnie(n-1)


# 2. Napisz funkcję, która obliczy n-ty wyroz ciągu Fibonacciego nie korzystając z rekurencji.
def fib_nierekurencyjnie(n):
    fib_numbers = [1, 1]
    for i in range(n):
        fib_numbers.append(fib_numbers[-2] + fib_numbers[-1])
    return fib_numbers[n]

def fib_nierekurencyjnie_error(n):
    fib_numbers = [-1, 1]
    for i in range(n):
        fib_numbers.append(fib_numbers[-3] + fib_numbers[-1])
    return fib_numbers[n]

