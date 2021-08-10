#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Question 2.
-----------

There is a fair in a city that contains N shops.
The shops are arranged in a straight line at 1, 2, ..., N positions.
M persons come to the fair and each visits shops in the [L, R] inclusively.

Determine the three most popular shops.
The task is to fix the code, not to rewrite it.


Constraints
-----------

* 1 <= N <= 10

* 3 <= N, M <= 10e5

* 1 <= L <= R <= N


Examples
--------

Input:

  1) 1 (one test case)
  
  2) 6 5 (N shops and M visitors)
  
  3-1) 3 5
  
  3-2) 2 3
  
  3-3) 4 6
  
  3-4) 1 6
  
  3-5) 5 6

Output:

  * 3 4 5

"""


__author__ = "unknown"


def solve(N, M, visit):
    # fix bugs in this function
    cnt = [0] * N
    for i in range(M):
        l, r = visit[i]
        cnt[l - 1] += 1
        cnt[r - 1] += 1
    
    for i in range(1, len(cnt) - 1):
        cnt[i] += cnt[i - 1]
    
    top3 = []
    for _ in range(3):
        top = cnt.index(max(cnt))
        del cnt[top]
        top3.append(top + 1)
    return sorted(top3)


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    visit = [list(map(int, input().split())) for i in range(M)]
    
    out_ = solve(N, M, visit)
    print (' '.join(map(str, out_)))
