#!/usr/bin/python
import sys
import string
import os
f = open('triangle.in', 'r')
line = f.readline()
inputdata = string.split(str(line), ' ')
p = float(inputdata[0])
q = float(inputdata[1])
f.close()
f = open('triangle.out', 'w')
f.write("%.1f\n" % ((p*q)/2))
f.write("%.6f %.6f\n" % (0.0, 0.0))
f.write("%.6f %.6f\n" % (p, 0.0))
f.write("%.6f %.6f" % (0.0, q))
f.close()

