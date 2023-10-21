import telnetlib
import time
import subprocess
import os

resCount = 0
pingCount = 0


def restart():
    hostserver = ""
    newline = "\n"
    username = "" + newline
    password = "" + newline
    telnet = telnetlib.Telnet(hostserver)
    telnet.read_until("login: ")
    telnet.write(username)
    telnet.read_until("Password: ")
    telnet.write(password)
    time.sleep(1)
    telnet.write("reboot" + "\n")
    time.sleep(1)
    telnet.close()
    global resCount
    resCount += 1
    print('restart...')


def restartTransmission():
    os.system("taskkill /im Transmission-qt.exe")
    time.sleep(1)
    subprocess.Popen("\"C:\\Program Files\\Transmission\\transmission-qt.exe\"")


def ping():
    global pingCount
    pingCount += 1
    website = "google.com"
    try:
        ping = subprocess.Popen(["ping", website], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, error = ping.communicate()
        if out:
            print(out, "\n\nPing OutPut")
            if "Reply from " in str(out) and not "unreachable" in str(out):
                return True
            else:
                return False
    except subprocess.CalledProcessError:
        print("Couldn't ping")
    return False


# while True:
os.system("cls")
print("ping #%d , res #%d" % (pingCount, resCount))

try:
    if not ping():
        print('ping not success')
        restart()
        time.sleep(99)
        restartTransmission()
    else:
        print('ping ok')
        restart()
        time.sleep(10)
except Exception as e:
    time.sleep(2)
    print("Unable to restart", e)
time.sleep(2)
