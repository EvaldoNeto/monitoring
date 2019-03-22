import disk.df as df
import disk.find as find
import disk.rm as rm
import time
import subprocess
import config
import monitor

def main():
    monitor.disk_space(config.fs_type)

if __name__=="__main__":
    main()
