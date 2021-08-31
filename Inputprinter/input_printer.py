import os
import sys


settings = {}

settings["Filepath"] = os.path.join(os.path.dirname(__file__), "printertext.txt")


# helper function, returns True if file exists and is not empty
def is_non_zero_file(filepath):
    return os.path.isfile(filepath) and os.path.getsize(filepath) > 0


# main function
def main():
    run = True
    while run:
        print("Input: ")
        inputString = sys.stdin.readline().strip()

        # escape condition
        if inputString == "q" or inputString == "quit":
            run = False
            print("...Aborted.")
            break

        # convert input if needed

        # write input to file
        if len(inputString) != 0:
            try:
                with open(settings["Filepath"], "w") as file:
                    file.write(inputString)
            except FileNotFoundError as e:
                print(e)
                break
        else:
            print("No input. Try again.")
            continue

        # if file not empty, print file
        if is_non_zero_file(settings["Filepath"]):
            try:
                # call local standard printer
                # os.startfile(settings["Filepath"], "print")
                print("File printed.")
                break  # remove for looping over several inputs
            except Exception as e:
                print(e)
                print("Printing failed.")
                break
        else:
            print("File is empty. Cannot print file.")
            break

    return None


if __name__ == "__main__":
    print("Started...")
    main()
