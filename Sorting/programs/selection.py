def Selection(a):
    for i in range(len(a)-1):      # Outer loop: iterate through the list
        k = i                      # Assume current index (i) has the smallest value
        for j in range(i+1, len(a)):  # Inner loop: check unsorted portion
            if a[j] < a[k]:        # Find the index of the smallest element
                k = j
        a[i], a[k] = a[k], a[i]    # Swap the smallest element with position i

a = [64, 25, 12, 22, 11]
Selection(a)
print(a)  # Output: [11, 12, 22, 25, 64]
