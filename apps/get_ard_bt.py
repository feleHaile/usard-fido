from fido.ardtile import Tile
from fido.ardtile import ParseFileName
import logging
from fido.files import mkdirs
import time
import sys


def process_ard(sensor):
    t = Tile()
    t.get_md5_list()

    cnt = 0
    max = 3
    for line in t.readlines('./h03v03.md5_list'):
        cksum,file = line.split()
        if (sensor in file) and ('BT'in file):
            # print(line, end="")
            cnt = cnt + 1
            if (cnt < max):
                start = time.time()
                logging.info("Processing file : %s" % file)
                t.get_file(file)
                t.untar_file(file)
                bt_list = t.get_file_list(file, 'BTB')
                for bt in bt_list:
                    print("###"*30)
                    print(bt)
                    t.send_file_s3(bt)
                end = time.time()
                t.rm_tmpdir(file)
                elapsed = int(end - start)
                logging.info("xfer_time:%d file:%s" % (elapsed, file))




# sensor = 'LC08'
# sensor = 'LE07'
sensor = 'LT05'
sensor = sys.argv[1]
logfile = "/data/logs/test-ard.log_" + sensor
created_file = mkdirs(logfile)
if created_file is None:
    print("trouble creating logs directory!")
else:
    print(created_file)

# my_level = logging.DEBUG
my_level = logging.INFO

logging.basicConfig(filename=logfile, level=my_level,
                    format='%(levelname)s,%(asctime)s,%(message)s,')
process_ard(sensor)

