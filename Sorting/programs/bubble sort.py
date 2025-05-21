def bubble(a):
    for i in range(len(a)):
        for j in range(0, len(a) - i - 1):  
            if a[j] > a[j + 1]:         
                a[j], a[j + 1] = a[j + 1], a[j]  

a = [5, 3, 7, 6, 8]
bubble(a)
print(a)
