import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    heap = []
    reverse_sorted = []

    for num in nums:
        pair = (-num, num)
        heapq.heappush(heap, pair)
    
    while heap:
        pair = heapq.heappop(heap)
        original_number = pair[1]
        reverse_sorted.append(original_number)

    return reverse_sorted



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
