import winsound
from time import sleep


def main():
    # set timer
    timer = int(input("Set Timer: "))
    
    sleep(timer)

    # play sound / alarm
    print("ALARM!")
    winsound.PlaySound("sound.wav", winsound.SND_FILENAME)

    for _ in range(2):
        print("BEEP")
        winsound.Beep(800, 250)
        sleep(0.1)


if __name__ == "__main__":
    main()
