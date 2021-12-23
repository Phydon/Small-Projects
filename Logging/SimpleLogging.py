import os
import json
import datetime as dt


json_logging = os.path.join(os.path.dirname(__file__), "logging.json")


# helper function, returns True if file exists and is not empty
def is_non_zero_file(filepath):
    return os.path.isfile(filepath) and os.path.getsize(filepath) > 0


def logging(inp_msg, filepath=json_logging):
    try:
        if not is_non_zero_file(filepath):
            with open(filepath, "w") as f:
                new_dict = {}
                json_obj = json.dumps(new_dict, indent=4)
                f.write(json_obj)

        with open(filepath, "r+") as j:
            logs = json.load(j)

            date = str(dt.datetime.now())
            item = {date: str(inp_msg)}
            logs.update(item)

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
