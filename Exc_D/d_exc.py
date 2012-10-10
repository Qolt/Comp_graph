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

def calc(p_aux):
    ans = []
    for i, item in enumerate(p_aux[1]):
        ans.append(GetFloat(p_aux[1][i], 0) + GetFloat(p_aux[2][i], 0))
    return ans

def MakeOutput(p_precomp):
    try:
        f = open(OutputFile, "w")
        for i, item in enumerate(p_precomp):
            if i != (len(p_precomp) - 1):
                f.write("%.3f " % (p_precomp[i]))
            else:
                f.write("%.3f" % (p_precomp[i]))
        f.close()
    except IOError, e:
        print "I/O error ({0}) " + OutputFile + ": {1}".format(e.errno, e.strerror)
        raise SystemExit(1)
    except:
        print "Unknown error while write " + OutputFile + ": file"
        raise SystemExit(1)

def main():
    Inputdata = GetInputData()
    print Inputdata 
    ans = calc(Inputdata)
    print ans
    MakeOutput(ans)

main()


