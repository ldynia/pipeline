import luigi
from codon import CodonTask
from nucleotide import NucleotideTask


class RunAllTask(luigi.Task):

    def requires(self):
        return [CodonTask(), NucleotideTask()]

    def output(self):
        # TODO update scraped results to database
        return

    def run(self):
        # TODO scrap all results
        return
