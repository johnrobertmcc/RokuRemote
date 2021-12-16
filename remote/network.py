import nmap

class Network(object):
    """
        Class that scans the user's network for available IP addresses.
    """
    def __init__ (self):
        ip = input("Please enter your custom IP router address, or press the Enter key to use default.\n")
        self.ip = ip
        self.roku_ip = False
        self.ip_addresses = []
        self.dict = {}

    def scanner(self):
        """
            Method that scans the network for available IP addresses.
        """
        if len(self.ip) == 0:
            network = '192.168.1.0/24'
        else:
            network = self.ip + '/24'

        print("Scanning please wait...")

        nm = nmap.PortScanner()
        nm.scan(hosts=network, arguments='-sn')
        host_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

        for item in nm.all_hosts():
            print(item)

        for host, status in host_list:
            self.ip_addresses.append(host)

        self.choose_address()

    def choose_address(self):
        """
            Method that allows the user to pick which IP address where their Roku is attached.
        """
        while(self.roku_ip == False):
            if len(self.ip_addresses) > 0:
                for i, address in enumerate(self.ip_addresses):
                    self.dict[str(i)] = address
                    print(i, address)
                print('Are any of these your Roku?: ')
                ipadd = input()

                if ipadd in self.dict:
                    self.roku_ip = self.dict[ipadd]
                else:
                    print("Sorry, I'm not sure how to help you :(")
                    self.roku_ip = 'none found'
                    return
            else:
                return

