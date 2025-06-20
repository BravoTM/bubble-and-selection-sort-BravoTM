def bubble_sort(unsorted_list):
    # Create a copy to avoid modifying the original list
    sorted_list = unsorted_list.copy()
    n = len(sorted_list)
    
    # Outer loop: controls number of passes
    for i in range(n):
        # Flag to optimize - check if any swaps occurred
        swapped = False
        
        # Inner loop: does adjacent comparisons
        for j in range(n - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                # Swap elements if out of order
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
                swapped = True
        
        # If no swaps in a complete pass, list is sorted
        if not swapped:
            break
    
    return sorted_list