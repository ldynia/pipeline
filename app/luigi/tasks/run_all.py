import luigi
from codon_scraper import CodonTask
from nucleotide_scraper import NucleotideTask


class RunAllTask(luigi.Task):

    def requires(self):
        return [CodonTask(), NucleotideTask()]

    def output(self):
        # TODO update scraped results to database
        pass

    def run(self):
        # TODO scrap all results
        pass
