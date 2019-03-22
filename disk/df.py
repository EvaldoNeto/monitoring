import subprocess

"""A class to store the main values found in df -h command.
"""
class Df():
    def __init__(self, file_system, size, p_use, mounted_on):
        self.file_system = file_system
        self.size = size
        self.p_use = p_use
        self.mounted_on = mounted_on

    def update(self, df_obj):
        self.file_system = df_obj.file_system
        self.size = df_obj.size
        self.p_use = df_obj.p_use
        self.mounted_on = df_obj.mounted_on

    def print_df(self):
        print(self.file_system + " " + self.size + " " + self.p_use + " " + self.mounted_on)

    def is_inside_limit(self, limit):
        p_use = float(self.p_use[0 : len(self.p_use) - 1])
        if p_use > limit:
            print("Disk " + self.file_system + " outside limit, usage " + str(self.p_use))
            return False
        return True

"""This function gets data from df -h command, see man df for more info
about it. It skips the first line, as it is contains only the headers
and skips all partitions that contains loop in its name.
"""
def get_data(fs_type=""):
    sp = ""
    if fs_type == "":
        sp = subprocess.check_output(["df", "-h"])
    else:
        try:
            sp = subprocess.check_output(["df", "-h", "-t", fs_type])
        except subprocess.CalledProcessError as e:
            print(e)
            # TO DO
            # HANDLE ERROR
    sp = sp.splitlines()
    disk_info = []
    for aux in sp:
        temp = str(aux, 'utf-8')
        temp = " ".join(temp.split())
        temp = temp.split(" ")
        if temp[0] != "Filesystem":
            disk_info.append(Df(temp[0], temp[1], temp[4], temp[5]))
    return disk_info
        
