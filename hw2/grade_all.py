#!/usr/bin/env python
import sys, os, os.path, subprocess
from StringIO import StringIO
for f in sorted(os.listdir('.')):
    if f.endswith('.pred') and os.path.isfile(f):
        # Can be done with awk or Python alone, but this is fastest.
        args = './grade'
        with open(f) as fin, open('/dev/null', 'w') as ferr:
            print '%s: ' % f,
            sys.stdout.flush()
            subprocess.call(args.split(), stdin=fin, stderr=ferr)

