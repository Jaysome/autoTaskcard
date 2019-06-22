import os
import sys
import time

import pyautogui
import pywinauto.keyboard as kb

import Inputs

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.2


def lookfortaskcard():
    helper = 0
    while True:
        status_loc = pyautogui.locateCenterOnScreen(resource_path('img\\status.png'),
                                                    grayscale=True)
        if status_loc is not None:
            break
        status_loc = pyautogui.locateCenterOnScreen(resource_path('img\\statusBlue.png'),
                                                    grayscale=True)
        if status_loc is not None:
            break
        status_loc = pyautogui.locateCenterOnScreen(resource_path('img\\statusWhite.png'),
                                                    grayscale=True)
        if status_loc is not None:
            break
        helper += 1
        print('Looking for an opened trax task card...' + '(' + str(helper) + ')', end='\r')
    return status_loc


def filltaskcard(x, y):
    status_loc = (x, y)
    save_loc = (x - 141, y - 82)
    by_loc = (x + 0, y + 45)
    date_loc = (x + 340, y + 113)
    hr_loc = (x + 388, y + 113)
    mn_loc = (x + 410, y + 113)
    station_loc = (x + 470, y + 113)
    resolution_loc = (x + 487, y + 78)
    workclick_loc = (x + 0, y + 315)
    work_tab_loc = (x + 347, y + 437)
    log_page_loc = (x + 400, y - 56)
    # work_loc = (x + 0, y + 220)
    inputs = Inputs.askforinputs()

    pyautogui.click(status_loc)
    pyautogui.typewrite('c')

    pyautogui.click(by_loc)
    eraserhotkey()
    pyautogui.typewrite(inputs.name)

    clickntype(date_loc, inputs.date)
    clickntype(hr_loc, inputs.hr)
    clickntype(mn_loc, inputs.mn)

    pyautogui.click(station_loc)
    eraserhotkey()
    pyautogui.typewrite(inputs.station)

    clickntype(resolution_loc, inputs.resolution)

    pyautogui.doubleClick(workclick_loc)
    time.sleep(0.5)

    pyautogui.doubleClick(work_tab_loc)
    time.sleep(0.5)
    clickntype(log_page_loc, inputs.logpage)

    savetaskcard(save_loc)
    print('\nautoTRAX COMPLETE')


# gets absolute path for dev and pyinstaller
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def clickntype(clicklocation, text):
    pyautogui.click(clicklocation)
    pyautogui.typewrite(text)


def eraser():
    kb.SendKeys("{VK_DELETE 10}")


def eraserhotkey():
    kb.SendKeys('^+{RIGHT}')


def savetaskcard(savecoords):
    pyautogui.click(savecoords)
    greenthumb = None
    tick = 0
    while greenthumb is None:
        greenthumb = pyautogui.locateCenterOnScreen(resource_path('img\\greenThumb.png'),
                                                    confidence=0.8, grayscale=True)
        tick += 1
        if tick > 5:
            break
    pyautogui.click(greenthumb)
    time.sleep(1)
    pyautogui.click(greenthumb)
