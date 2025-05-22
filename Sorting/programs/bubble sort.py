def bubble(a):
    for i in range(len(a)): #: Iterates over each element in the list using index i.
        for j in range(0, len(a) - i - 1):  
            if a[j] > a[j + 1]:         #Comparison
                a[j], a[j + 1] = a[j + 1], a[j]   Swap 

a = [5, 3, 7, 6, 8]
bubble(a)
print(a)
# Output [3, 5, 6, 7, 8]
