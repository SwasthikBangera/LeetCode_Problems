#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Swasthik Bangera

Problem statement: Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res






            