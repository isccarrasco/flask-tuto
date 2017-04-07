#!/usr/bin/python
import os
import subprocess
import sys

subprocess.call(['virtualenv', 'myenv'])
if sys.platform == 'win32':
  bin = 'Scripts'
else:
  bin = 'bin'

subprocess.call([os.path.join('myenv', bin, 'pip'), 'install', 'pip'])
subprocess.call([os.path.join('myenv', bin, 'pip'), 'install', 'psycopg2'])
subprocess.call([os.path.join('myenv', bin, 'pip'), 'install', 'Flask'])
subprocess.call([os.path.join('myenv', bin, 'pip'), 'install', 'Flask-SQLAlchemy'])
subprocess.call([os.path.join('myenv', bin, 'pip'), 'install', 'Flask-RESTful'])
