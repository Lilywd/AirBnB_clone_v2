#!/usr/bin/python3

import os.path
from fabric.api import *
from datetime import datetime
env.user = ["ubuntu"]
env.hosts = ["18.205.192.27"]

run('echo "Hello World"')
