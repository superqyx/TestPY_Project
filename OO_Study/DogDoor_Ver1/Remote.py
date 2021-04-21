import DogDoor

class Remote(object):
    def __init__(self,door):
        self.door = door

    def press_button(self):
        print("Pressing the remote control button...")
        if self.door.is_open():
            self.door.close_door()
        else:
            self.door.open_door()
