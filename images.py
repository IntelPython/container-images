# Copyright (c) 2017, Intel Corporation
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
#     * Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of Intel Corporation nor the names of its contributors
#       may be used to endorse or promote products derived from this software
#       without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from __future__ import print_function

import argparse
import getpass
import jinja2
import os
import re
import subprocess
import sys


def get_proxies():
    '''Pass through proxies to docker container'''
    proxies = ''
    for var in ['http_proxy','https_proxy','no_proxy']:
        if var in os.environ:
            proxies += ' --build-arg %s=%s' % (var,os.environ[var])
    return proxies

class Templates():
    '''singleton to render the templates'''
    def __init__(self):
        loader = jinja2.FileSystemLoader(searchpath = 'tpls')
        env = jinja2.Environment(loader=loader)
        self._readme = env.get_template('tpl.README.md')
        self._dockerfile = env.get_template('tpl.Dockerfile')
        self._post_push = env.get_template('tpl.post_push')

    def render(self, conf):
        name = conf.name()
        with open('configs/%s/README.md' % name,'wb') as fh:
            fh.write(self._readme.render(conf).encode('utf-8'))
        with open('configs/%s/Dockerfile' % name,'wb') as fh:
            fh.write(self._dockerfile.render(conf).encode('utf-8'))
        with open('configs/%s/hooks/post_push' % name,'wb') as fh:
            fh.write(self._post_push.render(conf).encode('utf-8'))

# singleton
templates = Templates()

def parse_name(name):
    pattern = re.compile(r'intelpython(?P<pyver>[23])_(?P<package>.*)')
    match = pattern.match(name)
    return (int(match.group('pyver')),match.group('package'))

class Conf(dict):
    '''Docker image configuration'''
    def __init__(self,pyver=None,package=None,name=None):
        if name:
            (pyver,package) = parse_name(name)
        self['pyver'] = pyver
        self['package'] = package
        # github tag & docker tag is update_number-build_number, e.g. 2017.0.1-1
        # conda package spec is update_number=build_number, e.g. intelpython2_core=2017.0.1=1
        self['update_number'] = '2017.0.3'
        self['build_number'] = '3'

    def name(self):
        return 'intelpython%d_%s' % (self['pyver'],self['package'])

    def tag(self):
        return '%s/%s' % (getpass.getuser(),self.name())

    def gen(self):
        templates.render(self)

    def build(self):
        cmd = 'docker build %s -t %s --file configs/%s/Dockerfile configs/%s' % (get_proxies(),self.tag(),self.name(),self.name())
        print('    ',cmd)
        subprocess.check_call(cmd, shell=True)

    def test(self):
        cmd = 'docker run -t %s python -c 1' % self.tag()
        print('    ',cmd)
        subprocess.check_call(cmd, shell=True)

# Add new configurations here
all_confs = [Conf(2,'core'),
             Conf(2,'full'),
             Conf(3,'core'),
             Conf(3,'full')
]

def main():
    conf_names = [conf.name() for conf in all_confs]
    parser = argparse.ArgumentParser(description='generate the configurations for docker images')
    parser.add_argument('--gen',
                        action='store_true',
                        help='Generate Dockerfile and README.md')
    parser.add_argument('--build',
                        action='store_true',
                        help='Build docker image')
    parser.add_argument('--test',
                        action='store_true',
                        help='Test docker image')
    parser.add_argument('conf',
                        choices=['all'] + conf_names,
                        nargs='*', 
                        help='list of confs to generate')
    args = parser.parse_args()
    if args.conf[0] == 'all':
        args.conf = conf_names

    for n in args.conf:
        print('Processing:',n)
        c = Conf(name=n)
        if args.gen:
            print('  gen')
            c.gen()
        if args.build | args.test:
            print('  build')
            c.build()
        if args.test:
            print('  test')
            c.test()
            

main()
