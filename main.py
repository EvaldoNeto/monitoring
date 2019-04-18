import disk.df as df
import disk.find as find
import disk.rm as rm
import time
import subprocess
import config
import monitor
import domain.hostname as host
import subprocess
import sys

def main(service=""):
    monitor.create_log_dir()
    monitor.disk_space(config.fs_type, service)

args = ["tomcat", "unifi"]
    
if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Wrong number of arguments for ", sys.argv[0], " - use one arg")
        sys.exit(0)
    if sys.argv[1] not in args:
        print("Argument not valid. Valid arguments:")
        for arg in args:
            print("-", arg)
        sys.exit(0)
    main(sys.argv[1])
