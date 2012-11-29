#!/usr/bin/python
import sys
import string
import os
f = open('twoc.in', 'r')
inputdata = string.split(str(f.readline()), ' ')
f.close()
for i, item  in enumerate(inputdata):
    inputdata[i] = float(inputdata[i])
dist = ((inputdata[0] - inputdata[2])**2 + (inputdata[1] - inputdata[3])**2)**0.5
print dist
print inputdata
ans = ""
if (dist == inputdata[5] + inputdata[4]):
    ans = "Tangent: outside"
if ((inputdata[4] == inputdata[5] + dist) and (ans == "")):
    ans = "Tangent: 2 in 1"
if ((inputdata[5] == inputdata[4] + dist) and (ans == "")):
    ans = "Tangent: 1 in 2"
if ((inputdata[4] > dist) and (ans == "") and (inputdata[5] < inputdata[4])):
    ans = "2 inside 1"
if ((inputdata[5] > dist) and (ans == "") and (inputdata[5] > inputdata[4])):
    ans = "1 inside 2"
if ((dist > inputdata[4] + inputdata[5]) and (ans == "")):
    ans = "Too far"
if (ans == ""):
    ans = "Intersect"
print ans
f = open('twoc.out', "w") 
f.write(ans)
f.close()
