import subprocess

class Find():
    def __init__(self, size, path):
        self.size = size
        self.path = path

"""Still gotta fix this function, it looks like the pipe is messing up
with the size displayed. Because of that the final order is wrong
"""
def get_data(path, n_files):
    sp1 = subprocess.Popen(["sudo", "find", path, "-type", "f", "-printf", "'%s %p\n'"], stdout=subprocess.PIPE) 
    sp2 = subprocess.Popen(["sort", "-nr"], stdin=sp1.stdout, stdout=subprocess.PIPE)
    sp3 = subprocess.Popen(["head", "-5"], stdin=sp2.stdout, stdout=subprocess.PIPE)
    sp1.stdout.close()
    sp2.stdout.close()
    output, err = sp3.communicate()
    output = output.splitlines()
    files_info = []
    for info in output:
        temp = str(info, 'utf-8')
        print(temp)
    #    return output
    
