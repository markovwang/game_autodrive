# Citation: Box Of Hats (https://github.com/Box-Of-Hats )

import win32api as wapi

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'APS$/\\":
    keyList.append(char)


def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys


def key_press(key):
    if key == 1:
        return "A"
    if key == 2:
        return "D"
    if key == 3:
        return "W"
    if key == 4:
        return "S"
    if key == 5:
        return "AW"
    if key == 6:
        return "AS"
    if key == 7:
        return "DW"
    if key == 8:
        return "DS"
    return "none"
