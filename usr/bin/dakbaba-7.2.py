#!/usr/bin/env python

import subprocess
subprocess.call(['curl', 'http://www.nytimes.com'], stdout=open('nytimes.html', 'w+'))
