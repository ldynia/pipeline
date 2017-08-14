process codon {
  output:
    file 'cdncount.json.out'
  script:
    template 'codon.sh'
}

process nucleotide {
  output:
    file 'ntcount.json.out'
  script:
    template 'nucleotide.sh'
}
