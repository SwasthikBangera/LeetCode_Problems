#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 11:34:33 2023

@author: yennamac
"""
'''

Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False 