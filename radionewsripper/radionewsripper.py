import requests
import random
import os


class RadioNewsRipper:
    def __init__(self, url, length_sec):

        self.url = url
        self.length_sec = int(length_sec)
        self.tmp_folder = "rec_" + str(random.randint(1, 10000))
        return

    def record(self):
        if not self.__checkurl():
            print("Error: URL '" + self.url + "' not reachable")
            return

        exec_str = "streamripper " + \
                   self.url + " -l " + str(self.length_sec) + " -A -a -s -d " + self.tmp_folder
        print("Executing ripper...")
        print(exec_str)
        os.system(exec_str)
        print("Ready recording")
        return

    def __checkurl(self):
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) " +
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"
        }
        try:
            requests.request("get", self.url, headers=headers)
        except requests.RequestException as e:
            return False
        return True
