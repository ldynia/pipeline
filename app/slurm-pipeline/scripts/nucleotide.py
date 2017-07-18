#!/usr/bin/env python3
import os

output = os.popen("ssh nucleotide ntcount -f /pipeline/data/dna.fsa").read()

with open("/pipeline/results/ntcount.json.out", "w") as data_file:
    data_file.write(output)
