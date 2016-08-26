import time
import sys
from subprocess import call

def usage():
    print "usage: " + sys.argv[0] + " <file to watch> <make command (optional)>"

def getData(fileName):
    f = open(fileName,"r")
    data = f.read()
    f.close()
    return data

numArgs = len(sys.argv)
fileName = sys.argv[1]
sleepTime = 2

if numArgs < 2:
    usage()
    exit()

command = "make"
if numArgs > 2:
    command = [command,sys.argv[2]]

data = getData(fileName)
while True:
    data2 = getData(fileName)
    if data != data2:
        call(command)
        data = data2
    time.sleep(sleepTime)

