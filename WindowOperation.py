from pynput.keyboard import Key, Controller
import time
import pyautogui as pau
from conf.MyLogger import customlogger

logger = customlogger("WindowOperation")


class WindowOperation:
    def __init__(self):
        logger.info("Window Operation Initiated", extra={'class-name': self.__class__.__name__})
        self.keyboard = Controller()

    def change_tab_backward(self, n=1):
        for i in range(n):
            self.keyboard.press(Key.shift)
            self.keyboard.press(Key.tab)
            time.sleep(0.011)
            self.keyboard.release(Key.shift)
            self.keyboard.release(Key.cmd)

    def change_tab(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.tab)
        time.sleep(0.011)
        self.keyboard.release(Key.tab)
        self.keyboard.release(Key.cmd)

    def terminate_program(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('c')
        time.sleep(0.011)
        self.keyboard.release('c')
        self.keyboard.release(Key.ctrl)

    @staticmethod
    def click_at_coordinates(x_cor, y_cor):
        # Click at the specified location
        pau.click(x=x_cor, y=y_cor)
        time.sleep(0.5)

    def press_enter(self, n=1):
        for i in range(n):
            self.keyboard.press(Key.enter)
            time.sleep(0.011)
            self.keyboard.release(Key.enter)

    def press_tab(self, n=1):
        for i in range(n):
            self.keyboard.press(Key.tab)
            time.sleep(0.011)
            self.keyboard.release(Key.tab)

    def arrow_down(self, n=1):
        for i in range(n):
            self.keyboard.press(Key.down)
            time.sleep(0.011)
            self.keyboard.release(Key.down)

    def arrow_up(self, n=1):
        for i in range(n):
            self.keyboard.press(Key.up)
            time.sleep(0.011)
            self.keyboard.release(Key.up)

    def select_all(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press('a')
        time.sleep(0.011)
        self.keyboard.release('a')
        self.keyboard.release(Key.cmd)

    def press_backspace(self):
        self.keyboard.press(Key.backspace)
        time.sleep(0.011)
        self.keyboard.release(Key.backspace)

    @staticmethod
    def add_delay(time_delay=0.5):
        time.sleep(time_delay)
        
    def scroll_up2(self, remove_follower_x_coordinates, remove_follower_y_coordinates, no_of_times=10):
        # Move mouse to target position
        # Click to ensure focus (optional but recommended)
        self.click_at_coordinates(remove_follower_x_coordinates, remove_follower_y_coordinates)

        # Scroll with smaller increments
        for _ in range(no_of_times):
            # Try negative value if positive doesn't work
            pau.scroll(-5)  # or try pau.scroll(1)
            self.add_delay(1)

    def scroll(self, start_x_coordinates, start_y_coordinates,no_of_time):
        pau.moveTo(start_x_coordinates, start_y_coordinates)
        for _ in range(no_of_time):
            pau.scroll(-100)
            self.add_delay(1)

    @staticmethod
    def drag(start_x_coordinates, start_y_coordinates, end_x_coordinates, end_y_coordinates, no_of_time):
        for _ in range(no_of_time):
            # Move the mouse to the starting
            pau.moveTo(start_x_coordinates, start_y_coordinates)
            # Click and drag to the ending position
            pau.dragTo(end_x_coordinates, end_y_coordinates, duration=1, button='left')


    def auto_type(self, word):
        self.add_delay(0.25)
        logger.info("word is " + word)

        lst_tm = 0.012
        space_tm = 0.011

        count = 0
        if word is not None:
            for i in word:
                count += 1
                if i == " ":
                    self.keyboard.press(' ')
                    self.add_delay(space_tm)
                    self.keyboard.release(' ')
                elif i == "\n":
                    self.keyboard.press(Key.enter)
                    self.add_delay(space_tm)
                    self.keyboard.release(Key.enter)
                else:
                    self.keyboard.press(i)
                    self.add_delay(lst_tm)
                    self.keyboard.release(i)





