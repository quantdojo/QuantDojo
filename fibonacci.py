def fib(n):
    "Print a Fibonacci series up to n"
    a, b = 0, 1
    while b < n:
            print b,
            a, b = b, a+b

fib(200)
input()
