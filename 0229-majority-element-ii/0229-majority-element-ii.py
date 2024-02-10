from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        els = []
        for k, v in Counter(nums).items():
            if v > len(nums) // 3:
                els.append(k)
        return els