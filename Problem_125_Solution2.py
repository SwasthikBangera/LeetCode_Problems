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
        
        

    
# Algorithm to equate if all values are same from both side left (l) and right (r)
        l, r = 0, len(s)-1
        
        while l<r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while r > l and not self.alphanum(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            # To move to next positions
            l, r = l + 1, r - 1
        
        return True
            
        
# Function to determine if 'c' is alphanumeric or not
    def alphanum(self, c):
        return(ord('A') <= ord(c) <= ord('Z') or
               ord('a') <= ord(c) <= ord('z') or
               ord('0') <= ord(c) <= ord('9'))           
            
            

        
        
        