class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i, num in enumerate(arr):
            if i == len(arr) - 1:
                arr[i] = -1
                break
            max_elem = 0
            for j in range(i+1, len(arr)):
                if arr[j] > max_elem:
                    max_elem = arr[j]
            arr[i] = max_elem
        return arr