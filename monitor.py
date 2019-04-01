import config
import disk.df as df
import time
import disk.rm as rm
import messages.mailing as mail
import disk.find as find
import logs.mon_log as mlog
import domain.hostname as host
import disk.mon_dir as mdir
import os

"""This function monitor the disk space and when above the disk limit
it deletes old log files
"""
def disk_space(fs_type):
    monitor_log_file()
    while True:
        disk_data = df.get_data(fs_type)
        for data in disk_data:
            if data.is_inside_limit(config.disk_limit):
                mlog.monLog.warning("host: " + host.get_name() + "\nDisk " + data.file_system + " inside limit, usage " + str(data.p_use), __name__)
            else:
                mlog.monLog.warning("Cleaning disk", __name__)
                msg = "host: " + host.get_name() + "\n" + data.file_system + " used disk before remove: " + data.p_use +"\nfiles removed:\n"
                files = find.all_but(config.tomcat_log_path, config.keep_file)
                for f in files:
                    msg += "-" + f + "\n"
                rm.all_but(config.tomcat_log_path, config.keep_file)
                data.update()
                msg += "\n" + data.file_system + " used disk after remove: " + data.p_use
                mlog.monLog.warning(msg, __name__)
                sendEmail(msg)
        time.sleep(config.wait_time)

def sendEmail(msg):
    provider = mail.MailProvider(config.smtp_provider, config.email_sender, config.pswd)
    email = mail.Mail(provider, config.email_receivers, [], "SPAM", msg)
    email.send()

def create_log_dir():
    if not mdir.exists(config.log_path, config.log_folder):
        mdir.create(config.log_path, config.log_folder)
        mlog.monLog.warning("log directory created", __name__)
        
def monitor_log_file():
    if find.m_file(config.log_path + "/" + config.log_folder, config.log_file, 1) != []:
        file_size = os.path.getsize(config.log_fullpath) / 1000000
        if file_size > config.max_log_size:
            msg = "Removing monitor log file"
            mlog.monLog.warning(msg, __name__)
            rm.single_file(config.log_path + "/" + config.log_folder, config.log_file)
