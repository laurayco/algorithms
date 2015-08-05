# Exercise 1.1 "Horner's Rule"

def horn(x,*a):
  s = 0
  for v in a:
    s = s*x + v
  return s

if __name__ == "__main__":
  from sys import argv; argv = argv[1:]
  vals = list(map(int,argv))
  x,pn = vals[0],vals[1:]
  print(horn(x,*pn))
