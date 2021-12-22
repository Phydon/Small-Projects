import os
import json
import datetime as dt


json_logging = os.path.join(os.path.dirname(__file__), "logging.json")


def logging(inp_msg, filepath=json_logging):
    try:
        with open(filepath, "r+") as j:
            logs = json.load(j)

            date = str(dt.datetime.now())
            item = [{date: str(inp_msg)}]
            logs["logging"].append(item)

            j.seek(0)
            json.dump(logs, j, indent=4)
    except Exception as e:
        print(e)
        print("Error while writing to logging file")


def main():
    try:
        print("This should not work" + 2)
    except Exception as e:
        logging(e)
        print("Error has been logged")


if __name__ == "__main__":
    main()
