""" ardtile is a module for wget of tiles """

import os
from os import listdir
from os.path import isfile, join

from fido.files import subprocess_cmd
from fido.wget import wgetfile

class Tile():

    extensions = { 'SR': '_SR.tar' }
    urld = 'https://edclpdsftp.cr.usgs.gov/downloads/collections/l2-ard-tiles/h03v03/'
    stagedir = "/data/h03v03"
    

    def __init__(self):
        pass


    def __repr__(self):
        pass


    # get the md5 hash list
    def get_md5_list(self):

         md5list = 'h03v03.md5_list'
         myfile = './' + md5list

         if os.path.exists(myfile):
	         print ("yay the md5 file is here...\n")
         else:
	         print ("Bummer!")
	         print ("go get it")
	         cmd = 'wget ' + self.urld + md5list
	         result = subprocess_cmd(cmd)
	         print(result)


    def get_file(self, file):
        tmpdir = self.make_tmpdir(file)
        dest_file = tmpdir + '/' + file
        file = self.urld + file
        print(file)
        wgetfile(file,dest_file)
        #wgetfile(file,dest_file)


    def readlines(self, path):
        """Read lines from a text file.

        Args:
            path (str): Full path to file
        Returns:
            list: File text
        """

        with open(path, 'r') as handle:
             return handle.readlines()


    def make_path(self,file):
        p = ParseFileName(file)
        pathlist = [p.sensor, p.acquision_date]
        path = '/'.join(pathlist)
        return(path)


    def untar_file(self,file):
        tmpdir = self.tmpdir_name(file)
        os.chdir(tmpdir)
        untarFile(file)


    def tmpdir_name(self, filename):
        root = '/data/'
        tmppath = self.make_path(filename)
        tmpdir = root + tmppath
        return(tmpdir)


    def make_tmpdir(self, filename):
        tmpdir = self.tmpdir_name(filename)
        print("dir=",tmpdir)
        pushcmd = "mkdir -p " + tmpdir
        subprocess_cmd(pushcmd)
        tmpdir = self.tmpdir_name(filename)
        return(tmpdir)


    def rm_tmpdir(self, filename):
        os.chdir("/opt/usard-fido")
        tmpdir = self.tmpdir_name(filename)
        pushcmd = "rm -fr " + tmpdir
        subprocess_cmd(pushcmd)


    def get_file_list(self, filename, criteria):
        mypath = '.'
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        found_files = []
        for file in onlyfiles:
            if criteria in file:
                found_files.append(file)
        return(found_files)


    def send_file_s3(self, filename):
        bucket = 's3://ga-odc-eros-ard-west/'
        path = 'usard/' + self.make_path(filename)
        dest_file = bucket + path + '/' + filename
        s3cp(filename, dest_file)


class ParseFileName():
    def __init__(self, filename):
        self.filename = filename
        self.scene = filename[:-7]
        ## LC08_CU_003003_20130414_20170713_C01_V01_BT.tar
        self.sensor, self.region, self.hv, self.acquision_date, self.processing_date,\
        self.collection, self.version, self.long_extension = filename.split("_")




def untarFile(fname):
    print("hello from untarFile decompressing file " + fname)
    infile = fname
    pushcmd = "tar -xvf %s" % infile
    print(pushcmd)
    subprocess_cmd(pushcmd)
    # time.sleep(2)
    # os.unlink(infile)


def s3cp(fromfile, tofile):
    print("hello from s3cp copying file " + fromfile)
    infile = fromfile
    outfile = tofile
    pushcmd = "aws s3 cp %s %s" % (infile, outfile)
    print(pushcmd)
    subprocess_cmd(pushcmd)

