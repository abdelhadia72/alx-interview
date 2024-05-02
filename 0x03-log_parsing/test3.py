from signal import signal, SIGINT
from sys import exit

def signal_handler(signum, frame):
    """Signal handler for printing the stats before exiting."""
    raise KeyboardInterrupt
    sys.exit(0)


# Register the signal handler for SIGINT (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)