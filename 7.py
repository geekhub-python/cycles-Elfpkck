#!/usr/bin/env python3
# -*- coding: utf-8 -*-

dist = 10
day = 1
sum_dist = 10
n = int(input('Enter days quantity: '))
check1 = check2 = check3 = check4 = True
while check1 or check2 or check3 or check4:
    if day in range(2, 11):
        print('а) day: {}, distance = {:.1f} km'. format(day, dist))
        if day == 10:
            check1 = False
    if day == 7:
        print('б) day: {}, total distance = {:.1f} km'.format(day, sum_dist))
        check2 = False
    if day == n:
        print('в) day: {}, total distance = {:.1f} km'.format(day, sum_dist))
        check3 = False
    if sum_dist > 80 and check4:
        print('г) stop! day: {}'.format(day - 1))
        check4 = False
    day += 1
    dist *= 1.1
    sum_dist += dist