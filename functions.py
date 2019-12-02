import requests
import gzip
import tarfile
import platform
import os
import subprocess
from shutil import copytree
import os.path
from os import path


def check_root():
    if os.getenv('USER') == 'root':
        return True
    return False


def disable_local_fw():
    command1 = 'systemctl stop firewalld'
    command2 = 'systemctl disable firewalld'
    subprocess.call(command1, shell=True)
    subprocess.call(command2, shell=True)


def disable_local_sel():
    command1 = 'setenforce 0'
    command2 = "sed -i 's/^SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config"
    subprocess.call(command1, shell=True)
    subprocess.call(command2, shell=True)