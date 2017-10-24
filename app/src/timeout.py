
# ------------------------------------------- #
#
# file: timeout.py
# author: julia drahozal
#
# timeout class
#
# ------------------------------------------- #

# include libraries
import signal
import time

# ------------------------------------------- #

# timeout class
class Timeout ():

    class TimeoutException (Exception):
        pass

    def __init__ (self, sec):
        self.sec = sec

    def __enter__ (self):
        signal.signal (signal.SIGALRM, self.raise_timeout)
        signal.alarm (self.sec)

    def __exit__ (self, *args):
        signal.alarm (0)

    def raise_timeout (self, *args):
        raise Timeout.TimeoutException ()

# ------------------------------------------- #
