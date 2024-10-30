def fun1(n):
   return n*(n+1)/2
print(fun1(4))
def fun2(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
def fun3(n):
    sum = 0
    for i in range(1, n+1):
        for j in range(i, i+1):
          sum += 1
        return sum