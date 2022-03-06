import requests
import sys
import xmltodict


class RokuConnector(object):

    def __init__(self, ip=False):
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
            sys.exit()

    def launch_channel(self, cmd):
        """
            Method to launch specfic App channels on Roku.

            @param {cmd} The channel ID of the requested channel.
        """

        channel_launch = '{}/launch/{}'.format(self.uri, cmd)
        r = requests.post(channel_launch)

        if r.ok:
            return r.ok
        else:
            print('nope')
            sys.exit

    def get_channel_ids(self):
        """
            Method to fetch available channel and app ID's from local Roku device.
        """
        channel_list = '{}/query/apps'.format(self.uri)
        r = requests.get(channel_list)

        if r.ok:
            txt = r.text
            obj = xmltodict.parse(txt)
            self.return_channel_list(obj)
        else:
            print('No channels found.')
            sys.exit

    def return_channel_list(self, obj):
        """
            Method to collect channels from Roku query.

            @param {obj} JSON structured data that returns information from available channels.
        """
        channels = []
        app_ids = []
        for idx in range(len(obj['apps']['app'])):
            value = obj['apps']['app'][idx]
            for data in value.keys():
                if data == '#text':
                    channels.append(value[data])
                if data == '@id':
                    app_ids.append(value[data])

        self.choose_channel(channels, app_ids)

    def choose_channel(self, channels, ids):
        """
            Method that prints a list of channels for the user to pick, and switches to inputted channel.
        """
        for idx in range(len(channels)):
            print('{} - {}'.format(idx, channels[idx]))

        print("Enter any letter to return to remote. ")
        i = input()

        if i == '/':
            print("Goodbye!")
            exit()
        elif i.isnumeric():
            self.launch_channel(ids[int(i)])
            print("Changing Channel...")
        else:
            print("Back to remote.")
            return
