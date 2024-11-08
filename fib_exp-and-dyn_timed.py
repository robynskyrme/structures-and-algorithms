# 8.11.2024
# just quick practice
# timing Fibonacci before and after DP element added

import time

mem = {}

def fib_recurs(n):
    if n <= 2:
        f = 1
    else:
        f = fib_recurs(n-1) + fib_recurs(n-2)

    return f

def fib_memo(n):

    if n in mem:
        return mem[n]

    f = 0

    if n <= 2:
        f = 1
    else:
        f = fib_memo(n-1) + fib_memo(n-2)
    mem[n] = f
    return f



if __name__ == "__main__":

    k = 1

    while k < 41:
        stopwatch = time.time()
        ans = fib_recurs(k)
        recurs = time.time()-stopwatch

        stopwatch = time.time()
        ans = fib_memo(k)
        memo = time.time()-stopwatch

        ratio = recurs / memo

        print("Fibonacci number " + str(k) + " is " + str(ans))
        print("... recursively in " + str(recurs) + " seconds, uzing memoization in " + str(memo) + " (" + str(ratio) + " times faster)\n")

        k+=1