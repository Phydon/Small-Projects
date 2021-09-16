import os
import webbrowser


filepath = "path/to/file.pdf"


def open_pdf(filepath):
    try:
        os.startfile(filepath)
    except Exception as e:
        print(e)
        print("_" * 50, "\n", "Cannot open file")


def open_pdf_web(filepath):
    try:
        webbrowser.open_new_tab(filepath)
    except Exception as e:
        print(e)
        print("_" * 50, "\n", "Cannot open file")


if __name__ == "__main__":
    open_pdf(filepath)
    open_pdf_web(filepath)
