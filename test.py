from itertools import cycle
from math import remainder
import os
from pickle import TRUE
import sys
import re
import subprocess
import paramiko
import time
import colorama
import telnetlib
from datetime import datetime
import yaml

from colorama import Fore, Style

def main(config_path, num_of_cycles):
    with open(config_path) as f:
        config = yaml.safe_load(f)
    LOG_PATH = config['local_output_file']
    PDU_IP = config["PDU_IP"]
    PDU_USERNAME = config["PDU_username"]
    PDU_PASSWORD = config["PDU_password"]
    OUTLET_ID = config["outlet_ID"]
    for cur_cycle in range(num_of_cycles):
        pdu_outlet_reboot(PDU_IP, PDU_USERNAME, PDU_PASSWORD,
                                OUTLET_ID, LOG_PATH)
        time.sleep(300)
    

def pdu_outlet_reboot(pdu_IP, username, password, pdu_ID_or_group, log_file):
    cmd = f'../modules/pdu_outlet_reboot.exp {pdu_IP} {username} {password} {pdu_ID_or_group} >> {log_file}'
    #cmd = f'C:\Users\fengy\Downloads\FOS_utils\FOS_utils\modules\pdu_outlet_reboot.exp {pdu_IP} {username} {password} {pdu_ID_or_group} >> {log_file}'
    
    execute_shell_cli(cmd)

def execute_shell_cli(cmd):
    return (subprocess.run(cmd, shell=True, text=True))

if __name__ == '__main__':
    config_path = sys.argv[1]
    num_of_cycles = sys.argv[2]
    main(config_path, int(num_of_cycles))



