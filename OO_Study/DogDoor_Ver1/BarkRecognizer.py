import DogDoor

class BarkRecognizer(object):
    def __init__(self, door):
        self.door = door

    def reognize(self):
        print("BarkRecognizer : Heard a bark")
        self.door.open()
        self.door.auto_close_door()