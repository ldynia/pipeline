import time
import luigi
from utility.network import Network
from luigi.contrib.ssh import RemoteContext


class CodonTask(luigi.Task):

    hostname = "codon"
    program = "cdncounter"
    timestamp = str(int(time.time()))

    def run(self):
        if not Network().ping(self.hostname):
            raise Exception("Cann't ping '" + self.hostname + "' host!")

        COMMAND = self.program + " -f /app/data/dna.fsa -o /pipeline/results/" + self.program + "_" + self.timestamp
        RemoteContext(self.hostname).check_output([COMMAND])
