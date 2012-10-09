#!/usr/bin/python
import sys
import string
import os
import math

InputFile = 'radius.in'
OutputFile = 'radius.out'

def GetFloat(s, default):
  try:
    i = float(s)
  except ValueError:
    i = default
  return i

def GetInputData():
    try:
        f = open(os.path.join(os.getcwd(), InputFile), 'r')
        length = f.readline()
        if (len(length) == 0 ):
            print "Failed to parse input file."
            sys.exit(1)
        else:
            tmp_radius = string.split(length, ' ', 1)
        radius = GetFloat(tmp_radius[0], 0)
        if radius < 0:
            print "Invalid radius value"
            raise SystemExit(1)
        f.close()
    except IOError, e:
        print "I/O error ({0}) " + InputFile + ": {1}".format(e.errno, e.strerror)
        raise SystemExit(1)
    return radius

def calc_c(radius):
    return 2 * math.pi * radius

def calc_d(c):
    return c / math.pi

def calc_s(r):
    return math.pi * r**2

def MakeOutput(p_precomp):
    try:
        f = open(OutputFile, "w")
        f.write("%.3f %.3f %.3f\n" % (p_precomp[1], p_precomp[0], p_precomp[2]))
        f.close()
    except IOError, e:
        print "I/O error ({0}) " + OutputFile + ": {1}".format(e.errno, e.strerror)
        raise SystemExit(1)
    except:
        print "Unknown error while write " + OutputFile + ": file"
        raise SystemExit(1)

def main():
    radius = GetInputData()
    print radius
    ans = []
    ans.append(calc_c(radius))
    ans.append(calc_d(ans[0]))
    ans.append(calc_s(radius))
    print "%.3f %.3f %.3f" % (ans[1], ans[0], ans[2])
    MakeOutput(ans)
main()


