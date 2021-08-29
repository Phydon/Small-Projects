import tkinter.messagebox


run = True
while run:
    userclick = tkinter.messagebox.askokcancel(
        "Installation", "Die Installation von Virus.exe wird jetzt gestartet."
    )

    if userclick:
        tkinter.messagebox.showinfo(
            "Setup beendet",
            "Die Installation von Virus.exe wurde erfolgreich abgeschlossen.",
        )
        run = False
        break
    else:
        continue
