# 📘 Assignment: Sorting and Searching Algorithms

## 🎯 Objective

Learn how to implement and compare fundamental searching and sorting algorithms. You'll build practical implementations of linear search, binary search, and sorting techniques while exploring how algorithm efficiency impacts performance.

## 📝 Tasks

### 🛠️ Task 1: Implement Linear and Binary Search

#### Description
Start by implementing two core search algorithms. Linear search scans through a list one element at a time, while binary search efficiently finds elements in sorted lists by repeatedly dividing the search space in half. Write both functions and test them with sample data.

#### Requirements
Completed program should:

- Implement `linear_search(arr, target)` that returns the index of the target or -1 if not found
- Implement `binary_search(arr, target)` that assumes the list is sorted and returns the index of the target or -1 if not found
- Include test cases demonstrating both functions work correctly
- Add comments explaining how each algorithm works


### 🛠️ Task 2: Implement Sorting Algorithms

#### Description
Implement bubble sort and selection sort to understand how sorting works under the hood. These algorithms form the foundation for understanding more advanced sorting techniques like quicksort and merge sort.

#### Requirements
Completed program should:

- Implement `bubble_sort(arr)` that sorts a list by repeatedly comparing adjacent elements
- Implement `selection_sort(arr)` that sorts a list by finding the minimum element each iteration
- Both functions should sort the list in-place and return the sorted list
- Include test cases with sample lists to verify correctness


### 🛠️ Task 3: Compare Algorithm Efficiency

#### Description
Measure how the performance of linear search vs. binary search, and different sorting algorithms, changes with larger datasets. Track execution time and understand Big O notation for each algorithm.

#### Requirements
Completed program should:

- Create test lists of varying sizes (e.g., 100, 1,000, 10,000 elements)
- Measure the execution time of linear search vs. binary search on sorted lists
- Measure the execution time of bubble sort vs. selection sort on unsorted lists
- Display results showing how execution time grows with input size
- Write a brief explanation (2-3 sentences) of which algorithm is faster and why


### 🛠️ Task 4: Implement Quicksort (Stretch Goal)

#### Description
Challenge yourself by implementing quicksort, a more advanced divide-and-conquer sorting algorithm. Quicksort is faster than bubble sort and selection sort on average, making it a practical choice for real-world applications.

#### Requirements
Completed program should:

- Implement `quicksort(arr)` using a pivot-based partitioning strategy
- Use recursion to divide the list and sort partitions
- Verify that quicksort produces correctly sorted output
- Compare quicksort's performance to bubble sort and selection sort on large lists
- Document your implementation with clear comments
