import subprocess
import logs.mon_log as mlog

"""This file contain functions to show or set the system's host name, for more 
information see man hostname
"""

def get_name():
    sp = ""
    try:
        sp = subprocess.check_output(["hostname"])
    except subprocess.CalledProcessError as e:
        mlog.monLog.exception(e, __name__)
    sp = str(sp, 'utf-8')
    return sp
    
