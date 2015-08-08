# "Non Decreasing Order"
# 1.3

"""
Write a C++ program that inputs three integer
and outputs them in non-decreasing order.
"""

# I'm interpreting this to mean we output them in increasing order?

def cheating(l):
  # something to take into consideration:
  #  While the name of this function is "cheating" -
  #  Most of the time it is not logical to implement
  #  a common function like this where a pre-made
  #  implementation is readily / freely available.
  #  Often times it is better than the one you would
  #  make anyways, and you spend less time worrying
  #  about things that don't matter.
  #  So, is this /really/ cheating?
  #  Only inside an algorithms class. :)
  print(*list(sorted(l)))

def not_cheating(l):
  # We have a non-sorted list.
  n = len(l)
  for i in range(n):
      low = i
      hi = i
      for j in range(i,n):
          if l[j] < l[low]:
              low = j
          if l[j] > l[hi]:
              hi = j
      if hi > i:
          t = l[i]
          l[i] = l[hi]
          l[hi] = t
      if low > i:
          t = l[i]
          l[i] = l[low]
          l[low] = t

if __name__ == "__main__":
  from sys import argv; argv = argv[1:]
  vals = list(map(int,argv))
  print(*vals)
  cheating(vals[:])
  not_cheating(vals)
  print(*vals)
