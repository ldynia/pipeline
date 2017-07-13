import time
import luigi
from utility.network import Network
from luigi.contrib.ssh import RemoteContext


class CodonScraperTask(luigi.Task):

    hostname = "codon"
    program = "cdncounter"
    timestamp = str(int(time.time()))

    def output(self):
        return luigi.LocalTarget("/pipeline/results/%s.json" % self.timestamp)

    def run(self):
        if Network().ping(self.hostname):
            output = RemoteContext(self.hostname).check_output([self.program + " /app/data/dna.fsa"])
            with self.output().open('w') as output_file:
                output_file.write(output)
