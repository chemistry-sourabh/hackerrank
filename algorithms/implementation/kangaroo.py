#!/bin/python
# Problem Link https://www.hackerrank.com/challenges/kangaroo


x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]

num = x2 - x1
den = v1 - v2

if den != 0:
    v = num / den
    rem = num % den
    if v > 0 and rem == 0:
        print "YES"
    else:
        print "NO"
else:
    print "NO"
