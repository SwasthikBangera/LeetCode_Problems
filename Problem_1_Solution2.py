#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 14:43:39 2023

@author: yennamac
"""

#LeetCode Problem #1 - Solution 2

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        
        for i, num in enumerate(nums):
            if target - num in seen:
                return([seen[target-num], i])
            elif num not in seen:
                seen[num] = i