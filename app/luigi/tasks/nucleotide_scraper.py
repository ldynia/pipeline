import time
import luigi
from utility.network import Network
from luigi.contrib.ssh import RemoteContext


class NucleotideScraperTask(luigi.Task):

    hostname = "nucleotide"
    program = "ntcounter"
    timestamp = str(int(time.time()))

    def output(self):
        return luigi.LocalTarget("/pipeline/results/{0}_{1}.json".format(self.program, self.timestamp))

    def run(self):
        if Network().ping(self.hostname):
            output = RemoteContext(self.hostname).check_output([self.program + " /app/data/dna.fsa"])
            with self.output().open('w') as output_file:
                output_file.write(output)
