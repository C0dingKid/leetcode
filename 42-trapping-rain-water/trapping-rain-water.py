class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        lmax = height[l]
        rmax = height[r]
        res = 0

        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(height[l], lmax) 
                if height[l] < lmax:
                    res += lmax - height[l]
            else:
                r -= 1
                rmax = max(height[r], rmax)
                if height[r] < rmax:
                    res += rmax - height[r]
        return res