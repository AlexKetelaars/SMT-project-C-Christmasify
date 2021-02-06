import sys
import os

# Print total number of arguments
print ('Total number of arguments:', format(len(sys.argv)))
 
# Print all arguments
print ('Argument List:', str(sys.argv))

iDir = sys.argv[1]
ascending = 0
descending = 0
flat = 0
mixed = 0

for dirname in os.listdir(iDir):
    cosFile = dirname
    for i in range(28):
        cosFile = cosFile[:-1]
    f = open(iDir + dirname + "\\" + cosFile + "-chrom.cos", "r")
    for line in f.readlines():
        newLine = False
        if line[0] is "T":
            patternHeights = []
            newLine = True
            patternFound = False
            for idx in range(len(line)):
                 if line[idx] is "p":
                     patternFound = True
                 if patternFound and line[idx] is ",":
                     patternHeights.append(int(line[idx + 1] + line[idx + 2]))
                     patternFound = False
            prev = 0
            firstTime = True
            a = False
            d = False
            f = False
            for height in patternHeights:
                if firstTime:
                     prev = height
                     firstTime = False
                elif prev is height:
                     f = True
                elif prev > height:
                     d = True
                else:
                     a = True
            if a:
                if d:
                     mixed += 1
                else:
                     ascending += 1
            elif d:
                if a:
                     mixed += 1
                else:
                     descending +=1
            else:
                 flat += 1

        #print(patternHeights)        
print(ascending)
print(descending)
print(flat)
print(mixed)                
