🧮 Min Heap Implementation in Python
---
This is a basic implementation of a Min Heap in Python. A Min Heap ensures that the smallest element is always at the root.

---
📌 Features
---
Insert elements into the heap

Extract the minimum element (root)

Maintains the heap property on each operation

---
🧠 How It Works
---
Insert: Adds a value and performs up-heap bubbling to maintain heap order.

Extract Min: Removes the root and performs down-heap bubbling.

Heapify Down: Ensures the heap property from top to bottom.

```python
class Minheap:
    def __init__(self):
        self.heap=[]
    def get_parent_index(self,i):
        Parent =(i - 1) // 2
        return Parent

    def get_left_child_index(self,i):
        Left = 2*i + 1
        return Left

    def get_right_child_index(self,i):
        Right =2*i + 2
        return Right
    
    def insert(self,Value):
        self.heap.append(Value)
        curr= len(self.heap)-1
        while curr >0 and self.heap[curr]<self.heap[self.get_parent_index(curr)]:
            temp=self.get_parent_index(curr)
            self.heap[temp],self.heap[curr]=self.heap[curr],self.heap[temp]
            curr=temp
    def extract_min(self):
        if not self.heap:
            return None
        min_val=self.heap[0]
        self.heap[0]=self.heap[len(self.heap)-1]
        #self.heap[len(self.heap)-1]=min_val
        self.heap.pop()
        self.heapify_down(0)
        return min_val
    def heapify_down(self, i):
        while True:
            left = self.get_left_child_index(i)
            right = self.get_right_child_index(i)
            smallest = i

        # check if left child exists and is smaller
            if  left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left

        # check if right child exists and is smaller
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right

            # if i is already the smallest, break
            if smallest == i:
                break

        # swap and continue
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest
a=[10, 4, 15, 1, 20]
h = Minheap()
for val in a:
    h.insert(val)
    print(f"Heap after inserting {val}: {h.heap}")

print(f"Extracted Min: {h.extract_min()}")
print(f"Heap after extract_min: {h.heap}")
```
# OUTPUT
```
Heap after inserting 10: [10]
Heap after inserting 4: [4, 10]
Heap after inserting 15: [4, 10, 15]
Heap after inserting 1: [1, 4, 15, 10]
Heap after inserting 20: [1, 4, 15, 10, 20]
Extracted Min: 1
Heap after extract_min: [4, 10, 15, 20]
```
---
# 🌳 Min Heap Visualization
Let's take the input:

a = [10, 4, 15, 1, 20]
We will insert them one by one and show how the heap looks like after each operation.

# 🔢 Step-by-step Insertion Visualization

Insert 10

        10
        
Insert 4 → Bubble up (4 < 10)
```
        4
       /
     10
```
Insert 15 → No bubble up (15 > 4)

```
        4
       / \
     10   15
```
Insert 1 → Bubble up twice (1 < 4)
```
        1
       / \
     4     15
    /
  10
```
Insert 20 → No bubble up
```
        1
       / \
     4     15
    / \
  10  20
```
# 🔻 Extract Min (remove 1)

Swap root with last node (20)

Remove 1

Heapify down → 20 → 4 → 10

Initial:
```
        1
       / \
     4     15
    / \
  10  20
```
 Swap and Pop:
```
        20
       / \
     4     15
    /  
  10
```
Heapify Down (20 > 4 → swap → 20 > 10 → swap):
```
        4
       / \
     10    15
    /
  20
```
# 📌 Final Heap Structure
```
        4
       / \
     10   15
    /
  20
```
# 📌 Max Heap Implementation in Python
A Max Heap is a complete binary tree where the value of each node is greater than or equal to its children. This ensures that the largest element is always at the root.

# 🧠 Features
Insert elements into a max-heap

Extract the maximum value

Maintain heap property after insertion and extraction
```python
class Maxheap:
    def __init__(self):
        self.heap=[]
    def get_parent_index(self,i):
        Parent =(i - 1) // 2
        return Parent

    def get_left_child_index(self,i):
        Left = 2*i + 1
        return Left

    def get_right_child_index(self,i):
        Right =2*i + 2
        return Right
    
    def insert(self,Value):
        self.heap.append(Value)
        curr= len(self.heap)-1
        while curr >0 and self.heap[curr]>self.heap[self.get_parent_index(curr)]:
            temp=self.get_parent_index(curr)
            self.heap[temp],self.heap[curr]=self.heap[curr],self.heap[temp]
            curr=temp
    def extract_max(self):
        if not self.heap:
            return None
        max_val=self.heap[0]
        self.heap[0]=self.heap[len(self.heap)-1]
        #self.heap[len(self.heap)-1]=min_val
        self.heap.pop()
        self.heapify_down(0)
        return max_val
    def heapify_down(self, i):
        while True:
            left = self.get_left_child_index(i)
            right = self.get_right_child_index(i)
            largest = i

        # check if left child exists and is smaller
            if  left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left

        # check if right child exists and is smaller
            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right

            # if i is already the smallest, break
            if largest == i:
                break

        # swap and continue
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            i = largest
a=[10, 4, 15, 1, 20]
h = Maxheap()
for val in a:
    h.insert(val)
    print(f"Heap after inserting {val}: {h.heap}")

print(f"Extracted Max: {h.extract_max()}")
print(f"Heap after extract_max: {h.heap}")
```
# OUTPUT
```
Heap after inserting 10: [10]
Heap after inserting 4: [10, 4]
Heap after inserting 15: [15, 4, 10]
Heap after inserting 1: [15, 4, 10, 1]
Heap after inserting 20: [20, 15, 10, 1, 4]
Extracted Max: 20
Heap after extract_max: [15, 4, 10, 1]
```
# 📊 Visualization
Imagine inserting values [10, 4, 15, 1, 20] step-by-step into the heap:
```
Insert 10:
     10

Insert 4:
     10
    /
   4

Insert 15:
     15
    /  \
   4   10

Insert 1:
     15
    /  \
   4   10
  /
 1

Insert 20:
     20
    /  \
   15  10
  / \
 1   4

```
# 🔻 extract_max() — Remove the Root (Maximum) Element
The extract_max() function removes and returns the maximum element (which is always the root node) from the Max Heap.

# 🚀 How It Works
Remove the root node (which is the max value).

Move the last element in the heap to the root.

Remove the last element from the array.

Restore the heap property using heapify_down() from the root down.

# 🧠 Key Insight
Since the Max Heap always maintains the largest element at the top, removing the root gives us the maximum in O(log n) time.

# 🧮 Step-by-Step Example
Suppose our heap looks like this:
```
     20
    /  \
  15    10
 / \
1   4
```
# Operation: extract_max()
Step 1: Remove 20 (the root).

Step 2: Move 4 (last element) to the top.

Step 3: Heap becomes:
```
     4
    / \
  15   10
 / 
1
```
Step 4: Heapify down:

4 < 15 → swap

Heap becomes:

```
     15
    /  \
   4    10
  /    
 1
```
4 is now > its children → stop.

✅ Final Heap:
```
     15
    /  \
   4    10
  /    
 1
```
