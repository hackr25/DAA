#Q1
a=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
  ];
rows=len(a);
cols=len(a[0]);
for i in range(0,rows):
    sumrow=0;
    for j in range(0,cols):
        sumrow=sumrow+a[i][j];
    print("sum of" + str(i+1) +"row: " +str(sumrow));
for i in range(0,rows):
    sumcol=0;
    for j in range(0,cols):
        sumcol=sumcol+a[j][i];
    print("sum of" + str(i+1) +"Columns: " +str(sumcol));

