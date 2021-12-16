import sys
from .connector import RokuConnector
from .cli import CLParser
from .ip_address import IP

def main():
    """
        Entry file that requires user input and takes the user's request.
    """

    address = IP()

    while(address.ip == False):
        address.get_ip()

    if address.ip == 'none found':
        print("Goodbye!")
    else:
        roku = RokuConnector(address.ip)
        sys.stdout.write('Press / to exit, ? for help\n')
        sys.stdout.write('Connected to Roku on: %s\n' % roku.ip);
        cli = CLParser(roku)

        while(cli.program == True):
            c = input()
            cli.handle_input(c)
