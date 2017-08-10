import time
import luigi


class RandomTask(luigi.Task):

    foutput = "random.json.out"
    timestamp = str(int(time.time()))

    def output(self):
        return luigi.LocalTarget("/pipeline/results/%s" % self.foutput)

    def run(self):
        filename = "/pipeline/results/%s" % self.foutput
        with open(filename, "w") as data_file:
            data = '{"random":' + str(self.timestamp) + '}'
            data_file.write(data)
