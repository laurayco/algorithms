# Exercise 1.2
# permutations of boolean variables.

# based on binary
# true = 1
# false = 0
# num_values = 2**n

def calculate(n):
  # slow algorithm
  mask = 2 ** (n-1)
  for i in range(2**n):
    for x in range(n):
      print(i&mask>0,end=" ")
      i = i << 1
    print()

if __name__=="__main__":
  from sys import argv; argv = argv[1:]
  vals = list(map(int,argv))
  calculate(max(vals))
