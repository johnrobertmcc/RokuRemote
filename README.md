# RokuRemote

Has your dog has chewed your Roku remote, while your phone is stuck charging in the bedroom? Well look no further<sup>*</sup>.


<sub>*as long as you're on Linux</sub>

## Instructions:
 - ` python3 setup.py build`
 - `sudo python3 setup.py install`
 -  Get your Roku's IP address. The best way is `ipconfig` and look at connected devices. If unsure, proceeed anyways.
 - `roku <Roku Ip Address>`
    - If unsure of Roku IP address, use command `roku` and you can select from a list of available devices on your network. VPN discouraged.
 -  Type `?` or `help` for a list of available commands

## Updates Planned:
- Currently, this remote only controls Roku and will not control your TV(even if a Roku TV). This prevents:
   - Volume control.
   - Power on/off.
   - Changing to different inputs.
   - And more!
   - Check the progress of these updates on `feature/add-volume`

- This program does currently use an `input()`, and not a keypress listener. 
   - Check the progress for this update on branch `feature/add-keypress-events`

- This program currently utilizes no keyboard entry. This is ridiculously annoying.
   - There is no active branch for this currently. Immediate release planned, however. It is the most annoying aspect of any remote.

## Noted Issues:
- If the IP address is not known, the program uses `nmap` to check for available devices. This is not always reliable.
   - If you have an idea, [answer here!](https://stackoverflow.com/questions/70374875/python-nmap-not-showing-same-results-as-terminal)
- Multiple, successive post requests to Roku can timeout if asked in rapid succession.
