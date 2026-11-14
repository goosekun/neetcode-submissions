class Solution:
    def resize(self, arr: list[int]) -> list[int]:
        length = len(arr)
        capacity = length * 2
        my_arr = [0] * capacity
        
        for i in range(0, length):
            my_arr[i] = arr[i]
        
        for i, k in enumerate(range(length, capacity)):
            my_arr[k] = arr[i]
        return my_arr
        

    def getConcatenation(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            new_arr = self.resize(nums)
        
        return new_arr