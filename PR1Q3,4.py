arr=[12,1234,45,67,9]
maximum=arr[0]
for i in range(len(arr)):
    if arr[i]>maximum:
        maximum=arr[i]
print(maximum)

minimum=arr[0]
for i in range(len(arr)):
    if arr[i] < minimum:
        minimum=arr[i]
print(minimum)
