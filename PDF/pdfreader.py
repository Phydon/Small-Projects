import os
import re
from pdfminer.high_level import extract_text


FILE = "test.pdf"


def main():
    path = os.path.join(os.path.dirname(__file__), FILE)
    txt = extract_text(path)
    # TODO remove interest rate
    amounts = re.compile(r"[0-9]*\.*[0-9]+,{1}[0-9]+")
    matches = amounts.findall(txt)
    
    for match in matches:
        print(match)


if __name__ == "__main__":
    main()
    
