def _sum(arr):
    sum=0
    for i in arr:
        sum=sum+i
    return(sum)
arr=[]
arr=[25,32,16,65]
n=len(arr)
ans=_sum(arr)
print('sum of the array is',ans)
print('length of an array',n)
