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
        
        # Using Counter command in Python
        return Counter(s) == Counter(t)
        

            
        
        
        