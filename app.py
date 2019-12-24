from datetime import datetime as dt
import time
host_file = "C:\\Windows\\System32\\drivers\\etc\\hosts"
#C:\Windows\System32\drivers\etc\hosts
website_list = ["www.facebook.com","www.youtube.com","www.xyz.com"]
redirect = r"127.0.0.1"
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 12) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,
                                                                           13):
        print(".....Working Time......")
        with open(host_file, "r+") as file:
            contents = file.read()
            for website in website_list:
                if website in contents:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")

    else:
        with open(host_file, "r+") as file:
            contents = file.readlines()
            file.seek(0)
            for line in contents:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print(".....Fun Time.....")
    time.sleep(10)






