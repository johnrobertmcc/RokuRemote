import sys
from .connector import RokuConnector
from .cli import CLParser

def main():
    """
        Entry file that requires user input and takes the user's request.
    """
    sys.stdout.write('Press / to exit, ? for help\n')

    roku = RokuConnector(sys.argv[1])
    sys.stdout.write('Connected to Roku on: %s\n' % roku.ip);
    cli = CLParser(roku)

    while(cli.program == True):
        c = input()
        cli.handle_input(c)
