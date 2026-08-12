class Solution:
    def trap(self, height: List[int]) -> int:
        left_max=[0]*len(height)
        right_max=[0]*len(height)
        curr_left_max=0
        curr_right_max=0
        water=0
        for left in range(len(height)):
            curr_left_max=max(curr_left_max,height[left])
            left_max[left]=curr_left_max
        for right in range(len(height)-1,-1,-1):
            curr_right_max=max(curr_right_max,height[right])
            right_max[right]=curr_right_max
        for i in range(len(height)):
            water+=min(left_max[i],right_max[i])-height[i]

        return water