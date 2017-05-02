#!/bin/python
# Problem link https://www.hackerrank.com/challenges/apple-and-orange


def convert_to_pos(tpos, dees):
    poses = []
    for d in dees:
        poses.append(tpos + d)
    return poses


def fell_on_house(s, t, poses):
    on_house = 0
    for pos in poses:
        if s <= pos <= t:
            on_house += 1
    return on_house


s, t = raw_input().strip().split(' ')
s, t = [int(s), int(t)]
a, b = raw_input().strip().split(' ')
a, b = [int(a), int(b)]
m, n = raw_input().strip().split(' ')
m, n = [int(m), int(n)]
apple = map(int, raw_input().strip().split(' '))
orange = map(int, raw_input().strip().split(' '))

applex = convert_to_pos(a, apple)
orangex = convert_to_pos(b, orange)

print fell_on_house(s, t, applex)
print fell_on_house(s, t, orangex)
