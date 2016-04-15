## for i in *.m8; do python blast-m8-parser-best_to_1_file.py $i; done > all_best.txt
import sys

f = sys.argv[1]
arg = f.split('.x.')[0].split('.')[0]
metag = f.split('.x.')[1].split('.')[0]

d = {}

for line in open(f):
    data = line.rstrip().split('\t')
    query = data[0]
    hit = data[1]
    if d.has_key(query):
        continue
    else:
        d[query] = hit
	print arg + "\t" + str(metag) + "\t" + line,
       # print line, 
