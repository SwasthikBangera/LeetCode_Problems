#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 15:28:24 2023

@author: Swasthik Bangera


Problem statement: A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing 
all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_str = ""
        
        for c in s:
            if c.isalnum():
                new_str += c.lower()
        return new_str == new_str[::-1]
    
        
        
        