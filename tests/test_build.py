import getpass
import os
import subprocess

def get_proxies():
    proxies = ''
    for var in ['http_proxy','https_proxy','no_proxy']:
        if var in os.environ:
            proxies += ' --build-arg %s=%s' % (var,os.environ[var])
    return proxies

def do_build(dir):
    tag = '%s/%s' % (getpass.getuser(),dir)
    subprocess.check_call('docker build %s -t %s --file %s/Dockerfile .' % (get_proxies(),tag,dir),shell=True)
    subprocess.check_call('docker run -t %s python -c 1' % tag ,shell=True)

def test_builds():
    for dir in ['idp2_core','idp3_core','idp2_full','idp3_full']:
        do_build(dir)
