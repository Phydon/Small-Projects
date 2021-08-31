from datetime import date

# from ScriptStarter/script_starter import runscript


def deadline(func):
    # check if current day is monday (monday == 0, tuesday == 1, etc.)
    if date.today().weekday() == 0:
        func()


def testfunc():
    print("Just testing...")


if __name__ == "__main__":
    deadline(testfunc)

    # while loop for permanent checking
    # while 1:
    #     deadline(testfunc)
