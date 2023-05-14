import os
import sys
import time

#functions
def WriteText(z):
    for e in z +'\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
time.sleep(0.1)
banner = '''\033[4;32m
░██████╗██╗░░██╗░█████╗░████████╗
██╔════╝██║░░██║██╔══██╗╚══██╔══╝
╚█████╗░███████║██║░░██║░░░██║░░░
░╚═══██╗██╔══██║██║░░██║░░░██║░░░
██████╔╝██║░░██║╚█████╔╝░░░██║░░░
╚═════╝░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░by Anonymous & Francisco'''
WriteText(banner)
os.system("pkg install ruby")
os.system("gem install lolcat")
time.sleep(2)
os.system("echo Updating system.....! | lolcat")
os.system("pkg update -y")
time.sleep(2)
os.system("echo Upgrading system....! | lolcat")
os.system("pkg upgrade -y")
os.system("echo Installing required dependencies....! | lolcat")
os.system("pkg install -y root-repo")
os.system("pkg install -y git tsu python wpa-supplicant pixiewps iw")
os.system("git clone --depth https://github.com/ancientmodder/shot deadxskull")
os.system("chmod +x shot/deadxskull.py")
time.sleep(0.1)
os.system("echo ########################################################|lolcat")
time.sleep(3)
os.system("                                                                    ")
time.sleep(3)
os.system("echo Usage  :            Turn of your wifi                   |lolcat")
time.sleep(3)
os.system("echo execute: sudo python deadxskull/deadxskull.py --mtk-wifi|lolcat")
time.sleep(3)
os.system("                                                                    ")
time.sleep(3)
os.system("echo ########################################################|lolcat")
time.sleep(3)
os.system("rm -rf setup.py")




























