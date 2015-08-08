
def fibo_recurse(n):
    return (fibo_recurse(n-1) if n>1 else 0) + n

def fibo_iterative(n):
    a = n
    for i in range(n):
        a = a + i
    return a

def fibo(n,i=True):
    return fibo_iterative(n) if i else fibo_recurse(n)

if __name__ == "__main__":
    v = int(input("Fibonacci > "))
    print(fibo(v))
    print(fibo(v,False))
