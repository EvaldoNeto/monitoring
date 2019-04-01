import subprocess
import logs.mon_log as mlog

"""This file contain functions to remove files based om the rm function from unix
like systems. For more information see the manual, man rm
"""

"""Remove all files from the path but the one specified
"""
def all_but(path, file_name):
    cmd = "find " + path + " ! -name " + file_name + " -type f -exec rm -f {} +"
    try:
        sp = subprocess.check_output(cmd.split(" "))
    except subprocess.CalledProcessError as e:
        mlog.monLog.exception(e, __name__)

"""Remove the file with the given name in the given path
"""
def single_file(path, file_name):
    cmd = "rm " + path + "/" + file_name
    try:
        sp = subprocess.check_output(cmd.split(" "))
    except subprocess.CalledProcessError as e:
        mlog.monLog.exception(e, __name__)
    
