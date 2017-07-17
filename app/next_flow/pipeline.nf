process codon {
  output:
    file 'codon.json' into codons
  script:
    template 'codon.sh'
}

process nucleotide {
  output:
    file 'nucleotide.json' into nucleotides
  script:
    template 'nucleotide.sh'
}
