from typing import List, Any

class SortAlgorithms:
    @staticmethod
    def bubble_sort(arr: List[Any]) -> List[Any]:
        """
        Perform bubble sort
        
        Args:
            arr (List[Any]): Input array to sort
        
        Returns:
            List[Any]: Sorted array
        """
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    @staticmethod
    def insertion_sort(arr: List[Any]) -> List[Any]:
        """
        Perform insertion sort
        
        Args:
            arr (List[Any]): Input array to sort
        
        Returns:
            List[Any]: Sorted array
        """
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            
            arr[j + 1] = key
        
        return arr

    @staticmethod
    def merge_sort(arr: List[Any]) -> List[Any]:
        """
        Perform merge sort
        
        Args:
            arr (List[Any]): Input array to sort
        
        Returns:
            List[Any]: Sorted array
        """
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = SortAlgorithms.merge_sort(arr[:mid])
        right = SortAlgorithms.merge_sort(arr[mid:])

        return SortAlgorithms._merge(left, right)

    @staticmethod
    def _merge(left: List[Any], right: List[Any]) -> List[Any]:
        """
        Merge two sorted arrays
        
        Args:
            left (List[Any]): First sorted array
            right (List[Any]): Second sorted array
        
        Returns:
            List[Any]: Merged sorted array
        """
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    @staticmethod
    def quick_sort(arr: List[Any]) -> List[Any]:
        """
        Perform quick sort
        
        Args:
            arr (List[Any]): Input array to sort
        
        Returns:
            List[Any]: Sorted array
        """
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return (SortAlgorithms.quick_sort(left) + 
                middle + 
                SortAlgorithms.quick_sort(right))

    @staticmethod
    def heap_sort(arr: List[Any]) -> List[Any]:
        """
        Perform heap sort
        
        Args:
            arr (List[Any]): Input array to sort
        
        Returns:
            List[Any]: Sorted array
        """
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and arr[left] > arr[largest]:
                largest = left

            if right < n and arr[right] > arr[largest]:
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        