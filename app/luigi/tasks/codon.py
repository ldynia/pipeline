import time
import luigi
from utility.network import Network
from luigi.contrib.ssh import RemoteContext


class CodonTask(luigi.Task):

    foutput = "cdncount.json.out"
    program = "cdncount"
    hostname = "codon"
    timestamp = str(int(time.time()))

    def output(self):
        return luigi.LocalTarget("/pipeline/results/%s" % self.foutput)

    def run(self):
        if not Network().ping(self.hostname):
            raise Exception("Cann't ping '" + self.hostname + "' host!")

        COMMAND = self.program + " -f /pipeline/data/dna.fsa"
        output = RemoteContext(self.hostname).check_output([COMMAND])

        filename = "/pipeline/results/%s" % self.foutput
        with open(filename, "w") as data_file:
            data_file.write(str(output)[2:-3])
