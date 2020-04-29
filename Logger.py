__author__ = 'Pavel Yatvetsky'

import sys, os
from time import strftime

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.filename = 'Log_' + strftime('%Y%m%d-%H%M') + '.log'
        self.dir = '.'
        self.load_file()

    def write(self, message):
        # Ignore backspaces produced by the Keras Progbar:
        if '\b' in message: return
        # Output to console:
        self.terminal.write(message.replace('\r', '\n'))
        # Output to file:
        if self.log.closed:
            self.terminal.write('[Logger: off]')
        else:
            self.log.write(message)
            if '\r' in message or '\n' in message:
                self.log.flush()

    def flush(self): pass

    def move_file(self, dir, filename=None):
        OldFilename = self.filename
        if filename is None:
            self.filename = dir + '/' + OldFilename
        else:
            self.filename = dir + '/' + filename
        if not os.path.exists(dir):
            print('Creating dir:', dir)
            os.mkdir(dir)
        else:
            # FileExistsError:
            temp_filename = self.filename
            ii = 0
            while os.path.exists(self.filename):
                self.filename = temp_filename[:-4] + '_%d' % ii + temp_filename[-4:]
                ii+=1

        self.log.close()
        os.rename(OldFilename, self.filename)
        self.load_file()

    def load_file(self):
        self.log = open(self.filename, "a")

    def __getattr__(self, item):
        return self.terminal.__getattribute__(item)


sys.stdout = sys.stderr = Logger()
