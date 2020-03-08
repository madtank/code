#!python3

import os
import subprocess
import time

accounts = open('accounts.txt','r').read().split('\n')


for account in accounts:
    cmd = "cmd /k set AWS_DEFAULT_PROFILE={}".format(account)
    os.system(cmd)
     # subprocess.call("set AWS_DEFAULT_PROFILE=account")
    print(account)
