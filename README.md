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

3. subset the blast result (from step 2) by specifying an e-value, and convert the best hits to a count table:
    ```
    Rscript convert_bests_to_counts.R BEST_HITS.txt MAX_E-VALUE OUTPUT_COUNTS.txt
    ```

