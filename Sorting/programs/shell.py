def shell(a):
    n=len(a)//2
    while n>0:
        for i in range(n,len(a)):
            key=a[i]
            k=i
            while k>=n and a[k-n]>key:
                a[k]=a[k-n]
                k=k-n
            a[k]=key
        n=n//2
        
a=[12, 34, 54, 2, 3]
result=shell(a)
print(a)
