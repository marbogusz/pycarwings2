#!/usr/bin/env python

import pycarwings2
from configparser import ConfigParser
import logging
import sys
import time
import datetime

logging.basicConfig(stream=sys.stdout, level=logging.ERROR)

parser = ConfigParser()
candidates = ['config.ini', 'my_config.ini']
found = parser.read(candidates)

username = parser.get('get-leaf-info', 'username')
password = parser.get('get-leaf-info', 'password')
region = parser.get('get-leaf-info', 'region')


# Main program


s = pycarwings2.Session(username, password, region)
leaf = s.get_leaf()

while(True):
    print(datetime.datetime.now())
    res = leaf.request_cabin_temp()
    while(True):
        time.sleep(45)
        response = leaf.request_cabin_temp_result(res)
        if response is not None:
            break
    print(response)
    time.sleep(360)


