#!/usr/bin/env nextflow

// https://www.nextflow.io/docs/latest/example.html
// https://www.nextflow.io/docs/latest/process.html#output-files

params.in = "/pipeline/data/dna.fsa"
sequences = file(params.in)

process splitSequences {
    input:
      file 'input.fa' from sequences
    output:
      file 'seq_*' into records
    """
    csplit input.fa '%^>%' '/^>/' '{*}' -f seq_
    """
}

process reverse {
    input:
      file x from records
    output:
      file 'out.fa' into result
    """
    cat $x | rev > out.fa
    """
}

result.subscribe { println it }
