from collections import defaultdict
from sys import argv
script = argv[0]
filename = argv[1]
fileout = argv[2]
dd = defaultdict(int)
with open(filename,'r') as f:
    for line in f:
        words = line.split('\t')
        for word in words:
            dd[word]  += 1

with open(fileout, 'w') as file:
	for k,v in dd.items():
		file.write(k+': '+str(v)+'\n')