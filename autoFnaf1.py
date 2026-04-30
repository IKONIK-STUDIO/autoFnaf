""" IMPORTS """
import time
import pyautogui as pg
from screeninfo import get_monitors
import keyboard as ky
import mss

""" VARIABLES """
lookingLeft = False
leftDoorDown = False
rightDoorDown = False

""" FUNCTIONS """
def clickMouse():
    pg.mouseDown()
    time.sleep(0.02)
    pg.mouseUp()
    time.sleep(0.02)

# MOVING FUNCTIONS
def moveToLeftDoor():
    goTo(main, 4, 46)
    pg.click()

def moveToLeftLight():
    goTo(main, 4, 64)
    pg.click()

def moveToRightDoor():
    goTo(main, 94, 48)
    pg.click()

def moveToRightLight():
    goTo(main, 94, 65)
    pg.click()

# CLICKING FUNCTIONS
def camera():
    goTo(main, 50, 79)
    pg.click()
    goTo(main, 50, 94)
    pg.click()
    
    time.sleep(0.5)

    goTo(main, 50, 79)
    pg.click()
    goTo(main, 50, 95)
    pg.click()

def clickLeftDoor():
    global lookingLeft

    if lookingLeft:
        moveToLeftDoor()
        clickMouse()
    else:
        moveToLeftDoor()
        time.sleep(0.7)
        clickMouse()

        lookingLeft = True

def clickLeftLight():
    global lookingLeft

    if lookingLeft:
        moveToLeftLight()
        clickMouse()
    else:
        moveToLeftLight()
        time.sleep(0.7)
        clickMouse()

        lookingLeft = True

def clickRightDoor():
    global lookingLeft

    if not lookingLeft:
        moveToRightDoor()
        clickMouse()
    else:
        moveToRightDoor()
        time.sleep(0.7)
        clickMouse()

        lookingLeft = False

def clickRightLight():
    global lookingLeft

    if not lookingLeft:
        moveToRightLight()
        clickMouse()
    else:
        moveToRightLight()
        time.sleep(0.7)
        clickMouse()

        lookingLeft = False

# HELPER FUNCTIONS
def percentToXY(monitor, px_percent, py_percent):    
    x = monitor.x + int(monitor.width * px_percent / 100)
    y = monitor.y + int(monitor.height * py_percent / 100)
    return x, y

def goTo(monitor, px, py):
    x, y = percentToXY(monitor, px, py)
    pg.moveTo(x, y, duration=0.1)

def XYToPercent(monitor, x, y):
    px_percent = int((x - monitor.x) / monitor.width * 100)
    py_percent = int((y - monitor.y) / monitor.height * 100)
    return px_percent, py_percent

def getPosition():
    return pg.position()

def getColor(x, y):
    img = sct.grab({
        "left": x,
        "top": y,
        "width": 1,
        "height": 1
    })

    p = img.pixel(0, 0)
    return (p[2], p[1], p[0])  # RGB

def colorMatch(c1, c2, tol=15):
    return (
        abs(c1[0] - c2[0]) < tol and
        abs(c1[1] - c2[1]) < tol and
        abs(c1[2] - c2[2]) < tol
    )

""" MAIN """
# Create an instance of mss
sct = mss.mss()

# List available monitors
monitors = get_monitors()
for i, m in enumerate(monitors, start=1):
    print(f"Monitor {i}: {m}")
print("\n")

# Ask user to select a monitor
monitor_number = int(input("Enter the monitor number (1, 2, 3, ...): "))
if monitor_number < 1 or monitor_number > len(monitors):
    raise ValueError(f"Monitor number must be between 1 and {len(monitors)}")

# Get the selected monitor
main = monitors[monitor_number - 1]
print("  offset=", main.x, main.y)
print("  size=", main.width, main.height)

while True:
    if ky.is_pressed('c'):
        x, y = getPosition()
        print(getColor(x, y))
        time.sleep(0.2)
    if ky.is_pressed('x'):
        x, y = getPosition()
        print(XYToPercent(main, x, y))
        time.sleep(0.2)

    if ky.is_pressed('q'):
        clickLeftDoor()
        time.sleep(0.2)
    if ky.is_pressed('a'):
        clickLeftLight()
        time.sleep(0.2)
    if ky.is_pressed('w'):
        clickRightDoor()
        time.sleep(0.2)
    if ky.is_pressed('s'):
        clickRightLight()
        time.sleep(0.2)
    
    if ky.is_pressed('e'):
        camera()
        time.sleep(0.2)