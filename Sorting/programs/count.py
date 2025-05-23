def count(arr):
    max=0
    for i in range(len(arr)):
        if arr[i]>max:
            max=arr[i]
    c=[0]*(max+1)

    for i in arr:
        c[i]+=1        
    
    sort=[]
    for i in range(len(c)):
       for _ in range(c[i]):
           sort.append(i)
    return sort

arr = [4, 2, 2, 8, 3, 3, 1]
result=count(arr)
print(result)
