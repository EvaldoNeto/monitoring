import config
import disk.df as df
import time
import disk.rm as rm
import messages.mailing as mail
import disk.find as find

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
                print("Cleaning disk")
                msg = data.file_system + " used disk before remove: " + data.p_use +"\nfiles removed:\n"
                files = find.all_but(config.log_path, config.keep_file, 1)
                for f in files:
                    msg += "-" + f + "\n"
                rm.all_but(config.log_path, config.keep_file)
                data.update()
                msg += "\n" + data.file_system + " used disk after remove: " + data.p_use
                sendEmail(msg)
        time.sleep(30)

def sendEmail(msg):
    provider = mail.MailProvider(config.smtp_provider, config.email_sender, config.pswd)
    email = mail.Mail(provider, config.email_receivers, [], "SPAM", msg)
    email.send()
