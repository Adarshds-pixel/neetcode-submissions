class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq={}
        for i,num in enumerate(nums):
            res=target-num
            if res in freq:
                return [freq[res],i]
            freq[num]=i
        