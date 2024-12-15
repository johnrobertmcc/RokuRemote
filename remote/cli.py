import logging
from typing import Dict, Callable

logging.basicConfig(level=logging.INFO)

class CLParser:
    """
    Takes the user's input and sends a request to the Roku.
    """

    def __init__(self, roku):
        self._roku = roku
        self.program = True
        self._keymode = False

        # Map commands to functions
        self.command_map: Dict[str, Callable[[], None]] = {
              'e': lambda: (print('Play/Pause'), self._roku.send_command('Play')),
            ']': lambda: (print('Volume Up'), self._roku.send_command('VolumeUp')),
            '0': lambda: (print('Mute'), self._roku.send_command('VolumeMute')),
            'off': lambda: (print('Power Off'), self._roku.send_command('PowerOff')),
            'on': lambda: (print('Power On'), self._roku.send_command('PowerOn')),
            '[': lambda: (print('Volume Down'), self._roku.send_command('VolumeDown')),
            'w': lambda: (print('Up'), self._roku.send_command('Up')),
            'i': lambda: (print('Info'), self._roku.send_command('Info')),
            'h': lambda: (print('Home'), self._roku.send_command('Home')),
            's': lambda: (print('Down'), self._roku.send_command('Down')),
            'a': lambda: (print('Left'), self._roku.send_command('Left')),
            'd': lambda: (print('Right'), self._roku.send_command('Right')),
            'z': lambda: (print('Enter'), self._roku.send_command('Select')),
            'netflix': lambda: (print('Netflix'), self._roku.launch_channel('12')),
            'amazon': lambda: (print('Amazon'), self._roku.launch_channel('13')),
            'showtime': lambda: (print('Showtime'), self._roku.launch_channel('8838')),
            'hulu': lambda: (print('Hulu'), self._roku.launch_channel('2285')),
            'youtube': lambda: (print('YouTube'), self._roku.launch_channel('837')),
            'peacock': lambda: (print('Peacock'), self._roku.launch_channel('593099')),
            'channels': lambda: (print('Please select a channel: '), self._roku.get_channel_ids()),
            'q': lambda: (print('Back'), self._roku.send_command('Back')),
            '1': lambda: (print('HDMI1'), self._roku.send_command('InputHDMI1')),
            '2': lambda: (print('HDMI2'), self._roku.send_command('InputHDMI2')),
            '3': lambda: (print('HDMI3'), self._roku.send_command('InputHDMI3')),
            '4': lambda: (print('HDMI4'), self._roku.send_command('InputHDMI4')),
            'l': lambda: (print('Backspace'), self._roku.send_command('Backspace')),
            'k': lambda: (print('Keyboard Mode'), print('Type "esc" at any time to exit keyboard.'), setattr(self, '_keymode', True)),
            '/': lambda: (print('Goodbye!'), setattr(self, 'program', False)),
            'help': lambda: self.print_help(),
            '?': lambda: self.print_help()
        }

    def print_help(self):
        """
        Prints a list of commands for the user.
        """
        print("\n".join([
            "e = Play/Pause",
            "q = Back",
            "z = Enter",
            "w = Up",
            "s = Down",
            "a = Left",
            "d = Right",
            "0 = Mute",
            "[ = Volume Down",
            "] = Volume Up",
            "on = Power On",
            "off = Power Off",
            "/ = Exit Remote",
            "Type 'channels' to list all available channels.",
        ]))

    def handle_input(self, prompt: str):
        """
        Takes the input and sends the required request to Roku.

        @param prompt: The string input from the user.
        """
        input = prompt.lower()

        if self._keymode:
            self.handle_keyboard_input(input)
        else:
            action = self.command_map.get(input, lambda: print("Invalid command. Try again."))
            action()

    def handle_keyboard_input(self, input: str):
        """
        Handles input in keyboard mode.

        @param input: The user's input.
        """
        if input == "esc":
            print("Exiting keyboard mode.")
            self._keymode = False
        else:
            for char in input:
                self._roku.send_command(f"Lit_{char}")

    def show_channels(self):
        """
        Fetches and displays available channels.
        """
        print("Please select a channel: ")
        self._roku.get_channel_ids()

    def exit_program(self):
        """
        Exits the program.
        """
        print("Goodbye!")
        self.program = False
