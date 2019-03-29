import config
import disk.df as df
import time
import disk.rm as rm
import messages.mailing as mail
import disk.find as find
import logs.mon_log as mlog
import domain.hostname as host
import disk.mon_dir as mdir

"""This function monitor the disk space and when above the disk limit
it deletes old log files
"""
def disk_space(fs_type):
    while True:
        disk_data = df.get_data(fs_type)
        for data in disk_data:
            if data.is_inside_limit(config.disk_limit):
                mlog.monLog.warning("host: " + host.get_name() + "\nDisk " + data.file_system + " inside limit, usage " + str(data.p_use), __name__)
            else:
                mlog.monLog.warning("Cleaning disk", __name__)
                msg = "host: " + host.get_name() + "\n" + data.file_system + " used disk before remove: " + data.p_use +"\nfiles removed:\n"
                files = find.all_but(config.log_path, config.keep_file, 1)
                for f in files:
                    msg += "-" + f + "\n"
                rm.all_but(config.log_path, config.keep_file)
                data.update()
                msg += "\n" + data.file_system + " used disk after remove: " + data.p_use
                mlog.monLog.warning(msg, __name__)
                sendEmail(msg)
        time.sleep(30)

def sendEmail(msg):
    provider = mail.MailProvider(config.smtp_provider, config.email_sender, config.pswd)
    email = mail.Mail(provider, config.email_receivers, [], "SPAM", msg)
    email.send()

def create_log_dir():
    if not mdir.exists(config.log_path, config.log_folder):
        mdir.create(config.log_path, config.log_folder)
        mlog.monLog.warning("log directory created", __name__)
