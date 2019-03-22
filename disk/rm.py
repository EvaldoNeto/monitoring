import subprocess

"""This file contain functions to remove files based om the rm function from unix
like systems. For more information see the manual, man rm
"""
def all_but(path, file_name):
    cmd = "find " + path + " ! -name " + file_name + " -type f -exec rm -f {} +"
    try:
        sp = subprocess.check_output(cmd.split(" "))
    except subprocess.CalledProcessError as e:
        # TO DO
        # HANDLE ERROR
        print(e)

def single_file(path, file_name):
    cmd = "rm " + path + "/" + file_name
    try:
        sp = subprocess.check_output(cmd.split(" "))
    except subprocess.CalledProcessError as e:
        print(e)
        # TO DO
        # HANDLE ERROR
        #print(e)
    
