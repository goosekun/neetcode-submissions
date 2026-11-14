class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i, num in enumerate(nums):
            if num == val:
                nums[i] = -1
        nums.sort(reverse=True)
        print(nums)

        i = 0
        count = 0 
        while i < len(nums):
            if nums[i] == -1:
                break
            count += 1
            i += 1
        
        return count