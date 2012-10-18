#!/usr/bin/python
import sys
import string
import os

InputFile = 'triangle.in'
OutputFile = 'triangle.out'

f = open(InputFile, 'r')
line = f.readline()
inputdata = string.split(str(line), ' ')
p = float(inputdata[0])
q = float(inputdata[1])
print p, q
f.close()
f = open(OutputFile, 'w')
f.write("%.1f\n" % ((p*q)/2))
f.write("%.6f %.6f\n" % (0.0, 0.0))
f.write("%.6f %.6f\n" % (p, 0.0))
f.write("%.6f %.6f\n" % (0.0, q))
f.close()
