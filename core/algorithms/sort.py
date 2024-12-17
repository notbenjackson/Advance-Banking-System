def merge_sort(arr):
    """Merge Sort Algorithm"""
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    """Merge two sorted arrays"""
    result = []
    left_index = right_index = 0
    
    # Compare and merge elements
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    
    # Add remaining elements
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    
    return result

def quick_sort(arr):
    """Quick Sort Algorithm"""
    if len(arr) <= 1:
        return arr
    
    # Choose the pivot (last element)
    pivot = arr[-1]
    
    # Partition the array
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    # Recursively sort partitions
    return quick_sort(left) + [pivot] + quick_sort(right)