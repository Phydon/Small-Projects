import os
import subprocess


default_file = os.path.join(os.path.dirname(__file__), "defaultfile.py")


def runscript(filepath=default_file):
    try:
        subprocess.run("python {}".format(filepath))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    runscript()
    # runscript("C:/Users/Pohl/Desktop/main/testfile.py")
