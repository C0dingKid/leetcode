class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lol = set(nums)
        longest = 0

        for num in lol:
            if num-1 not in lol:
                length = 1
                while num + length in lol:
                    length += 1
                longest = max(length,longest)
        return longest
                
