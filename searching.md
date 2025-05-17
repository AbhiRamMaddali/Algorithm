Here we talk about Searching algorithms 

Mainly there are two as we all know

🔍 1. Linear Search

✅ Basic Idea:
Traverse the array element by element from the beginning.

Compare each element with the target.

If a match is found, return the index; else continue till the end.

⏱️ Time Complexity:

Best Case: O(1) (if the target is the first element)

Average Case: O(n)

Worst Case: O(n)

🧠 Space Complexity:

O(1) (no extra space needed)

🛠️ Use Cases:

When the data is unsorted or small.

Simple to implement and no preprocessing is needed.

⚡ 2. Binary Search

✅ Basic Idea:
Works only on sorted arrays.

Repeatedly divide the search range in half:

Compare the middle element with the target.

If it's a match, return the index.

If the target is less, search the left half.

If greater, search the right half.

Recursively or iteratively apply this process.

⏱️ Time Complexity:

Best Case: O(1) (if the middle is the target)

Average Case: O(log n)

Worst Case: O(log n)

🧠 Space Complexity:

O(1) (iterative)

O(log n) (recursive – due to function call stack)

🛠️ Use Cases:

For large sorted datasets.

Used in searching over:

Databases

Dictionaries

Indexes

Search engines (internally)

🔁 Comparison Table

Feature	          |  Linear Search	   | Binary Search
------------------|--------------------|----------------------|
Data  Requirement	| Unsorted or sorted | Sorted only          |
Time Complexity	  | O(n)	             | O(log n)             |           
Space Complexity	| O(1)	             | O(1) / O(log n)      |
Implementation	  | Simple	           |  Requires sorting    |
Use Case	        | Small data sets	   | Large sorted arrays  |

