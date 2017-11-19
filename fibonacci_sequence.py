def fibonacci(n):
    fib = [1,1,2]
    while(len(fib) < n):
        fib.append(fib[len(fib)-1] + fib[len(fib)-2])
        print(fib)
