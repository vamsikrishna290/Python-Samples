def fib(n):
    if n <= 1:
        return 0
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fib_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

def print_fib(n):
    a, b = 0, 1
    ser=[a, b]
    for _ in range(2, n + 1):
        a, b = b, a + b
        ser.append(b)
    return ser

if __name__ == '__main__':
    n=5
    print(f"Iterative fib({n}): {fib(n)}")
    print(f"Recursive fib({n}): {fib_recursive(n)}")
    print(print_fib(n))
