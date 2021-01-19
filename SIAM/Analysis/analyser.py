import sys

# Print total number of arguments
print ('Total number of arguments:', format(len(sys.argv)))
 
# Print all arguments
print ('Argument List:', str(sys.argv))

iDir = sys.argv[1]
oDir = sys.argv[2]

iFile = open(iDir, "r")
oFile = open(oDir, "w")

data = iFile.readlines()
patterns = []

for line in data:
    if line[0] is 'T':
        patterns.append(line)

for p in patterns:
    print(p)
oFile.write("ah yes, beautiful music")