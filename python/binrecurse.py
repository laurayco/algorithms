
# takes a single argument and
# outputs each combination of
# binary digits.

def br(n):
  if n<1:
    print('0')
  else:
    m = 2**n - 1
    for i in range(2**(n-1)):
      print(bin(m-i)[2:])
    br(n-1)

if __name__ == "__main__":
    from sys import argv
    [x for x in map(br,map(int,argv[1:]))]
