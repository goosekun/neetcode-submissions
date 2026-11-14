class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        my_list = []
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                my_list.append(count)
                count = 0
        my_list.append(count)
        my_list = sorted(my_list, reverse=True)
        print(my_list)
        return my_list[0]