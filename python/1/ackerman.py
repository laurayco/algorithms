def ack(m,n):
    if m==0:
        return n+1
    elif n==0:
        return ack(m-1,1)
    return ack(m-1,ack(m,n-1))

if __name__=="__main__":
    m = int(input("m> "))
    n = int(input("n> "))
    print(ack(m,n))
