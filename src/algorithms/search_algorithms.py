from typing import List, Any, Optional

class SearchAlgorithms:
    @staticmethod
    def linear_search(arr: List[Any], target: Any) -> Optional[int]:
        """
        Perform linear search on an array
        
        Args:
            arr (List[Any]): Input array to search
            target (Any): Element to find
        
        Returns:
            Optional[int]: Index of target if found, None otherwise
        """
        for i, item in enumerate(arr):
            if item == target:
                return i
        return None

    @staticmethod
    def binary_search(arr: List[Any], target: Any) -> Optional[int]:
        """
        Perform binary search on a sorted array
        
        Args:
            arr (List[Any]): Sorted input array
            target (Any): Element to find
        
        Returns:
            Optional[int]: Index of target if found, None otherwise
        """
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return None

    @staticmethod
    def exponential_search(arr: List[Any], target: Any) -> Optional[int]:
        """
        Perform exponential search on a sorted array
        
        Args:
            arr (List[Any]): Sorted input array
            target (Any): Element to find
        
        Returns:
            Optional[int]: Index of target if found, None otherwise
        """
        if arr[0] == target:
            return 0

        # Find range for binary search
        i = 1
        while i < len(arr) and arr[i] <= target:
            i *= 2

        # Perform binary search in found range
        return SearchAlgorithms.binary_search(
            arr[:min(i, len(arr))], 
            target
        )

    @staticmethod
    def jump_search(arr: List[Any], target: Any) -> Optional[int]:
        """
        Perform jump search on a sorted array
        
        Args:
            arr (List[Any]): Sorted input array
            target (Any): Element to find
        
        Returns:
            Optional[int]: Index of target if found, None otherwise
        """
        n = len(arr)
        step = int(n ** 0.5)  # Square root of array length
        
        prev = 0
        while arr[min(step, n) - 1] < target:
            prev = step
            step += int(n ** 0.5)
            
            if prev >= n:
                return None

        # Linear search in block
        while arr[prev] < target:
            prev += 1
            
            if prev == min(step, n):
                return None

        # Check if target is found
        if arr[prev] == target:
            return prev

        return None

    @staticmethod
    def interpolation_search(arr: List[Any], target: Any) -> Optional[int]:
        """
        Perform interpolation search on a sorted array
        
        Args:
            arr (List[Any]): Sorted input array
            target (Any): Element to find
        
        Returns:
            Optional[int]: Index of target if found, None otherwise
        """
        left, right = 0, len(arr) - 1

        while left <= right and arr[left] <= target <= arr[right]:
            # Interpolation formula
            pos = left + int(
                ((float(right - left) / (arr[right] - arr[left])) * 
                 (target - arr[left]))
            )

            if arr[pos] == target:
                return pos
            
            if arr[pos] < target:
                left = pos + 1
            else:
                right = pos - 1

        return None