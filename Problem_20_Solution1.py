#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 14:43:39 2023

@author: yennamac
"""

#LeetCode Problem #20 - Solution 1

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed_to_open = {")" : "(", "]" : "[", "}" : "{"}
        
        for c in s:
            if c in closed_to_open:
                if stack and stack[-1] == closed_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False