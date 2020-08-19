import win32ui
import win32gui
import win32api
import win32con
import numpy as np
import time
import cv2
import keyboard.key_get as key_get
import utils
import os


def grab_screen(region=None):
    """
    region:tuple,(left, top, right,down)
    """

    hwin = win32gui.GetDesktopWindow()
    if region:
        left, top, x2, y2 = region
        width = x2 - left
        height = y2 - top
    else:
        width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
        height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
        left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
        top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

    hwindc = win32gui.GetWindowDC(hwin)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)
    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.frombuffer(signedIntsArray, dtype='uint8')
    # print(img.shape)
    img.shape = (height, width, 4)
    # print(img.shape)
    srcdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwin, hwindc)
    win32gui.DeleteObject(bmp.GetHandle())
    return img


if __name__ == '__main__':
    time.sleep(5)
    t_all = time.time()
    # for i in range(10000):
    while True:
        t = time.time()
        img = grab_screen(region=(1, 26, 801, 626))
        img = cv2.resize(img, (400, 300))
        keys = key_get.key_check()
        print(keys)
        label = utils.key_convert(keys)
        if "Q" in keys and "E" in keys:
            break
        cv2.imshow('win', img)
        cv2.waitKey(1)
        # if not cv2.imwrite(f'{label}_{i}.jpg', img=img):
        #     raise Exception("could not write img")
        # # time.sleep(0.1)
        print("FPS at ", 1 / (time.time() - t))
    print("total FPS as ", 10000 / (time.time() - t_all))
