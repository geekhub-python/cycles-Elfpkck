#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import string


s = string.ascii_lowercase
i = 0
while i < len(s):
    print(s[i:i+5])
    i += 5