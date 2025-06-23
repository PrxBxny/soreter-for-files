import asyncio
from time import sleep
import keyboard
import os
# class Stopwatch:
#     def __init__(self, seconds = 0):
#         self.seconds = seconds
    
#     def update_timer(self):
#         while True:
#             mins, secs = divmod(self.seconds, 60)
#             self.value = "{:02d}:{:02d}".format(mins, secs)
#             sleep(1)
#             self.seconds += 1
#             return self.value
    
#     def __del__():
#         pass

# sw = Stopwatch
# print(sw)



# async def stopwatch(seconds = 0):
#     while True:
#         await asyncio.sleep(1)
#         seconds += 1
#         print(seconds)
        

# stopwatch()



class Stopwatch():
    def __init__(self, seconds = 0, unmount = True):
        self.seconds = seconds
        self.unmount = unmount

    def pause(self):
        self.unmount = False

    def update_timer(self):
        while self.unmount == True:
            sleep(1)
            self.seconds += 1
            mins, secs = divmod(self.seconds, 60)
            self.value = "{:02d}:{:02d}".format(mins, secs)
            print(f"\r{self.value}", end="")

    def clear():
        os.system('cls')

while True:
    sw = Stopwatch()
    sw.unmount = False
    sw.update_timer()
    keyboard.wait('x')
    sw.unmount = False
    sw.pause()