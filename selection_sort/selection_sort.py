def selection_sort(unsorted_list):
    # Create a copy to avoid modifying the original list
    sorted_list = unsorted_list.copy()
    n = len(sorted_list)
    
    # Traverse through all list elements
    for i in range(n):
        # Assume the current position is the minimum
        min_idx = i
        
        # Find the actual minimum in the remaining unsorted portion
        for j in range(i+1, n):
            if sorted_list[j] < sorted_list[min_idx]:
                min_idx = j
                
        # Swap the found minimum with the current element
        sorted_list[i], sorted_list[min_idx] = sorted_list[min_idx], sorted_list[i]
    
    return sorted_list