THERE ARE TOTAL 10 SORTING ALGORITHM

OUT OF 10 SORTING ALGORITHM IT IS DIVEIDED INTO TWO TYPES 

---COMPARISON
    
Bubble Sort || Selection Sort || Insertion Sort || Merge Sort || Quicksort || Heap Sort || Shell Sort
    
🔹 1. Bubble Sort

✅ Basic Idea:
Repeatedly compare adjacent elements and swap if out of order. Smaller elements "bubble" to the top.

💡 Use Case:
Educational purposes only; used to teach sorting fundamentals and internal loops.

🔹 2. Selection Sort

✅ Basic Idea:
Repeatedly find the minimum element from the unsorted part and place it at the beginning.

💡 Use Case:
Useful where swaps are costly but comparisons are cheap. Also for simple array problems.

🔹 3. Insertion Sort

✅ Basic Idea:
Build the final sorted array one item at a time by inserting elements into the correct position.

💡 Use Case:
Excellent for small or nearly sorted arrays. Often used as the base case in recursive sorts like Merge Sort.

🔹 4. Merge Sort

✅ Basic Idea:
Divide the array into halves, recursively sort them, then merge the sorted halves.

💡 Use Case:
Great for linked lists, external sorting, and when stability is important (e.g., sorting database records).

🔹 5. Quick Sort

✅ Basic Idea:
Select a pivot, partition the array such that left < pivot < right, then recursively sort partitions.

💡 Use Case:
Ideal for large arrays and commonly used in practice due to fast average performance.

🔹 6. Heap Sort

✅ Basic Idea:
Build a heap (max or min) and extract elements one by one to sort.

💡 Use Case:
Useful when O(1) space and guaranteed O(n log n) time are needed. Also good for priority queues.

🔹 7. Shell Sort

✅ Basic Idea:
Generalization of Insertion Sort that sorts elements far apart using gaps, reducing the gap each pass.

💡 Use Case:
Practical improvement over Insertion Sort for moderate-sized arrays. Useful in embedded systems.



---NON-COMPARISON
    
Counting Sort || Radix Sort || Bucket Sort
    
🔹 1. Counting Sort

✅ Basic Idea:
Count occurrences of each element in a frequency array (indexed by value), then compute positions using prefix sums and place elements accordingly.

💡 Use Cases:

Sorting integers in a small fixed range (e.g., age, scores).

Situations where O(n log n) comparison-based limits can be avoided.

Useful as a subroutine in Radix Sort.

🔹 2. Radix Sort

✅ Basic Idea:
Sort elements digit by digit, from least significant to most significant (LSD variant), using a stable sort (often Counting Sort) at each digit level.

💡 Use Cases:

Sorting large lists of integers, especially when digit length (k) is small.

Sorting fixed-length strings (e.g., IDs, zip codes).

Used in databases and network routers for integer or IP address sorting.

🔹 3. Bucket Sort

✅ Basic Idea:
Distribute elements into buckets based on value ranges. Then sort each bucket individually (using Insertion Sort or another sort) and concatenate the results.

💡 Use Cases:

Sorting uniformly distributed real numbers (e.g., [0, 1)).

Sorting floating point numbers when values are well-distributed.

Used in hash-based applications and sometimes in graphics pipelines.



| Algorithm          | Best Case     | Average Case   | Worst Case | Space Complexity       | Stable? |
| ------------------ | ------------- | -------------- | ---------- | ---------------------- | ------- |
| Bubble Sort        | O(n)          | O(n²)          | O(n²)      | O(1)                   | ✅ Yes   |
| Selection Sort     | O(n²)         | O(n²)          | O(n²)      | O(1)                   | ❌ No    |
| Insertion Sort     | O(n)          | O(n²)          | O(n²)      | O(1)                   | ✅ Yes   |
| Merge Sort         | O(n log n)    | O(n log n)     | O(n log n) | O(n)                   | ✅ Yes   |
| Quick Sort         | O(n log n)    | O(n log n)     | O(n²)      | O(log n)               | ❌ No    |
| Heap Sort          | O(n log n)    | O(n log n)     | O(n log n) | O(1)                   | ❌ No    |
| Shell Sort         | O(n log n)    | Depends on gap | O(n²)      | O(1)                   | ❌ No    |
| Counting Sort	     | O(n + k)	     | O(n + k)	      | O(n + k)   | O(k)	                | ✅ Yes   |
| Radix Sort	     | O(nk)	     | O(nk)	      | O(nk)	   | O(n + k)	            | ✅ Yes   |
| Bucket Sort	     | O(n + k)      | O(n + k)       |	O(n²) |    | (if poorly distributed)|✅ Yes (if stable sort is used inside)|	
                                                                        O(n + k)            	

n = number of elements

k = range of input (or number of digits for Radix Sort)

Bucket Sort worst case can degrade to O(n²) if many elements fall into one bucket.

