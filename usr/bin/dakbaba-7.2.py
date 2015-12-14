#!/usr/bin/env python

import subprocess
doc=subprocess.call(['curl', 'http://www.nytimes.com', '>', 'nytimes.html'])
