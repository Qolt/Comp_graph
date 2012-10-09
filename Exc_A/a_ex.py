#!/usr/bin/python
import sys
import string
import os

InputFile = 'vector.in'
OutputFile = 'vector.out'

def GetFloat(s, default):
  try:
    i = float(s)
  except ValueError:
    i = default
  return i

def GetInputData():
    position = []
    try:
        f = open(os.path.join(os.getcwd(), InputFile), 'r')
        length = f.readline()
        if (len(length) == 0 ):
            print "Failed to parse input file."
            sys.exit(1)
        else:
            coord = string.split(length, ' ', 3)
            for i in coord:
                position.append(GetFloat(i, 0))
        f.close()
    except IOError, e:
        print "I/O error ({0}) " + InputFile + ": {1}".format(e.errno, e.strerror)
        raise SystemExit(1)
    except:
        print "Unknown error while open " + InputFile + ": file"
        raise SystemExit(1)
    return position

def GetLength(position):
    length = ((position[0])**2 + (position[1])**2 + (position[2])**2)**0.5
    return length

def MakeOutput(p_precomp):
    try:
        f = open(OutputFile, "w")
        f.write("%.2f\n" % (p_precomp))
        f.close()
    except IOError, e:
        print "I/O error ({0}) " + OutputFile + ": {1}".format(e.errno, e.strerror)
        raise SystemExit(1)
    except:
        print "Unknown error while write " + OutputFile + ": file"
        raise SystemExit(1)

def main():
    position = GetInputData()
    print position 
    length = GetLength(position)
    print "Vector length: %.2f" % (length)
    MakeOutput(length)
main()
