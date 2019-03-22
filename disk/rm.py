import subprocess

class Rm():
    def __init__(self):

    def all_but(file_name):
        sp = subprocess.check_output(["rm", "--", "!(" + str(file_name) + ")"])
        print(sp)
