import time
import sys
from subprocess import call

def getData(fileName):
    f = open(fileName,"r")
    data = f.read()
    f.close()
    return data

fileName = sys.argv[1]
sleepTime = 2
command = ["make",sys.argv[2]]

data = getData(fileName)
while True:
    data2 = getData(fileName)
    if data != data2:
        call(command)
        data = data2
    time.sleep(sleepTime)

