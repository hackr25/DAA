from array import *
arr=array('i',[])
n=int(input('enter a length of an array: '))
for i in range(n):
    x=int(input('enter elements:'))
    arr.append(x)
print(arr)
val=int(input('enter the value to be searches:'))
k=0
for e in arr:
    if e==val:
        print(k)
        break
    k=k+1
