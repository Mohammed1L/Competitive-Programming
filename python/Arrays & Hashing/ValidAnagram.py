# LeetCode 242 - Valid Anagram
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-anagram/
#
# Problem:
# Given two strings s and t, return True if t is an anagram of s,
# otherwise return False.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = {}
        str2 = {}
        for i in s: 
           str1[i] = str1.get(i,0) + 1

        for i in t: 
             str2[i] = str2.get(i,0) + 1

 
        if str2 == str1: 
            return True
        return False
