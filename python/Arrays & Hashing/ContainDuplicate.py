# LeetCode 217 - Contains Duplicate
# Difficulty: Easy
# Link: https://leetcode.com/problems/contains-duplicate/
#
# Problem:
# Given an integer array nums, return True if any value appears more than once
# in the array, otherwise return False.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dub = {}

        for i in nums:
            dub[i] = dub.get(i, 0) + 1

        for i in dub:
            if dub[i] > 1:
                return True

        return False