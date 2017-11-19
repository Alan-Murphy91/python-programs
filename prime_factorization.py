def prime_factorization(n):
    prime_list = []
    result = []
    #use sieve of erathostenes to generate list of primes
    bools = [True for i in range(n+1)]
    pr = 2
    while(pr * pr <= n):
        if(bools[pr] == True):
            for x in range(pr*2,n+1,pr):
                bools[x] = False
        pr += 1

    for var, count in enumerate(bools):
        if(count == True and var > 1):
            prime_list.append(var)

    def calc(m, x):
        while(m % prime_list[x] == 0):
            result.append(prime_list[x])
            m = m/prime_list[x]
        if(m < prime_list[x]):
            print(result)
        else:
            return calc(m, x+1)
            
    calc(n,0)
    
    
    
prime_factorization(468)
