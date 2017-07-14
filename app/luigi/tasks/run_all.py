import luigi
from codon_scraper import CodonScraperTask
from nucleotide_scraper import NucleotideScraperTask


class RunAllTask(luigi.Task):

    def requires(self):
        return [CodonScraperTask(), NucleotideScraperTask()]

    def output(self):
        # TODO update scraped results to database
        pass

    def run(self):
        # TODO scrap all results
        pass
