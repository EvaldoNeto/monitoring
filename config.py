""" This file contains some values that will be used to monitor
the enviroment.
"""

# file system type to be monitored
fs_type = "ext4"

# the upper limit for disk space usage in %
disk_limit = 30

# the path where the files to be removed are in
log_path = "/var/log/tomcat7"

# file to keep
keep_file = "catalina.out"

# emails to be sent about server status
emails = [
    "evaldo@becon.com.br",
    "lucas@becon.com.br",
    "evaldoneto8@gmail.com"
]
