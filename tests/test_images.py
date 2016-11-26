import getpass
import os
import subprocess

def test_gen():
    subprocess.check_call('python images.py --gen all', shell=True)
def test_build():
    subprocess.check_call('python images.py --build all', shell=True)
def test_test():
    subprocess.check_call('python images.py --test all', shell=True)
