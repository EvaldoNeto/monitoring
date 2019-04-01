# monitoring
For now this project monitors the disk usage and remove old log files to clean up some disk space.

# Configuration

The file config.py contains all the configuration needed. I choose fs_type ext4 because it is the main file system type to be monitored on our servers.

As there is a tomcat running on the machine I want to monitor I choose to keep only the latest logs from it, i.e, catalina.out. All other files on the tomcat log folder are going to be deleted.

The list email_receivers contains all emails that will receive a notification when the disk_limit is reached

# Running the Application

Just clone the repo to a folde, cd to it and run "python3 main.py"

## Creating a Linux service

Create a file named monitoring.service under the folder /etc/systemd/system contaning the content bellow:

```
[Unit]
Description=Monitoring host status
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
StartLimitIntervalSec=0
User=root
ExecStart=/usr/bin/python3 /path/to/application/main/file

[Install]
WantedBy=multi-user.target
```

After that just run 

```
systemctl start monitoring.service 
```
to start the service

To enable the service to automaticaly run when the machine start run 

```
systemctl enable monitoring.service
```

For some more basic information on Linux services see:
https://medium.com/@benmorel/creating-a-linux-service-with-systemd-611b5c8b91d6
