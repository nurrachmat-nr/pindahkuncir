#!/usr/bin/python

# Copyright 2013 Joe Walnes and the websocketd team.
# All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from sys import stdin, stdout
from time import sleep
while True:
    x = open('bin/data.txt','r')
    y = x.read()
    print(y)
    stdout.flush()
    x.close()
    sleep(0.2)