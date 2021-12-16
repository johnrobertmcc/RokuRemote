import sys

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
        print('/ = Exit Remote')


    def handle_input(self, input):
        """
            Takes the input and sends the required request to Roku.

            @param {input} The string input from the user.
        """

        if self._keymode:
            print('keyboard mode!')

        else:
                if input == 'e':
                    print('Play/Pause')
                    self._roku.send_command('Play')
                    return
                if input == 'w':
                    print('Up')
                    self._roku.send_command('up')
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
