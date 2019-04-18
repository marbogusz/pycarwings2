#!/usr/bin/env python

import pycarwings2
import time
import datetime
from configparser import ConfigParser
import logging
import sys
import pprint

logging.basicConfig(stream=sys.stdout, level=logging.ERROR)

parser = ConfigParser()
candidates = ['config.ini', 'my_config.ini']
found = parser.read(candidates)

username = parser.get('get-leaf-info', 'username')
password = parser.get('get-leaf-info', 'password')
region = parser.get('get-leaf-info', 'region')
sleepsecs = 30     # Time to wait before polling Nissan servers for update


def print_info(info):
    print("  Operation date %s" % info.answer["BatteryStatusRecords"]["OperationDateAndTime"])
    print("  Remaining Wh %s" % info.battery_remaining_wh)
    print("  Time to full 3kW %s" % info.time_to_full_l2)
    print("  SOC %s" % info.state_of_charge)
    print("  Range AC  on %s" % info.cruising_range_ac_on_km)
    print("  Range AC off %s" % info.cruising_range_ac_off_km)


# Main program


s = pycarwings2.Session(username, password, region)
leaf = s.get_leaf()

while(True):
    print(datetime.datetime.now())
    leaf_info = leaf.get_latest_battery_status()
    print_info(leaf_info)
    time.sleep(600)
    

