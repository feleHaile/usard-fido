from fido.files import subprocess_cmd
import logging

logger = logging.getLogger()

def wgetfile(fname, dest_file):
        # wget_cmd = "wget --tries=10 --wait=2 --waitretry=2 -O " + dest_file + " " + fname 
        wget_cmd = "wget --tries=10 --retry-connrefused --waitretry=1 --read-timeout=10 --timeout=10 -O " + dest_file + " " + fname 
        print("<",wget_cmd,">")
        status = subprocess_cmd(wget_cmd)

def wgetfile_simple(fname, dest_file):
    print ("hello from wgetfile (cmd) getting file " + fname)
    cmd = "wget -O " + dest_file + " " + fname
    print (cmd)
    subprocess_cmd(cmd)


def download_file(url, file, fileSize=0):
    # local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    local_filename = file


    if (os.path.isfile(local_filename)):
        logger.info("file exists %s" % local_filename)
        return local_filename


    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush(/) commented by recommendation from J.F.Sebastian

    if (fileSize > 0):
        statinfo = os.stat(local_filename)
        actualSize = statinfo.st_size;
        _logd.info("actual=%s; filesize=%s" % (actualSize, fileSize))
        if (actualSize != fileSize):
            _logee.error("ERROR BIGTIME file size not what we expected !")
        return local_filename
    else:
        return local_filename


