# trapping rain wafer
class Solution:
    def trap(self, height: List[int]) -> int:
        len_h = len(height)
        if len_h <= 2:
            return 0
        max_h = max(height)
        vol_bef = sum(height)

        l = 0
        max_l = 0
        while height[l] < max_h:
            if height[l] > max_l:
                max_l = height[l]
            height[l] = max_l
            l += 1

        r = len_h - 1
        max_r = 0
        while height[r] < max_h:
            if height[r] > max_r:
                max_r = height[r]
            height[r] = max_r
            r -= 1

        vol_aft = sum(height[:l]) + sum(height[r:]) + (r - l) * max_h
        return vol_aft - vol_bef
