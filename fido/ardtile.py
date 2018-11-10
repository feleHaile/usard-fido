""" ardtile is a module for wget of tiles """

import os
import subprocess

class Tile():

    extensions = { 'SR': '_SR.tar' }
    urld = 'https://edclpdsftp.cr.usgs.gov/downloads/collections/l2-ard-tiles/h03v03/'
    stagedir = "./h03v03"
    

    def __init__(self):
        pass


    def __repr__(self):
        pass


    # get the md5 hash list
    def get_md5_list(self):

         md5list = 'h03v03.md5_list'
         myfile = './' + md5list

         if os.path.exists(myfile):
	         print ("yay ths md5 file is here...\n")
         else:
	         print ("Bummer!")
	         print ("go get it")
	         cmd = 'wget ' + self.urld + md5list
	         result = subprocess_cmd(cmd)
	         print(result)


    def get_file(self, file):
        print(file)
        self.wgetfile(file)


    def readlines(self, path):
        """Read lines from a text file.
        Args:
            path (str): Full path to file
        Returns:
            list: File text
        """

        with open(path, 'r') as handle:
             return handle.readlines()

    def wgetfile(self,fname):
        print ("hello from wgetxml getting file " + fname)
        fullfile = self.stagedir + '/' + fname
        wgetfile = self.urld + fname
        cmd = "wget -O " + fullfile + " " + wgetfile
        print (cmd)
        subprocess_cmd(cmd)



def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    stupidBytesObject = proc_stdout
    outStr = (stupidBytesObject.decode("utf-8"))
    print(outStr)
    return(outStr)

