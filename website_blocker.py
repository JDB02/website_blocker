import os
import time
from datetime import datetime as dt


if os.name =='nt':
    hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
elif os.name =='posix':
    hosts_path=r"/etc/hosts"
else:
    print("Operating System Unkown: unable to locate hosts file")

redirect="127.0.0.1"
website_list=["www.facebook.com", "facebook.com", "outlook.live.com", "hotmail.com", "twitter.com", "www.instagram.com", "gmail.com"]
final_lists=[redirect + " " + i for i in website_list]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hours...")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(hosts_temp,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Happy Surfing")
    time.sleep(5)
