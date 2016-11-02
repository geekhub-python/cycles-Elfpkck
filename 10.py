#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import string


low = string.ascii_lowercase
up = string.ascii_uppercase
digit = string.digits

all = [random.choice(up) for i in range(2)]
all.extend([int(random.choice(digit)) for i in range(5)])
all.extend(random.choice(low) for i in range(10))
all.append('_')
random.shuffle(all)

pswd = str(all[0])
for i in range(len(all) - 1):
    if isinstance(all[i], int) and isinstance(all[i+1], int):
        continue
    pswd += str(all[i+1])
print(pswd)
