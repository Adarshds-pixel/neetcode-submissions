class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        max_length=0
        length=0
        for num in nums:
            if num-1 not in nums:
                current_element=num
                length=1
                while current_element+1 in nums:
                    length+=1
                    current_element+=1
                max_length=max(length,max_length)
        return max_length


        