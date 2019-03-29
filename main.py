import disk.df as df
import disk.find as find
import disk.rm as rm
import time
import subprocess
import config
import monitor
import domain.hostname as host

def main():
    monitor.create_log_dir()
    monitor.disk_space(config.fs_type)

if __name__=="__main__":
    main()
