#!/usr/bin/env python

import pycarwings2
from configparser import ConfigParser
import logging
import sys
import time

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

parser = ConfigParser()
candidates = ['config.ini', 'my_config.ini']
found = parser.read(candidates)

username = parser.get('get-leaf-info', 'username')
password = parser.get('get-leaf-info', 'password')
region = parser.get('get-leaf-info', 'region')


# Main program

logging.debug("login = %s, password = %s, region = %s" % (username, password, region))

print("**************************** Prepare Session ***********************************")
s = pycarwings2.Session(username, password, region)
print("*************************** Login... *******************************************")
leaf = s.get_leaf()


print("*************************** Try getting the temp ****************************")
res = leaf.request_cabin_temp()


while(True):
    print("*************************** Sleep ****************************")
    time.sleep(10)
    response = leaf.request_cabin_temp_result(res)
    if response is not None:
        break

print("*********************** get_latest_hvac_status from servers ********************")
leaf_info = leaf.get_latest_hvac_status()
if leaf_info.is_hvac_running:
    print("************************* Climate control is on *******************************")
else:
    print("************************* Climate control is off ******************************")
