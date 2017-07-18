#!/usr/bin/env python3
import os

output = os.popen("ssh codon cdncount -f /pipeline/data/dna.fsa").read()

with open("/pipeline/results/cdncount.json.out", "w") as data_file:
    data_file.write(output)
