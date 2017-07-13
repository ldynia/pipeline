import os


class Network:

    def ping(self, hostname):
        result = os.system("ping -c1 " + hostname + " > /dev/null 2>&1")
        return result == 0
