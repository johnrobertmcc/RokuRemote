# RokuRemote

Has your dog has chewed your Roku remote, while your phone is stuck charging in the bedroom? Well look no further<sup>*</sup>.


<sub>*as long as you're on Linux</sub>

Available commands:
```
e = Play/Pause
q = Back
z = Enter
w = Up
s = Down
a = Left
d = Right
0 = Mute
[ = Volume Down
] = Volume Up
on = Power On
off = Power Off
1 = HDMI1
2 = HDMI2
3 = HDMI3
4 = HDMI4
i = Info
k = Keyboard
l = Backspace
/ = Exit Remote

----------

Type "channels" to see all available channels.
Quick Channels available:
  Netflix
  YouTube
  Amazon
  Hulu

```

**UPDATE 12/17/21**
This now supports keyboard entry.

## Instructions:
 - ` python3 setup.py build`
 - `sudo python3 setup.py install`
 -  Get your Roku's IP address. The best way is `ipconfig` and look at connected devices. If unsure, proceeed anyways.
 - `roku <Roku Ip Address>`
    - If unsure of Roku IP address, use command `roku` and you can select from a list of available devices on your network. VPN discouraged.
 -  Type `?` or `help` for a list of available commands

## Updates Planned:

- This program does currently use an `input()`, and not a keypress listener. 
   - Check the progress for this update on branch `feature/add-keypress-events`
