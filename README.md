# SimplePowerMenu

This is a simple menu to manage system actions such as shutdown, reboot and logout in linux operating systems, built with Python it was used in Polybar and i3wm.

## Configuration

First, clone the repository

```bash
git clone
```

Then, add to your ``~/.config/polybar/config.ini`` this

```c++
[module/powermenu]
type = custom/text
content = power
click-left = python ~/$PATH/powermenu.py
```

Then add the powermenu module to your modules in ``~/.config/polybar/config.ini``.

```c++
modules-right = powermenu 
```

And reload the configuration file.

If you did everything correctly you should see the word power added to your polybar.

## Screenshots
![SimplePowerMenu](/assets/images/simplepowermenu_v_1.png "Showing Interface")