def Selection(a):
    for i in range(len(a)-1):
        k=i
        for j in range (i+1,len(a)):
            if a[j]<a[k]:
               k=j
        a[i],a[k]=a[k],a[i]
a=[64,25,12,22,11]
Selection(a)
print(a)
