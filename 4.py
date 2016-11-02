#!/usr/bin/env python3
# -*- coding: utf-8 -*-

i = 1
while True:
    if (i % 11 == 0
            and i % 2 == 1
            and i % 3 == 1
            and i % 4 == 1
            and i % 5 == 1
            and i % 6 == 1
            and i % 7 == 1
            and i % 8 == 1
            and i % 9 == 1
            and i % 10 == 1):
        print(i)
        break
    i += 1