from __future__ import print_function
import Logger
print("This text will be logged.")

import sys

print('Log filename is', sys.stdout.filename)
print("Lets move the log file to a new location 'example_logdir'")
sys.stdout.move_file('example_logdir')
print("From now on, the log file is named", sys.stdout.filename)

print("Have fun using the python std logger!")

