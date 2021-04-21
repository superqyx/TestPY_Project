import DogDoor
import Remote

if __name__ == '__main__':
    dogdoor = DogDoor.DogDoor()
    remote_control = Remote.Remote(dogdoor)
    print("Fido barks to go outsides...")
    remote_control.press_button()
    print("Fido has gone outside...")
    remote_control.press_button()
    print("Fido's all done...")
    remote_control.press_button()
    print("fido has back inside...")
    remote_control.press_button()

