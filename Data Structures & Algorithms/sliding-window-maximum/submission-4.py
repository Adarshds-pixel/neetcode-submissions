class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left=0
        max_element=max(nums[left:k])
        res=[]
        res.append(max_element)
        for right in range(k,len(nums)):
            outgoing_element=nums[left]
            left+=1
            if outgoing_element==max_element:
                max_element=max(nums[left:right+1])
            else:
                max_element=max(max_element,nums[right])
            res.append(max_element)
        return res
        