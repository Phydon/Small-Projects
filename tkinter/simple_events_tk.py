import tkinter


class MyApp(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.createWidgets()
        self.createBindings()

    def createWidgets(self):
        self.label = tkinter.Label(self)
        self.label.pack()
        self.label["text"] = "Bitte sende ein Event"
        self.entry = tkinter.Entry(self)
        self.entry.pack()
        self.ok = tkinter.Button(self)
        self.ok.pack()
        self.ok["text"] = "Beenden"
        self.ok["command"] = self.quit

    def createBindings(self):
        self.entry.bind("Entenhausen", self.eventEntenhausen)
        self.entry.bind("<ButtonPress-1>", self.eventMouseClick)
        self.entry.bind("<MouseWheel>", self.eventMouseWheel)

    def eventEntenhausen(self, event):
        self.label["text"] = "Sie kennen das geheime Passwort!"

    def eventMouseClick(self, event):
        self.label["text"] = "Mausklick an Position " "({},{})".format(event.x, event.y)

    def eventMouseWheel(self, event):
        if event.delta < 0:
            self.label["text"] = (
                "Bitte bewegen Sie das Mausrad" " in die richtige Richtung."
            )
        else:
            self.label["text"] = "Vielen Dank."


root = tkinter.Tk()
gui = MyApp(root)
gui.mainloop()
