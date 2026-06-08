"""
Sorting and Searching Algorithms
Starter code for implementing and comparing algorithms
"""

import time

# ============================================================================
# TASK 1: Searching Algorithms
# ============================================================================

def linear_search(arr, target):
    """
    Search for target in arr by checking each element sequentially.
    Returns the index of target if found, -1 otherwise.
    
    Time Complexity: O(n)
    """
    # TODO: Implement linear search
    pass


def binary_search(arr, target):
    """
    Search for target in a sorted arr by repeatedly dividing the search space.
    Returns the index of target if found, -1 otherwise.
    Assumes arr is already sorted!
    
    Time Complexity: O(log n)
    """
    # TODO: Implement binary search
    pass


# ============================================================================
# TASK 2: Sorting Algorithms
# ============================================================================

def bubble_sort(arr):
    """
    Sort arr by repeatedly comparing adjacent elements and swapping if needed.
    
    Time Complexity: O(n²)
    """
    # TODO: Implement bubble sort
    # Remember: Modify the list in-place and return it
    pass


def selection_sort(arr):
    """
    Sort arr by repeatedly finding the minimum element and placing it.
    
    Time Complexity: O(n²)
    """
    # TODO: Implement selection sort
    # Remember: Modify the list in-place and return it
    pass


# ============================================================================
# TASK 3: Performance Comparison
# ============================================================================

def compare_search_algorithms():
    """
    Compare the performance of linear search vs binary search.
    """
    # TODO: Create test lists of different sizes
    # TODO: Time linear_search and binary_search on each list
    # TODO: Display and analyze results
    pass


def compare_sorting_algorithms():
    """
    Compare the performance of bubble sort vs selection sort.
    """
    # TODO: Create test lists of different sizes
    # TODO: Time bubble_sort and selection_sort on each list
    # TODO: Display and analyze results
    pass


# ============================================================================
# TASK 4: Advanced Sorting (Stretch Goal)
# ============================================================================

def quicksort(arr):
    """
    Sort arr using the quicksort divide-and-conquer algorithm.
    
    Time Complexity: O(n log n) average, O(n²) worst case
    """
    # TODO: Implement quicksort
    # Hint: Choose a pivot, partition the list, recursively sort partitions
    pass


# ============================================================================
# TEST YOUR IMPLEMENTATIONS
# ============================================================================

if __name__ == "__main__":
    # Test searching
    test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("Testing Linear and Binary Search")
    print(f"Original list: {test_list}")
    print(f"Linear search for 5: {linear_search(test_list, 5)}")
    print(f"Binary search for 5 (sorted): {binary_search(sorted(test_list), 5)}")
    print()
    
    # Test sorting
    print("Testing Sorting Algorithms")
    test_unsorted = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"Original list: {test_unsorted}")
    print(f"Bubble sorted: {bubble_sort(test_unsorted.copy())}")
    print(f"Selection sorted: {selection_sort(test_unsorted.copy())}")
    print()
    
    # Compare performance
    print("Algorithm Performance Comparison:")
    compare_search_algorithms()
    compare_sorting_algorithms()
