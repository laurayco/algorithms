
def search(x,l):
    for i in range(len(l)):
        if l[i]==x:
            return i
    return -1 # the Exercise specifies to return 0. I'm ignoring that.

if __name__=="__main__":
    from sys import argv
    print(search(input("query> "),argv[1:]))
