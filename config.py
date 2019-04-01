""" This file contains some values that will be used to monitor
the enviroment.
"""

# file system type to be monitored
fs_type = "ext4"

# the upper limit for disk space usage in %
disk_limit = 40

# the time between two consecutive scans
wait_time = 30

# the path where the logs from the application are going to be
log_path = "/var/log"
log_folder = "monitoring"
log_file = "mon.log"
log_fullpath = log_path + "/" + log_folder + "/" + log_file
# the max log file size in MB, when it reaches this value it will be deleted. i know, bad practice, still got to improve it
max_log_size = 0

# file to keep
keep_file = "catalina.out"
tomcat_log_path = "/var/log/tomcat7"

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
