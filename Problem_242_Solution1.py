#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 14:34:39 2023

@author: Swasthik Bangera


Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically 
using all the original letters exactly once.

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Determine if length of the strings are same
        if len(s) != len(t):
            return False
        
        count_s, count_t = {}, {}
        
        # Determine counts of the alphabets in each string
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i],0)
            count_t[t[i]] = 1 + count_t.get(t[i],0)
        
        # Compare the counts in the two strings
        for c in count_s:
            if count_s[c] != count_t.get(c, 0):
                return False
        
        return True

            
        
        
        