#!/usr/bin/python

from sys import stdin, stdout

while True:
    line = stdin.readline().strip()
    if len(line) != 0:
        x = open('bin/data.txt','w')
        x.write(line)
        x.close()
        print(line)
        stdout.flush()