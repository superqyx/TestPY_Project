import time

class DogDoor(object):
    def __init__(self):
        self.openstate = False

    def open_door(self):
        print("The door is open")
        self.openstate = True

    def close_door(self):
        print("The door is closed")
        self.openstate = False

    def is_open(self):
        return  self.openstate

    def auto_close_door(self):
        time.sleep(5)
        if self.openstate:
            self.close_door()


