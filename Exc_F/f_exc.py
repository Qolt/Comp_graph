#!/usr/bin/python
import sys
import string
import os

InputFile = 'triangle.in'
OutputFile = 'triangle.out'

def GetFloat(s, default):
  try:
    i = float(s)
  except ValueError:
    i = default
  return i

def GetInputData():
    position = []
    inputdata = []
    checkdata = []
    try:
        f = open(os.path.join(os.getcwd(), InputFile), 'r')
        length = f.readlines()
        if (len(length) == 0 ):
            print "Failed to parse input file."
            sys.exit(1)
        else:
            for line in length:
                inputdata = string.split(str(line), ' ')
                for i, item in enumerate(inputdata):
                    try:
                        checkdata.append(float(inputdata[i]))
                    except:
                        print ""
                position.append(checkdata)
                inputdata = [] 
                checkdata = [] 
        f.close()
    except IOError, e:
        print "I/O error ({0}) " + InputFile + ": {1}".format(e.errno, e.strerror)
        raise SystemExit(1)
        
    return position 

def calc(p_aux):
    answer =(p_aux[0][0] * p_aux[0][1])/2
    p_precomp = []
    p_precomp.append([answer])
    coord = []
    coord.append(0.000000)
    coord.append(0.000000)
    p_precomp.append(coord)
    coord = []
    coord.append(p_aux[0][0])
    coord.append(0.000000)
    p_precomp.append(coord)
    coord = []
    coord.append(0.000000)
    coord.append(p_aux[0][1])
    p_precomp.append(coord)
    return p_precomp

def MakeOutput(p_aux):
    try:
        f = open(OutputFile, "w")
        for p_precomp in p_aux:
            for i, item in enumerate(p_precomp):
                if i != (len(p_precomp) - 1):
                    f.write("%.6f " % (p_precomp[i]))
                else:
                    f.write("%.6f\n" % (p_precomp[i]))
        f.close()
    except IOError, e:
        print "I/O error ({0}) " + OutputFile + ": {1}".format(e.errno, e.strerror)
        raise SystemExit(1)


def main():
    Inputdata = GetInputData()
    print Inputdata 
    ans = calc(Inputdata)
    print ans
    MakeOutput(ans)

main()


