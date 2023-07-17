class solution :
    def matrix_transpose(self,a):
        row=len(a)
        col=len(a[0])
        b=[[0 for _ in range(row)]for _ in range (col)]
        for i in range (row):
            for j in range (col):
                b[j][i]=a[i][j]
        j=-1
        c=0
        while(c<row):
            j+=1
            left=0
            right=row-1
            while(right>left):
                b[j][left],b[j][right]=b[j][right],b[j][left]
                left+=1
                right-=1
            c+=1
        return b
a1=solution()
row =int(input())
arr=[]
for i in range (row):
    col=list(map(int,input().split()))
    arr.append(col)
print(a1.matrix_transpose(arr))
