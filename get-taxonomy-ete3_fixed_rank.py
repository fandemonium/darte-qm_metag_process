from ete3 import NCBITaxa
import sys
import collections

#This script uses python module ete3 to query NCBI taxonomy hierarchy for corresponding NCBI taxID
```
The input file, ncbi_gi_taxid_file, resemles a tab delimited two column table,
where the first column is the NCBI gene id, the second column is the NCBI taxID. 

The output file, output.txt, is a four column table, 
where the first column is the NCBI gene id, the second column is the NCBI taxID, the third column is the taxonomy rank (e.g, phylum), and the fourth column is the calssification at the taxonomy rank (e.g., Proteobacteria)

The output does not contain header. It's also in long table format as known in R. The output can be converted to the traditional wide table format in R using "reshape2".
```

if len(sys.argv) == 1:
	sys.exit("USAGE: python %s <path/to/ncbi_gi_taxid_file> > <output.txt>" % sys.argv[0])

ncbi = NCBITaxa()
#ncbi.update_taxonomy_database()

fp = open('taxa-ids-not-found.txt', 'w')
hier = ["kingdom", "phylum", "class", "order", "family", "genus", "species"]

for x in open(sys.argv[1]):
    dat = x.rstrip().split('\t')[-1]
    try:
        lineage = ncbi.get_lineage(dat)
	names = ncbi.get_taxid_translator(lineage)
	ranks = ncbi.get_rank(lineage)
	
	new_ranks = {}
	for keys in ranks:
		if ranks[keys] in hier:
			new_ranks[keys]=ranks[keys]
        
	d = {}
        for taxid in lineage and new_ranks:
		d[new_ranks[taxid]] = names[taxid]
	
	for key in sorted(d):
		print x.rstrip() + "\t"+ str(key)+"\t"+d[key]
    except ValueError:
        fp.write('%s\n' % x.rstrip())




