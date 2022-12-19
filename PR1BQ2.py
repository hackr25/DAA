#Q2
a=[[12,56,38,49],[15,47,32,72],[52,43,27,16],[89,75,96,25]]
sum=0
primary_diagonal=0
n=4
for i in range(len(a)):
    for j in range(len(a[i])):
        if i==j:
            primary_diagonal=primary_diagonal+a[i][j]
        if i+j==(n-1):
            sum=sum+a[i][j]
print(primary_diagonal)
print(sum)
