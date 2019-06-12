# coding=utf-8
#exec(open('setup.py').read())
import sys
from yacryptopan import CryptoPAn

def getFile():
    datContent = [i.strip().split() for i in open(sys.argv[1]).readlines()]
    for x in datContent:
        x[4] = getCryptopan(x[4])
        x[5] = getCryptopan(x[5])
    return datContent

def getCryptopan(address):
    cp = CryptoPAn(b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    return cp.anonymize(address)

def toTextFile():
    list = []
    for line in getFile():
        string = ''
        for field in line:
            string += field + "\t"
        list.append(string)

    outF = open(sys.argv[2], "w")
    for line in list:
        outF.write(str(line))
        outF.write("\n")
    print("Created file",sys.argv[2])
    outF.close()

if __name__ == '__main__':
    toTextFile()
