# darte-qm_metag_process

## General purpose

This repo contains scripts used to process multiple gene blast hits from metagenomics.
In this case, multiple genes used as blast database are RESFAM antibiotic resistance genes
from different families. Blast queries are metagenomic sequences available publically.

## Procedures
1. Run blast (diamond blast in our case) and obtain m8 table output (i.e., GENE.x.METAG.*.m8)

2. Obtain best hits and combine them into one file:
    ```
    for i in GENE.x.METAG.*.m8; do python blast-m8-parser-best_to_1_file.py $i; done > OUTPUT.txt
    ```

3. 
_taxid_get_taxa.qsub
-rw-r--r--  1 fanyang  staff   1.5K Apr 15 11:28 get-taxonomy-ete3_fixed_rank.py
-rw-r--r--  1 fanyang  staff   844B Apr 15 13:02 blast-m8-parser-best_to_1_file.py
-rw-------  1 fanyang  staff   1.3K Apr 15 13:31 convert_bests_to_counts.R
