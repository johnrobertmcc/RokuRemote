import sys

from .network import Network


class IP:
    """
        Class that declares the computer's and Roku's ip addresses.
    """

    def __init__(self):
        if 2 > len(sys.argv):
            self.running = True
            self.ip = False
        else:
            self.running = False
            self.ip = sys.argv[1]

    def get_ip(self):
        """
            Method that allows the user to entertheir own custom IP address or choose from a populated list.
        """
        while self.running:
            print('Would you like help getting the IP address of your Roku?(Y/N)\n')
            inp = input()

            if inp.upper() == 'Y':
                print("Ok let's find it...")
                self.scrape_network()
            elif inp.upper() == 'N':
                print('Ok bye.')
                sys.exit()
            else:
                print('Try again? (Y/N)')
                self.ip = True

    def scrape_network(self):
        """
            Method that scans the network for available devices on the devices.
        """
        network = Network()
        while not network.roku_ip:
            network.scanner()
        self.ip = network.roku_ip
        self.running = False
