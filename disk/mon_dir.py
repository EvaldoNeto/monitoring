import subprocess
import logs.mon_log as mlog

"""Functions to deal with directories
"""

"""Creates a new directory
"""
def create(path, dir_name):
    cmd = "mkdir " + path + "/" + dir_name
    try:
        sp = subprocess.check_output(cmd.split(" "))
    except subprocess.CalledProcessError as e:
        mlog.monLog.exception(e, __name__)

"""Checks if the directory exists
"""
def exists(path, dir_name):
    cmd = "find " + path + " -type d -name " + dir_name
    try:
        sp = str(subprocess.check_output(cmd.split(" ")), 'utf-8')
        if sp != "":
            return True
        return False
    except subprocessCalledProcessError as e:
        mlog.monLog.exception(e, __name__)
        return None
