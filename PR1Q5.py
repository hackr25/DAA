def counteo(arr,arr_size):
    eve_count=0
    od_count=0
    for i in range(arr_size):
        if(arr[i]&1==1):
            od_count+=1
        else:
            eve_count+=1
    print('Number of even elements= ',eve_count)
    print('Number of odd elements= ',od_count)
arr=[12,65,95,36,15,68,25,6,65,95]
n=len(arr)
counteo(arr,n)
