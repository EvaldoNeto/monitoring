import subprocess
import logs.mon_log as mlog

class Find():
    def __init__(self, size, path):
        self.size = size
        self.path = path

"""Find all files from the path but the one specified, for more information
see man find. 
The return value is a list with the file names that were found
"""
def all_but(path, file_name, max_depth=""):
    cmd = ""
    if max_depth != "":
        cmd = "find " + path + " -maxdepth " + str(max_depth) + " -type f ! -name " + file_name
    else:
        cmd = "find " + path + " -type f -name " + file_name
    try:
        sp = str(subprocess.check_output(cmd.split(" ")), 'UTF-8')
        sp = sp.splitlines()
        return sp
    except subprocess.CalledProcessError as e:
        mlog.monLog.exception(msg, __name__)
