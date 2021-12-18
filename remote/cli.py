class CLParser(object):
    """
        Takes the user's input and sends a request to the Roku.
    """

    def __init__(self, roku):
        self._roku = roku
        self.program = True
        self._keymode = False


    def print_help(self):
        """
            Prints a list of commands for the user.
        """
        print('e = Play')
        print('w = Up')
        print('s = Down')
        print('a = Left')
        print('d = Right')
        print('z = Enter')
        print('0 = Mute')
        print('[ = Volume Down')
        print('] = Volume Up')
        print('on = Power On')
        print('off = Power Off')
        print('channel = List of available channels')
        print('1 = HDMI1')
        print('2 = HDMI2')
        print('3 = HDMI3')
        print('4 = HDMI4')
        print('q = Back')
        print('k = Keyboard')
        print(' = Backspace')
        print('/ = Exit Remote')


    def handle_input(self, input):
        """
            Takes the input and sends the required request to Roku.

            @param {input} The string input from the user.
        """

        if self._keymode == True:
            if input == 'esc':
                print('Exiting keyboard mode.')
                self._keymode = False
            else:
                if len(input)>1:
                    for i in range(len(input)):
                        self._roku.send_command(f'Lit_{input[i]}')
                else:
                    self._roku.send_command(f'Lit_{input}')


        else:
                if input == 'e':
                    print('Play/Pause')
                    self._roku.send_command('Play')
                    return
                if input == ']':
                    print('Volume Up')
                    self._roku.send_command('VolumeUp')
                    return
                if input == '0':
                    print('Mute')
                    self._roku.send_command('VolumeMute')
                    return
                if input == 'off':
                    print('Power Off')
                    self._roku.send_command('PowerOff')
                    return
                if input == 'on':
                    print('Power On')
                    self._roku.send_command('PowerOn')
                    return
                if input == '[':
                    print('Volume Down')
                    self._roku.send_command('VolumeDown')
                    return
                if input == 'w':
                    print('Up')
                    self._roku.send_command('Up')
                    return
                if input == 'h':
                    print('Home')
                    self._roku.send_command('Home')
                    return
                if input == 's':
                    print('Down')
                    self._roku.send_command('Down')
                    return
                if input == 'a':
                    self._roku.send_command('Left')
                    print('Left')
                    return
                if input == 'd':
                    self._roku.send_command('Right')
                    print('Right')
                    return
                if input == 'z':
                    print('Enter')
                    self._roku.send_command('Select')
                    return
                if input == 'netflix':
                    print('Netflix')
                    self._roku.launch_channel('12')
                    return
                if input == 'amazon':
                    print('Amazon')
                    self._roku.launch_channel('13')
                    return
                if input == 'showtime':
                    print('Showtime')
                    self._roku.launch_channel('8838')
                    return
                if input == 'hulu':
                    print('Hulu')
                    self._roku.launch_channel('2285')
                    return
                if input == 'youtube':
                    print('YouTube')
                    self._roku.launch_channel('837')
                    return
                if input == 'peacock':
                    print('Peacock')
                    self._roku.launch_channel('593099')
                    return
                if input == 'channels':
                    print('Please select a channel: ')
                    x = self._roku.get_channel_ids()
                    return
                if input == 'q':
                    print('Back')
                    self._roku.send_command('Back')
                    return
                if input == '1':
                    print('HDMI1')
                    self._roku.send_command('InputHDMI1')
                    return
                if input == '2':
                    print('HDMI2')
                    self._roku.send_command('InputHDMI2')
                    return
                if input == '3':
                    print('HDMI3')
                    self._roku.send_command('InputHDMI3')
                    return
                if input == '4':
                    print('HDMI4')
                    self._roku.send_command('InputHDMI4')
                    return
                if input == 'q':
                    print('Back')
                    self._roku.send_command('Back')
                    return
                if input == 'l':
                    print('Backspace')
                    self._roku.send_command('Backspace')
                    return
                if input == 'k':
                    print('Keyboard Mode')
                    print('Type "esc" at any time to exit keyboard.')
                    self._keymode = True
                    return
                if input == '/':
                    print('Goodbye!')
                    self.program = False
                    return
                if input == 'help':
                    self.print_help()
                    return
                if input == '?':
                    self.print_help()
                    return
                else:
                    print('Try again.')
