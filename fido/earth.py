""" dogapi - provides a simple abstraction to talk to
    USGS EarthExporer and list scenes available
"""

import sys
import logging
import pprint
import json
import time
import requests


# pylint: disable=C0103

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


log_error = LOGGER
log_debug = LOGGER
log_info = LOGGER
log_local = LOGGER


# Debug = True
Debug = False

def dprint(obj):
    """ used to debug the code and print structures """
    if Debug:
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(obj)


#pylint: disable=W0212
class EarthExplorer():
    """ This is the EarthExplorer class that implements the request response code """

    def __init__(self, version='1.4.1'):
        self.baseurl = 'https://earthexplorer.usgs.gov/inventory/json/v/%s/' % version

    def _api(self, endpoint='login', body=None):
        err_code = 'blank'
        body = {'jsonRequest': json.dumps(body)} if body else {}
        for retry in range(10):
            r = requests.post(self.baseurl+endpoint, data=body)
            r.raise_for_status()
            dat = r.json()
            # print(type(dat))
            if dat.get('error'):
                if 'SCENES_EMPTY' in dat.get('errorCode'):
                    return dat
                err_code = ': '.join([dat.get('errorCode'), dat.get('error')])
                print("<%s>" % dat.get('errorCode'))
                log_error.error(err_code)
                log_msg = "Retry %s %s" % (retry, endpoint)
                log_error.error(log_msg)
                time.sleep(2)
            else:
                break
        return dat

    @classmethod
    def login(cls, username, password=None):
        """ login - user and passwd come from dog_config ~/.dog/dog_config.json """
        if password is None:
            sys.exit("No password was specified check the config file.")
        payload = {'username': username, 'password': password}
        return cls()._api('login', payload).get('data')

    @classmethod
    def search(cls, **kwargs):
        """ search """
        return cls()._api('search', kwargs).get('data')

    @classmethod
    def datasets(cls, **kwargs):
        """ datasets  """
        return cls()._api('datasets', kwargs).get('data')

    @classmethod
    def datasetfields(cls, **kwargs):
        """ dataset fields  """
        return cls()._api('datasetfields', kwargs).get('data')

    @classmethod
    def downloadoptions(cls, **kwargs):
        """ downloadoptions   """
        return cls()._api('downloadoptions', kwargs).get('data')

    @classmethod
    def download(cls, **kwargs):
        """ EE download """
        return cls()._api('download', kwargs).get('data')

    @classmethod
    def getorderproducts(cls, **kwargs):
        """ EE download """
        return cls()._api('getorderproducts', kwargs).get('data')

    def grid2ll(self, path, row):
        """ returns lat long from a path row - very handy"""

        ee_request = '{"gridType": "WRS2", "responseShape": "point", "path": "%s", "row": "%s"}' % (
            path, row)
        dprint(ee_request)

        body = 'jsonRequest=%s' % ee_request
        url = self.baseurl+'grid2ll?'+body
        dprint(url)
        r_obj = requests.post(url)
        r_obj.raise_for_status()
        dat = r_obj.json()
        if dat.get('error'):
            sys.stderr.write(
                ': '.join([dat.get('errorCode'), dat.get('error')]))
            log_error.error(': '.join([dat.get('errorCode'), dat.get('error')]))
        return dat


