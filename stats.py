n = int(input())
def belist ():
  sum = 0
  nlist = [ 0 for i in range(n)]
  for i in range(n):
    nlist[i] = int(input())
    sum = sum + nlist[i]
  print('Before data')
  print(nlist)

def aflist ():

  if sum >= 10 :
    n = n+1
  else:
    n = n-1
  nlist = [ 0 for i in range (n)]

  for i in range(n):
    nlist[i] = int(input())
  print('After data')
  print(nlist)

belist()
aflist()