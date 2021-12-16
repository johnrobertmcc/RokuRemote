import requests


class RokuConnector(object):

    def __init__(self, ip = False):
        self.ip = ip
        self.uri = 'http://{}:8060'.format(self.ip)

    def send_command(self, cmd):
        """
            Method that sends the command to Roku.

            @param {cmd} Sends the proper command.
        """

        commands = '{}/keypress/{}'.format(self.uri, cmd)
        r = requests.post(commands)

        if r.ok:
            return r.ok
        else:
            print('shit sorry try again')
