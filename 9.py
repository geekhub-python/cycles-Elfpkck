#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string


s = input('Enter a letter: ').lower()
abc = string.ascii_lowercase * 2
for item in abc:
    if s == item:
        index = abc.find(s)
        for i in range(1, 4):
            print(abc[index + i])
        break