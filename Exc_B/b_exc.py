#!/usr/bin/python
import sys
import string
import os

InputFile = 'line.in'
OutputFile = 'line.out'

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
            inputdata = string.split(length, ' ', 3)
            for i in inputdata:
                position.append(GetFloat(i, 0))
        f.close()
    except IOError, e:
        print "I/O error ({0}) " + InputFile + ": {1}".format(e.errno, e.strerror)
        raise SystemExit(1)
    except:
        print "Unknown error while open " + InputFile + ": file"
        raise SystemExit(1)
    return position

def GetLine(coord):
    ans = []
    ans.append(coord[1] - coord[3])
    ans.append(coord[2] - coord[0])
    ans.append(coord[0]*coord[3] - coord[2]*coord[1])
    return ans

def MakeOutput(p_precomp):
    try:
        f = open(OutputFile, "w")
        f.write("%.3f %.3f %.3f\n" % (p_precomp[0], p_precomp[1], p_precomp[2]))
        f.close()
    except IOError, e:
        print "I/O error ({0}) " + OutputFile + ": {1}".format(e.errno, e.strerror)
        raise SystemExit(1)
    except:
        print "Unknown error while write " + OutputFile + ": file"
        raise SystemExit(1)

def main():
    coord = GetInputData()
    print coord
    ans = GetLine(coord)
    print ans
    MakeOutput(ans)

main()
