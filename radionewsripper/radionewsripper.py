import requests
import random
import os
import shutil


class RadioNewsRipper:
    def __init__(self, url, length_sec, location, name):

        self.url = url
        self.length_sec = int(length_sec)
        self.tmp_folder = "/tmp/rec_" + str(random.randint(1, 10000))
        self.final_folder = location
        self.file_name = name
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
        print("Getting and moving mp3-file")
        existing_files = os.listdir(self.tmp_folder)
        tmp_mp3_filename = None
        for f in existing_files:
            mp3_pos = f.find(".mp3")
            if mp3_pos != -1:
                tmp_mp3_filename = f
                break

        if not tmp_mp3_filename :
            print("Error: Could not find recorded file")
            return


        os.rename(self.tmp_folder+"/"+tmp_mp3_filename, self.final_folder + "/" + self.file_name + ".mp3")
        shutil.rmtree(self.tmp_folder)
        print("Ready")
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
