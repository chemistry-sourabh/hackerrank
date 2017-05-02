#!/bin/python
# Problem link https://www.hackerrank.com/challenges/grading


def solve(grades):
    rounded = []
    for grade in grades:
        if grade < 38:
            rounded.append(grade)
        else:
            next_5 = int(grade / 5) * 5 + 5
            if next_5 - grade < 3:
                rounded.append(next_5)
            else:
                rounded.append(grade)
    return rounded


n = int(raw_input().strip())
grades = []
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))
