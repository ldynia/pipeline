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
        if not Network().ping(self.hostname):
            raise Exception("Cann't ping '" + self.hostname + "' host!")

        COMMAND = self.program + " -f /app/data/dna.fsa -o " + self.output().path
        output = RemoteContext(self.hostname).check_output([COMMAND])
        with self.output().open('w') as output_file:
            output_file.write(output)
