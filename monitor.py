import config
import disk.df as df
import time
import disk.rm as rm

"""This function monitor the disk space and when above the disk limit
it deletes old log files
"""
def disk_space(fs_type):
    while True:
        disk_data = df.get_data(fs_type)
        for data in disk_data:
            if data.is_inside_limit(config.disk_limit):
                print("Disk " + data.file_system + " inside limit, usage " + str(data.p_use))
            else:
                rm.all_but(config.log_path, config.keep_file)
        time.sleep(3)
            
