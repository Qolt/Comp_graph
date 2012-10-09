#!/usr/bin/python
import sys
import string
import os

InputFile = 'sum.in'
OutputFile = 'sum.out'

def GetFloat(s, default):
  try:
    i = float(s)
  except ValueError:
    i = default
  return i

def GetInputData():
    position = []
    inputdata = []
    try:
        f = open(os.path.join(os.getcwd(), InputFile), 'r')
        length = f.readlines()
        if (len(length) == 0 ):
            print "Failed to parse input file."
            sys.exit(1)
        else:
            for line in length:
                inputdata = string.split(str(line), ' ')
                position.append(inputdata)
                inputdata = [] 
        f.close()
    except IOError, e:
        print "I/O error ({0}) " + InputFile + ": {1}".format(e.errno, e.strerror)
        raise SystemExit(1)
    return position 

def main():
    Inputdata = GetInputData()
    print Inputdata 

main()


