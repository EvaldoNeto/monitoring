""" This file contains some values that will be used to monitor
the enviroment.
"""

# file system type to be monitored
fs_type = "ext4"

# the upper limit for disk space usage in %
disk_limit = 51

# the path where the files to be removed are in
log_path = "/var/log"
log_folder = "monitoring"
log_file = "mon.log"
log_fullpath = log_path + "/" + log_folder + "/" + log_file

# file to keep
keep_file = "catalina.out"

# emails to be sent about server status
email_receivers = [
    "evaldo@becon.com.br",
    "lucas@becon.com.br",
    "evaldoneto8@gmail.com"
]

# email provider configurations
smtp_provider = "smtp-mail.outlook.com"
email_sender = "becon.monitor@outlook.com"
pswd = "********"