import subprocess
import logs.mon_log as mlog

"""A class to store the main values found in df -h command.
"""
class Df():
    def __init__(self, file_system, size, p_use, mounted_on):
        self.file_system = file_system
        self.size = size
        self.p_use = p_use
        self.mounted_on = mounted_on

    def update(self):
        sp = ""
        cmd = "df -h " + self.file_system
        try:
            sp = subprocess.check_output(cmd.split(" "))
        except subprocess.CalledProcessError as e:
            mlog.monLog.exception(e, __name__)
        sp = str(sp, 'utf-8')
        sp = sp.splitlines()
        temp = " ".join(sp[1].split())
        temp = temp.split(" ")
        self.size = temp[1]
        self.p_use = temp[4]
        self.mounted_on = temp[5]
        
    def print_df(self):
        print(self.file_system + " " + self.size + " " + self.p_use + " " + self.mounted_on)

    def is_inside_limit(self, limit):
        p_use = float(self.p_use[0 : len(self.p_use) - 1])
        if p_use > limit:
            mlog.monLog.warning("Disk " + self.file_system + " outside limit, usage " + str(self.p_use), __name__)
            return False
        return True

"""This function gets data from df -h command, see man df for more info
about it. It skips the first line, as it is contains only the headers
and skips all partitions that contains loop in its name.
"""
def get_data(fs_type=""):
    sp = ""
    if fs_type == "":
        try:
            sp = subprocess.check_output(["df", "-h"])
        except subprocess.CalledProcessError as e:
            mlog.monLog.exception(e, __name__)
    else:
        try:
            sp = subprocess.check_output(["df", "-h", "-t", fs_type])
        except subprocess.CalledProcessError as e:
            mlog.monLog.exception(e, __name__)
    sp = sp.splitlines()
    disk_info = []
    for aux in sp:
        temp = str(aux, 'utf-8')
        temp = " ".join(temp.split())
        temp = temp.split(" ")
        if temp[0] != "Filesystem":
            disk_info.append(Df(temp[0], temp[1], temp[4], temp[5]))
    return disk_info
