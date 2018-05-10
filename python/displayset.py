#!/usr/bin/python

#*-* coding: utf-8 *-*

import os

import sys

if len(sys.argv) != 4:

print „Usage: displayset.py <hpixels> <vpixels> <refresh_rate>”

exit()

else:

home = os.environ[‚HOME’]

os.chdir(home)

if os.path.exists(‚.xprofile’):

os.rename(‚.xprofile’, ‚.xprofile.bak’)

print „The ‚.xprofile’ file backuped as ‚%s/.xprofile.bak'” % home

xprofile = open(‚.xprofile’, ‚w’)

modeline = os.popen(„cvt %s %s %s” % (sys.argv[1], sys.argv[2], sys.argv[3])).read().split(„Modeline”)[1].split(‚ ‚)[0]

output = os.popen(‚xrandr’).read().split(‚ ‚)[1].split(‚ ‚)[0]

mode = modeline.split(‚ ‚)[1].replace(‚”‚, ”)

xprofile.write(„xrandr –newmode %s ” % modeline)

xprofile.write(„xrandr –addmode %s %s ” % (output, mode))

xprofile.write(„xrandr –output %s –mode %s ” % (output, mode))

xprofile.close()

print „Finished. Now log out and log in to your account”
